"""Generate trophy SVG using GraphQL API (includes private + collab repos)."""
import json, os, urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = os.environ.get("USERNAME", "lkun45598-lgtm")
OUTPUT = os.environ.get("OUTPUT", "stats/trophy.svg")

def graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=payload,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER], isFork: false) {
      totalCount
      nodes {
        stargazerCount
        forkCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { node { name } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
    }
  }
}
"""

data = graphql(QUERY, {"login": USERNAME})
user = data["data"]["user"]
cc = user["contributionsCollection"]

total_stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])
total_forks = sum(r["forkCount"] for r in user["repositories"]["nodes"])
total_repos = user["repositories"]["totalCount"]
followers = user["followers"]["totalCount"]
total_commits = cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
langs = len(set(name for r in user["repositories"]["nodes"] for e in r["languages"]["edges"] for name in [e["node"]["name"]]))

trophies = [
    ("Stars", total_stars, [(1,"C"),(10,"B"),(50,"A"),(100,"S"),(500,"SS"),(1000,"SSS")]),
    ("Commits", total_commits, [(10,"C"),(100,"B"),(500,"A"),(1000,"S"),(2000,"SS"),(5000,"SSS")]),
    ("Repos", total_repos, [(1,"C"),(5,"B"),(10,"A"),(30,"S"),(50,"SS"),(100,"SSS")]),
    ("Followers", followers, [(1,"C"),(10,"B"),(50,"A"),(100,"S"),(500,"SS"),(1000,"SSS")]),
    ("Forks", total_forks, [(1,"C"),(5,"B"),(10,"A"),(30,"S"),(50,"SS"),(100,"SSS")]),
    ("Languages", langs, [(1,"C"),(3,"B"),(5,"A"),(8,"S"),(10,"SS"),(15,"SSS")]),
]

rank_colors = {
    "SSS": ("#06b6d4","#0891b2"), "SS": ("#0891b2","#0e7490"), "S": ("#0e7490","#155e75"),
    "A": ("#155e75","#164e63"), "B": ("#164e63","#1e3a8a"), "C": ("#1e3a8a","#1e3a8a"), "?": ("#334155","#1e293b"),
}

def get_rank(value, thresholds):
    rank = "?"
    for thresh, r in thresholds:
        if value >= thresh: rank = r
    return rank

W, H, cols, pad = 120, 120, 6, 8
total_w = cols * (W + pad) - pad

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{H}" viewBox="0 0 {total_w} {H}">',
    '<style>',
    '  .label { font: bold 11px "Segoe UI", sans-serif; fill: #cdd9e5; }',
    '  .value { font: bold 16px "Segoe UI", sans-serif; fill: #ffffff; }',
    '  .rank  { font: bold 22px "Segoe UI", sans-serif; }',
    '</style>',
]

for i, (label, value, thresholds) in enumerate(trophies):
    rank = get_rank(value, thresholds)
    fill, stroke = rank_colors.get(rank, rank_colors["?"])
    x = i * (W + pad)
    svg.append(f'<g transform="translate({x}, 0)">')
    svg.append(f'  <rect x="0" y="0" width="{W}" height="{H}" rx="8" fill="#161b22" stroke="{stroke}" stroke-width="1.5" />')
    svg.append(f'  <rect x="{W-32}" y="4" width="28" height="18" rx="4" fill="{stroke}" />')
    svg.append(f'  <text x="{W-18}" y="16" text-anchor="middle" class="rank" style="font-size:11px; fill:#fff;">{rank}</text>')
    svg.append(f'  <text x="{W//2}" y="50" text-anchor="middle" style="font-size:26px;">🏆</text>')
    svg.append(f'  <text x="{W//2}" y="78" text-anchor="middle" class="value">{value}</text>')
    svg.append(f'  <text x="{W//2}" y="100" text-anchor="middle" class="label">{label}</text>')
    svg.append('</g>')

svg.append('</svg>')

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w") as f:
    f.write("\n".join(svg))

print(f"Generated {OUTPUT}")
for label, value, thresholds in trophies:
    print(f"  {label}: {value} (Rank {get_rank(value, thresholds)})")
