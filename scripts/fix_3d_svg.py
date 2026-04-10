"""Post-process 3D contribution SVGs: replace pie chart & radar data with real data (incl. private repos)."""
import json, os, re, math, urllib.request, glob

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

langs_sorted = sorted(lang_totals.items(), key=lambda x: x[1]["size"], reverse=True)
total_lang_size = sum(v["size"] for _, v in langs_sorted)
# Keep top N, group rest as "other"
MAX_LANGS = 6
top_langs = langs_sorted[:MAX_LANGS]
other_size = sum(v["size"] for _, v in langs_sorted[MAX_LANGS:])
if other_size > 0:
    top_langs.append(("other", {"size": other_size, "color": "#444444"}))

lang_info = ", ".join(f"{n}={v['size']}" for n, v in top_langs)
print(f"Data: commits={total_commits} stars={total_stars} repos={total_repos}")
print(f"Langs: {lang_info}")

# === Radar data: linear normalization with real proportions ===
def norm_linear(val, cap):
    """Linear normalization: real proportion, capped at 1.0"""
    if val <= 0:
        return 0.0
    return min(val / cap, 1.0)

radar_data = [
    ("Commit", norm_linear(total_commits, 1000)),
    ("PullReq", norm_linear(total_prs, 50)),
    ("Issue", norm_linear(user["issues"]["totalCount"], 30)),
    ("Fork", norm_linear(total_forks, 20)),
    ("Repo", norm_linear(total_repos, 30)),
]

# === Generate new pie chart arcs ===
def make_pie_arcs(langs, cx, cy, R_outer, R_inner):
    """Generate SVG arc paths for a donut chart."""
    arcs = []
    angle = -90  # start from top (in degrees)
    anim_delays = ["0;0.2;0.4;0.6;0.8;1;1;1;1",
                   "0;0;0.2;0.4;0.6;0.8;1;1;1",
                   "0;0;0;0.2;0.4;0.6;0.8;1;1",
                   "0;0;0;0;0.2;0.4;0.6;0.8;1",
                   "0;0;0;0;0;0.2;0.4;0.6;0.8",
                   "0;0;0;0;0;0;0.2;0.4;0.6",
                   "0;0;0;0;0;0;0;0.2;0.4"]
    total = sum(v["size"] for _, v in langs)
    for i, (name, info) in enumerate(langs):
        pct = info["size"] / total
        sweep = pct * 360
        if sweep < 0.5:
            angle += sweep
            continue
        
        start_rad = math.radians(angle)
        end_rad = math.radians(angle + sweep)
        
        x1o = cx + R_outer * math.cos(start_rad)
        y1o = cy + R_outer * math.sin(start_rad)
        x2o = cx + R_outer * math.cos(end_rad)
        y2o = cy + R_outer * math.sin(end_rad)
        x1i = cx + R_inner * math.cos(end_rad)
        y1i = cy + R_inner * math.sin(end_rad)
        x2i = cx + R_inner * math.cos(start_rad)
        y2i = cy + R_inner * math.sin(start_rad)
        
        large = 1 if sweep > 180 else 0
        
        d = (f"M{x1o:.6f},{y1o:.6f}"
             f"A{R_outer},{R_outer},0,{large},1,{x2o:.6f},{y2o:.6f}"
             f"L{x1i:.6f},{y1i:.6f}"
             f"A{R_inner},{R_inner},0,{large},0,{x2i:.6f},{y2i:.6f}Z")
        
        count = info["size"]
        anim = anim_delays[min(i, len(anim_delays)-1)]
        arc = (f'<path d="{d}" style="fill: {info["color"]};" stroke="#ffffff" stroke-width="2px">'
               f'<title>{name} {count}</title>'
               f'<animate attributeName="fill-opacity" values="{anim}" dur="3s" repeatCount="1"></animate>'
               f'</path>')
        arcs.append(arc)
        angle += sweep
    return "".join(arcs)

