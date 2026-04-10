"""Generate GitHub Stats & Languages SVG cards using GraphQL API (includes private + contributed repos)."""
import json, os, sys, urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = os.environ.get("USERNAME", "lkun45598-lgtm")
STATS_OUTPUT = os.environ.get("STATS_OUTPUT", "stats/github-stats.svg")
LANGS_OUTPUT = os.environ.get("LANGS_OUTPUT", "stats/languages.svg")

def graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=payload,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

# === Fetch all stats ===
QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER], isFork: false) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalRepositoriesWithContributedCommits
      restrictedContributionsCount
      contributionCalendar { totalContributions }
    }
  }
}
"""

data = graphql(QUERY, {"login": USERNAME})
user = data["data"]["user"]
cc = user["contributionsCollection"]

# Stats
total_stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])
total_commits = cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
total_prs = cc["totalPullRequestContributions"]
total_issues = cc["totalIssueContributions"]
total_contribs = cc["totalRepositoriesWithContributedCommits"]
followers = user["followers"]["totalCount"]

# Rank calculation (same as github-readme-stats)
import math
def calc_rank(commits, prs, issues, stars, followers):
    score = (commits * 0.25 + prs * 0.5 + issues * 0.25 + stars * 0.25 + followers * 0.5)
    level = 1 - (1 / (1 + math.exp(-((score - 50) / 25))))
    if level <= 0.01: return "S+", level
    if level <= 0.05: return "S", level
    if level <= 0.15: return "A++", level
    if level <= 0.25: return "A+", level
    if level <= 0.45: return "A", level
    if level <= 0.65: return "B+", level
    return "B", level

rank, rank_pct = calc_rank(total_commits, total_prs, total_issues, total_stars, followers)
ring_pct = 1 - rank_pct  # for ring animation

# Languages aggregation
lang_totals = {}
for repo in user["repositories"]["nodes"]:
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        color = edge["node"]["color"] or "#858585"
        lang_totals[name] = lang_totals.get(name, {"size": 0, "color": color})
        lang_totals[name]["size"] += edge["size"]

# Sort and get top languages (exclude Jupyter Notebook)
langs_sorted = sorted(
    [(k, v) for k, v in lang_totals.items() if k != "Jupyter Notebook"],
    key=lambda x: x[1]["size"], reverse=True
)[:8]
total_size = sum(v["size"] for _, v in langs_sorted)

stats_items = [
    ("Total Stars Earned", str(total_stars), "⭐"),
    ("Total Commits", str(total_commits), "📝"),
    ("Total PRs", str(total_prs), "🔀"),
    ("Total Issues", str(total_issues), "❗"),
    ("Contributed to", str(total_contribs), "📦"),
]

# === Generate Stats SVG ===
W, H = 495, 195
svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" rx="4.5" fill="#0d1117" />
<text x="25" y="35" fill="#0891b2" font-family="\'Segoe UI\', Ubuntu, sans-serif" font-weight="600" font-size="18">My GitHub Statistics</text>
'''

# Stats list
for i, (label, value, icon) in enumerate(stats_items):
    y = 65 + i * 25
    svg += f'<text x="25" y="{y}" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-size="14" font-weight="600">{icon} {label}:</text>\n'
    svg += f'<text x="240" y="{y}" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-size="14" font-weight="700">{value}</text>\n'

# Rank circle
cx, cy, r = 400, 110, 40
circumference = 2 * 3.14159 * r
offset = circumference * (1 - ring_pct)
svg += f'''
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#0891b2" stroke-width="6" opacity="0.2" />
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#0891b2" stroke-width="6" stroke-dasharray="{circumference:.1f}" stroke-dashoffset="{offset:.1f}" stroke-linecap="round" transform="rotate(-90 {cx} {cy})" opacity="0.8" />
<text x="{cx}" y="{cy + 8}" text-anchor="middle" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-weight="800" font-size="24">{rank}</text>
'''

svg += '</svg>'

os.makedirs(os.path.dirname(STATS_OUTPUT), exist_ok=True)
with open(STATS_OUTPUT, "w") as f:
    f.write(svg)
print(f"Generated {STATS_OUTPUT}: stars={total_stars} commits={total_commits} prs={total_prs} rank={rank}")

# === Generate Languages SVG ===
LW, LH = 350, 195
bar_h = 8
lsvg = f'''<svg width="{LW}" height="{LH}" viewBox="0 0 {LW} {LH}" xmlns="http://www.w3.org/2000/svg">
<rect width="{LW}" height="{LH}" rx="4.5" fill="#0d1117" />
<text x="25" y="35" fill="#0891b2" font-family="\'Segoe UI\', Ubuntu, sans-serif" font-weight="600" font-size="18">Most Used Languages</text>
'''

# Progress bar
bar_x, bar_y, bar_w = 25, 50, LW - 50
lsvg += f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="4" fill="#161b22" />\n'
offset_x = bar_x
for name, info in langs_sorted:
    pct = info["size"] / total_size
    w = pct * bar_w
    lsvg += f'<rect x="{offset_x:.1f}" y="{bar_y}" width="{w:.1f}" height="{bar_h}" fill="{info["color"]}" />\n'
    offset_x += w

# Round corners
lsvg += f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="4" fill="none" stroke="#0d1117" stroke-width="0.5" />\n'

# Language list (2 columns)
cols = 2
per_col = (len(langs_sorted) + 1) // 2
for i, (name, info) in enumerate(langs_sorted):
    col = i // per_col
    row = i % per_col
    x = 25 + col * 155
    y = 80 + row * 25
    pct = info["size"] / total_size * 100
    lsvg += f'<circle cx="{x}" cy="{y - 4}" r="5" fill="{info["color"]}" />\n'
    lsvg += f'<text x="{x + 12}" y="{y}" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-size="12">{name} <tspan fill="#64748b">{pct:.1f}%</tspan></text>\n'

lsvg += '</svg>'

with open(LANGS_OUTPUT, "w") as f:
    f.write(lsvg)
print(f"Generated {LANGS_OUTPUT}: {len(langs_sorted)} languages")
for name, info in langs_sorted:
    print(f"  {name}: {info['size']/total_size*100:.1f}%")
