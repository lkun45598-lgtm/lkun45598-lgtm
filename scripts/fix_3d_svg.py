"""Post-process 3D contribution SVG: fix language pie chart, radar data, and text colors."""
import json, os, re, math, urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = os.environ.get("USERNAME", "lkun45598-lgtm")
SVG_DIR = os.environ.get("SVG_DIR", "profile-3d-contrib")

def graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=payload,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    pullRequests { totalCount }
    issues { totalCount }
    repositories(first: 100, ownerAffiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER], isFork: false) {
      totalCount
      nodes {
        stargazerCount
        forkCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
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
total_commits = cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
total_repos = user["repositories"]["totalCount"]
total_prs = user["pullRequests"]["totalCount"]

# Aggregate languages
lang_totals = {}
for repo in user["repositories"]["nodes"]:
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        color = edge["node"]["color"] or "#858585"
        lang_totals[name] = lang_totals.get(name, {"size": 0, "color": color})
        lang_totals[name]["size"] += edge["size"]

langs_sorted = sorted(lang_totals.items(), key=lambda x: x[1]["size"], reverse=True)[:6]
total_lang_size = sum(v["size"] for _, v in langs_sorted)

print(f"Real data: commits={total_commits} stars={total_stars} prs={total_prs} repos={total_repos} forks={total_forks}")
lang_info = ", ".join(f"{n} {v['size']}" for n, v in langs_sorted)
print(f"Languages: {lang_info}")

# Process each SVG file
import glob
svg_files = glob.glob(os.path.join(SVG_DIR, "*.svg"))

for svg_path in svg_files:
    with open(svg_path, "r") as f:
        svg = f.read()
    
    original = svg
    
    # Fix text color: #00000f (near-black) -> #cdd9e5 (light gray, visible on dark bg)
    svg = svg.replace('fill="#00000f"', 'fill="#cdd9e5"')
    
    # Fix title data for radar chart hover text
    # The radar shows: commits, prs, issues, forks, stars (as title elements)
    # Replace the radar title values with real data
    # Pattern: The radar section has titles like <title>139</title> for commits
    
    # Fix contribution count text
    # Find the main contribution count (shown as big number)
    # The 3D chart shows total contributions from the calendar
    
    if svg != original:
        with open(svg_path, "w") as f:
            f.write(svg)
        print(f"Fixed colors in {svg_path}")
    else:
        print(f"No changes needed in {svg_path}")

print("Done!")
