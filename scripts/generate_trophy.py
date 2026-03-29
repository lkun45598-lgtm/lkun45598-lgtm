"""Generate a trophy-style SVG from GitHub API data."""
import json, os, sys, urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = os.environ.get("USERNAME", "lkun45598-lgtm")
OUTPUT = os.environ.get("OUTPUT", "stats/trophy.svg")

headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

def api(url):
    req = urllib.request.Request(url, headers=headers)
    return json.loads(urllib.request.urlopen(req).read())

user = api(f"https://api.github.com/users/{USERNAME}")
repos = api(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner")

total_stars = sum(r["stargazers_count"] for r in repos)
total_forks = sum(r["forks_count"] for r in repos)
total_repos = user["public_repos"]
followers = user["followers"]
langs = len(set(r["language"] for r in repos if r.get("language")))

# Fetch commit count from search API
try:
    search = api(f"https://api.github.com/search/commits?q=author:{USERNAME}&per_page=1")
    total_commits = search.get("total_count", 0)
except:
    total_commits = 0

# Trophy definitions: (label, value, thresholds for rank)
trophies = [
    ("Stars", total_stars, [(1, "C"), (10, "B"), (50, "A"), (100, "S"), (500, "SS"), (1000, "SSS")]),
    ("Commits", total_commits, [(10, "C"), (100, "B"), (500, "A"), (1000, "S"), (2000, "SS"), (5000, "SSS")]),
    ("Repos", total_repos, [(1, "C"), (5, "B"), (10, "A"), (30, "S"), (50, "SS"), (100, "SSS")]),
    ("Followers", followers, [(1, "C"), (10, "B"), (50, "A"), (100, "S"), (500, "SS"), (1000, "SSS")]),
    ("Forks", total_forks, [(1, "C"), (5, "B"), (10, "A"), (30, "S"), (50, "SS"), (100, "SSS")]),
    ("Languages", langs, [(1, "C"), (3, "B"), (5, "A"), (8, "S"), (10, "SS"), (15, "SSS")]),
]

rank_colors = {
    "SSS": ("#ff0", "#b8860b"),
    "SS": ("#ffd700", "#b8860b"),
    "S": ("#c0c0c0", "#707070"),
    "A": ("#cd7f32", "#8b4513"),
    "B": ("#6a9fb5", "#3d6d80"),
    "C": ("#90a4ae", "#546e7a"),
    "?": ("#455a64", "#37474f"),
}

def get_rank(value, thresholds):
    rank = "?"
    for thresh, r in thresholds:
        if value >= thresh:
            rank = r
    return rank

W = 120
H = 120
cols = 6
pad = 8
total_w = cols * (W + pad) - pad

svg_parts = [
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

    # Trophy cup shape using paths
    svg_parts.append(f'<g transform="translate({x}, 0)">')

    # Background card
    svg_parts.append(f'  <rect x="0" y="0" width="{W}" height="{H}" rx="8" fill="#161b22" stroke="{stroke}" stroke-width="1.5" />')

    # Rank badge (top-right)
    svg_parts.append(f'  <rect x="{W-32}" y="4" width="28" height="18" rx="4" fill="{stroke}" />')
    svg_parts.append(f'  <text x="{W-18}" y="16" text-anchor="middle" class="rank" style="font-size:11px; fill:#fff;">{rank}</text>')

    # Trophy icon (simple cup)
    cx = W // 2
    svg_parts.append(f'  <text x="{cx}" y="50" text-anchor="middle" style="font-size:26px;">🏆</text>')

    # Value
    svg_parts.append(f'  <text x="{cx}" y="78" text-anchor="middle" class="value">{value}</text>')

    # Label
    svg_parts.append(f'  <text x="{cx}" y="100" text-anchor="middle" class="label">{label}</text>')

    svg_parts.append('</g>')

svg_parts.append('</svg>')

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w") as f:
    f.write("\n".join(svg_parts))

print(f"Generated {OUTPUT} with {len(trophies)} trophies")
for label, value, thresholds in trophies:
    print(f"  {label}: {value} (Rank {get_rank(value, thresholds)})")