# === Generate new legend ===
def make_legend(langs):
    items = []
    anim_delays = ["0;0.2;0.4;0.6;0.8;1;1;1;1",
                   "0;0;0.2;0.4;0.6;0.8;1;1;1",
                   "0;0;0;0.2;0.4;0.6;0.8;1;1",
                   "0;0;0;0;0.2;0.4;0.6;0.8;1",
                   "0;0;0;0;0;0.2;0.4;0.6;0.8",
                   "0;0;0;0;0;0;0.2;0.4;0.6",
                   "0;0;0;0;0;0;0;0.2;0.4"]
    font_size = 21.666666666666668
    for i, (name, info) in enumerate(langs):
        y_rect = 70.41666666666667 + i * 32.5
        y_text = y_rect + 10.833333333333334
        anim = anim_delays[min(i, len(anim_delays)-1)]
        items.append(
            f'<rect x="0" y="{y_rect}" width="{font_size}" height="{font_size}" '
            f'fill="{info["color"]}" stroke="#ffffff" stroke-width="1px">'
            f'<animate attributeName="fill-opacity" values="{anim}" dur="3s" repeatCount="1"></animate></rect>'
            f'<text dominant-baseline="middle" x="26" y="{y_text}" fill="#00000f" font-size="{font_size}px">{name}'
            f'<animate attributeName="fill-opacity" values="{anim}" dur="3s" repeatCount="1"></animate></text>'
        )
    return "".join(items)

# === Generate radar polygon ===
def make_radar(radar_vals, max_r=156):
    """radar_vals: list of (label, 0-1 normalized value)"""
    n = len(radar_vals)
    points_start = []
    points_end = []
    for i, (label, val) in enumerate(radar_vals):
        a = math.radians(-90 + i * 360 / n)
        # Start small (20% of actual)
        sx = max_r * 0.2 * val * math.cos(a)
        sy = max_r * 0.2 * val * math.sin(a)
        points_start.append(f"{sx:.2f},{sy:.2f}")
        # End at actual value
        ex = max_r * val * math.cos(a)
        ey = max_r * val * math.sin(a)
        points_end.append(f"{ex:.2f},{ey:.2f}")
    
    start_str = " ".join(points_start)
    end_str = " ".join(points_end)
    
    return (f'<polygon style="stroke-width: 4px; stroke: #47a042; fill: #47a042; fill-opacity: 0.5;" '
            f'points="{end_str}">'
            f'<animate attributeName="points" values="{start_str};{end_str}" dur="3s" repeatCount="1" fill="freeze"></animate>'
            f'</polygon>')

# === Process SVG files ===
svg_files = glob.glob(os.path.join(SVG_DIR, "*.svg"))

for svg_path in svg_files:
    with open(svg_path, "r") as f:
        svg = f.read()
    
    original_len = len(svg)
    
    # 1. Replace pie chart arcs (inside translate(130, 130) group)
    pie_pattern = r'(<g transform="translate\(130, 130\)">)(.*?)(</g></g>)'
    pie_match = re.search(pie_pattern, svg, re.DOTALL)
    if pie_match:
        new_arcs = make_pie_arcs(top_langs, 0, 0, 117, 65)
        svg = svg[:pie_match.start(2)] + new_arcs + svg[pie_match.end(2):]
    
    # 2. Replace legend (inside translate(273, 0) group, before the pie group)
    legend_pattern = r'(<g transform="translate\(273, 0\)">)(.*?)(</g><g transform="translate\(130, 130\)">)'
    legend_match = re.search(legend_pattern, svg, re.DOTALL)
    if legend_match:
        new_legend = make_legend(top_langs)
        svg = svg[:legend_match.start(2)] + new_legend + svg[legend_match.end(2):]
    
    # 3. Replace radar polygon
    radar_pattern = r'<polygon style="stroke-width: 4px; stroke: #47a042[^>]*>.*?</polygon>'
    radar_match = re.search(radar_pattern, svg, re.DOTALL)
    if radar_match:
        new_radar = make_radar(radar_data)
        svg = svg[:radar_match.start()] + new_radar + svg[radar_match.end():]
    
    # 4. Replace stars count at bottom (color may be #00000f or #cdd9e5)
    stars_pattern = r'(font-weight: bold;" x="650" y="830" text-anchor="start" fill="#[0-9a-fA-F]+">)\d+(<title>)\d+(</title>)'
    svg = re.sub(stars_pattern, rf'\g<1>{total_stars}\g<2>{total_stars}\g<3>', svg)
    
    if len(svg) != original_len or svg != open(svg_path).read():
        with open(svg_path, "w") as f:
            f.write(svg)
        print(f"Fixed {os.path.basename(svg_path)}")
    else:
        print(f"No changes in {os.path.basename(svg_path)}")

print("Done!")
