"""Generate Language Donut Chart & Skills Radar Chart SVGs."""
import json, os, math, urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = os.environ.get("USERNAME", "lkun45598-lgtm")
DONUT_OUTPUT = os.environ.get("DONUT_OUTPUT", "stats/lang-donut.svg")
RADAR_OUTPUT = os.environ.get("RADAR_OUTPUT", "stats/skills-radar.svg")

def graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=payload,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

QUERY = """
query($login: String!) {
  user(login: $login) {
    pullRequests { totalCount }
    issues { totalCount }
    followers { totalCount }
    repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, ISSUE, REPOSITORY]) { totalCount }
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

# === Language data ===
lang_totals = {}
for repo in user["repositories"]["nodes"]:
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        color = edge["node"]["color"] or "#858585"
        lang_totals[name] = lang_totals.get(name, {"size": 0, "color": color})
        lang_totals[name]["size"] += edge["size"]

langs_sorted = sorted(
    [(k, v) for k, v in lang_totals.items() if k != "Jupyter Notebook"],
    key=lambda x: x[1]["size"], reverse=True
)[:6]
total_size = sum(v["size"] for _, v in langs_sorted)

# === Generate Donut Chart ===
W, H = 400, 300
cx, cy, R, r = 140, 150, 100, 55  # outer/inner radius

svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<rect width="{W}" height="{H}" rx="4.5" fill="#0d1117" />
<text x="{W//2}" y="30" text-anchor="middle" fill="#0891b2" font-family="'Segoe UI', Ubuntu, sans-serif" font-weight="600" font-size="16">Language Distribution</text>
'''

# Draw donut segments
angle = -90  # start from top
for name, info in langs_sorted:
    pct = info["size"] / total_size
    sweep = pct * 360
    # Arc path
    start_rad = math.radians(angle)
    end_rad = math.radians(angle + sweep)
    
    x1_o = cx + R * math.cos(start_rad)
    y1_o = cy + R * math.sin(start_rad)
    x2_o = cx + R * math.cos(end_rad)
    y2_o = cy + R * math.sin(end_rad)
    x1_i = cx + r * math.cos(end_rad)
    y1_i = cy + r * math.sin(end_rad)
    x2_i = cx + r * math.cos(start_rad)
    y2_i = cy + r * math.sin(start_rad)
    
    large = 1 if sweep > 180 else 0
    
    d = f"M {x1_o:.1f} {y1_o:.1f} A {R} {R} 0 {large} 1 {x2_o:.1f} {y2_o:.1f} L {x1_i:.1f} {y1_i:.1f} A {r} {r} 0 {large} 0 {x2_i:.1f} {y2_i:.1f} Z"
    svg += f'<path d="{d}" fill="{info["color"]}" stroke="#0d1117" stroke-width="2" />\n'
    angle += sweep

# Center text
svg += f'<circle cx="{cx}" cy="{cy}" r="{r-2}" fill="#0d1117" />\n'
svg += f'<text x="{cx}" y="{cy-5}" text-anchor="middle" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-weight="700" font-size="20">{len(lang_totals)}</text>\n'
svg += f'<text x="{cx}" y="{cy+15}" text-anchor="middle" fill="#64748b" font-family="\'Segoe UI\', sans-serif" font-size="11">Languages</text>\n'

# Legend (right side)
for i, (name, info) in enumerate(langs_sorted):
    lx, ly = 265, 65 + i * 35
    pct = info["size"] / total_size * 100
    svg += f'<circle cx="{lx}" cy="{ly}" r="6" fill="{info["color"]}" />\n'
    svg += f'<text x="{lx+14}" y="{ly+4}" fill="#ffffff" font-family="\'Segoe UI\', sans-serif" font-size="13" font-weight="600">{name}</text>\n'
    svg += f'<text x="{lx+14}" y="{ly+18}" fill="#64748b" font-family="\'Segoe UI\', sans-serif" font-size="11">{pct:.1f}%</text>\n'

svg += '</svg>'

os.makedirs(os.path.dirname(DONUT_OUTPUT), exist_ok=True)
with open(DONUT_OUTPUT, "w") as f:
    f.write(svg)
print(f"Generated {DONUT_OUTPUT}")

# === Skills Radar Chart ===
total_stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])
total_commits = cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
total_prs = user["pullRequests"]["totalCount"]
total_repos = user["repositories"]["totalCount"]
total_contribs = user["repositoriesContributedTo"]["totalCount"]
followers = user["followers"]["totalCount"]

# Normalize to 0-1 (with reasonable caps)
def norm(val, cap):
    return min(val / cap, 1.0)

skills = [
    ("Commits", norm(total_commits, 2000)),
    ("Stars", norm(total_stars, 200)),
    ("PRs", norm(total_prs, 100)),
    ("Repos", norm(total_repos, 50)),
    ("Followers", norm(followers, 100)),
    ("Contrib", norm(total_contribs, 20)),
]

RW, RH = 400, 350
rcx, rcy, rR = 200, 190, 120
n = len(skills)

rsvg = f'''<svg width="{RW}" height="{RH}" viewBox="0 0 {RW} {RH}" xmlns="http://www.w3.org/2000/svg">
<rect width="{RW}" height="{RH}" rx="4.5" fill="#0d1117" />
<text x="{RW//2}" y="30" text-anchor="middle" fill="#0891b2" font-family="'Segoe UI', Ubuntu, sans-serif" font-weight="600" font-size="16">Skills Radar</text>
'''

# Draw grid rings
for level in [0.25, 0.5, 0.75, 1.0]:
    points = []
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        px = rcx + rR * level * math.cos(a)
        py = rcy + rR * level * math.sin(a)
        points.append(f"{px:.1f},{py:.1f}")
    rsvg += f'<polygon points="{" ".join(points)}" fill="none" stroke="#1e293b" stroke-width="1" />\n'

# Draw axis lines
for i in range(n):
    a = math.radians(-90 + i * 360 / n)
    px = rcx + rR * math.cos(a)
    py = rcy + rR * math.sin(a)
    rsvg += f'<line x1="{rcx}" y1="{rcy}" x2="{px:.1f}" y2="{py:.1f}" stroke="#1e293b" stroke-width="1" />\n'

# Draw data polygon
data_points = []
for i, (label, val) in enumerate(skills):
    a = math.radians(-90 + i * 360 / n)
    px = rcx + rR * val * math.cos(a)
    py = rcy + rR * val * math.sin(a)
    data_points.append(f"{px:.1f},{py:.1f}")

rsvg += f'<polygon points="{" ".join(data_points)}" fill="#0891b2" fill-opacity="0.25" stroke="#06b6d4" stroke-width="2.5" />\n'

# Data points and labels
for i, (label, val) in enumerate(skills):
    a = math.radians(-90 + i * 360 / n)
    # Data dot
    px = rcx + rR * val * math.cos(a)
    py = rcy + rR * val * math.sin(a)
    rsvg += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#06b6d4" stroke="#0d1117" stroke-width="2" />\n'
    # Label
    lx = rcx + (rR + 25) * math.cos(a)
    ly = rcy + (rR + 25) * math.sin(a)
    anchor = "middle"
    if math.cos(a) > 0.3: anchor = "start"
    elif math.cos(a) < -0.3: anchor = "end"
    rsvg += f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" fill="#cdd9e5" font-family="\'Segoe UI\', sans-serif" font-size="13" font-weight="600">{label}</text>\n'
    # Value below label
    rsvg += f'<text x="{lx:.1f}" y="{ly+14:.1f}" text-anchor="{anchor}" fill="#64748b" font-family="\'Segoe UI\', sans-serif" font-size="10">{int(val*100)}%</text>\n'

rsvg += '</svg>'

with open(RADAR_OUTPUT, "w") as f:
    f.write(rsvg)
print(f"Generated {RADAR_OUTPUT}")
for label, val in skills:
    print(f"  {label}: {int(val*100)}%")
