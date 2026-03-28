#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request


GRAPHQL_QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    login
    followers {
      totalCount
    }
    repositories(first: 100, after: $cursor, privacy: PUBLIC, isFork: false) {
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        name
        url
        stargazerCount
      }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
      totalCommitContributions
    }
  }
}
"""


DEMO_STATS = {
    "login": "lkun45598-lgtm",
    "followers": 18,
    "public_repos": 12,
    "stars": 41,
    "contributions_last_year": 286,
    "commits_last_year": 214,
    "active_days_last_year": 104,
    "current_streak_days": 13,
    "longest_streak_days": 29,
    "top_repo_name": "SST_FTM",
    "top_repo_stars": 16,
    "top_repo_url": "https://github.com/lkun45598-lgtm/SST_FTM",
    "updated_at": "demo mode",
}

README_STATS_PATTERN = re.compile(
    r"<!-- stats:start -->.*?<!-- stats:end -->",
    flags=re.DOTALL,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", default=os.environ.get("GITHUB_LOGIN", "lkun45598-lgtm"))
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    parser.add_argument("--output-dir", default="assets")
    parser.add_argument("--demo", action="store_true")
    return parser.parse_args()


def github_graphql(token: str, query: str, variables: dict[str, object]) -> dict[str, object]:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "lkun-profile-stats",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub GraphQL request failed: {message}") from exc

    if "errors" in data:
        raise RuntimeError(f"GitHub GraphQL returned errors: {data['errors']}")
    return data


def fetch_stats(login: str, token: str) -> dict[str, object]:
    cursor = None
    total_stars = 0
    followers = 0
    public_repos = 0
    contributions_last_year = 0
    commits_last_year = 0
    active_days_last_year = 0
    current_streak_days = 0
    longest_streak_days = 0
    top_repo_name = ""
    top_repo_stars = 0
    top_repo_url = ""

    while True:
        data = github_graphql(token, GRAPHQL_QUERY, {"login": login, "cursor": cursor})
        user = data["data"]["user"]
        if user is None:
            raise RuntimeError(f"GitHub user '{login}' not found.")

        if cursor is None:
            followers = user["followers"]["totalCount"]
            public_repos = user["repositories"]["totalCount"]
            contributions_last_year = user["contributionsCollection"]["contributionCalendar"]["totalContributions"]
            commits_last_year = user["contributionsCollection"]["totalCommitContributions"]
            days = []
            for week in user["contributionsCollection"]["contributionCalendar"]["weeks"]:
                days.extend(week["contributionDays"])

            contribution_counts = [int(day["contributionCount"]) for day in days]
            active_days_last_year = sum(1 for count in contribution_counts if count > 0)
            current_streak_days, longest_streak_days = compute_streaks(contribution_counts)

        for repo in user["repositories"]["nodes"]:
            stars = int(repo["stargazerCount"])
            total_stars += stars
            if stars > top_repo_stars:
                top_repo_name = repo["name"]
                top_repo_stars = stars
                top_repo_url = repo["url"]

        page_info = user["repositories"]["pageInfo"]
        if not page_info["hasNextPage"]:
            break
        cursor = page_info["endCursor"]

    return {
        "login": login,
        "followers": followers,
        "public_repos": public_repos,
        "stars": total_stars,
        "contributions_last_year": contributions_last_year,
        "commits_last_year": commits_last_year,
        "active_days_last_year": active_days_last_year,
        "current_streak_days": current_streak_days,
        "longest_streak_days": longest_streak_days,
        "top_repo_name": top_repo_name,
        "top_repo_stars": top_repo_stars,
        "top_repo_url": top_repo_url,
        "updated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def format_number(value: int) -> str:
    return f"{value:,}"


def load_cached_stats(json_path: pathlib.Path) -> dict[str, object]:
    if not json_path.exists():
        raise RuntimeError("GITHUB_TOKEN is required unless --demo is used or cached stats already exist.")
    return json.loads(json_path.read_text(encoding="utf-8"))


def compute_streaks(contribution_counts: list[int]) -> tuple[int, int]:
    longest = 0
    current = 0
    running = 0

    for count in contribution_counts:
        if count > 0:
            running += 1
            longest = max(longest, running)
        else:
            running = 0

    for count in reversed(contribution_counts):
        if count > 0:
            current += 1
        else:
            break

    return current, longest


def render_stats_section(stats: dict[str, object]) -> str:
    updated_at = html.escape(str(stats["updated_at"]))
    metrics: list[tuple[str, str]] = [
        ("Public Repos", format_number(int(stats["public_repos"]))),
        ("Total Stars", format_number(int(stats["stars"]))),
        ("Followers", format_number(int(stats["followers"]))),
        ("Contributions (1y)", format_number(int(stats["contributions_last_year"]))),
        ("Commits (1y)", format_number(int(stats["commits_last_year"]))),
    ]
    optional_metrics = [
        ("active_days_last_year", "Active Days (1y)"),
        ("current_streak_days", "Current Streak"),
        ("longest_streak_days", "Best Streak"),
    ]
    for key, label in optional_metrics:
        if key in stats:
            metrics.append((label, format_number(int(stats[key]))))

    row_size = len(metrics) if len(metrics) <= 6 else 4
    rows = []
    for index in range(0, len(metrics), row_size):
        chunk = metrics[index:index + row_size]
        cells = "\n".join(
            f'    <td align="center"><strong>{html.escape(value)}</strong><br /><sub>{html.escape(label)}</sub></td>'
            for label, value in chunk
        )
        rows.append(f"  <tr>\n{cells}\n  </tr>")

    top_repo_name = html.escape(str(stats.get("top_repo_name", "")))
    top_repo_url = html.escape(str(stats.get("top_repo_url", "")))
    top_repo_stars = format_number(int(stats.get("top_repo_stars", 0)))
    if top_repo_name and top_repo_url:
        summary = (
            f'Most-starred public repo: <a href="{top_repo_url}">{top_repo_name}</a> '
            f'({html.escape(top_repo_stars)} stars)'
        )
    elif top_repo_name:
        summary = f"Most-starred public repo: {top_repo_name} ({html.escape(top_repo_stars)} stars)"
    else:
        summary = ""

    if summary:
        summary = f"{summary} · "

    return f"""<!-- stats:start -->
<table>
{chr(10).join(rows)}
</table>

<p align="center">
  <sub>{summary}Updated {updated_at}. This section is refreshed automatically with GitHub Actions.</sub>
</p>
<!-- stats:end -->"""


def update_readme(readme_path: pathlib.Path, stats: dict[str, object]) -> None:
    content = readme_path.read_text(encoding="utf-8")
    replacement = render_stats_section(stats)
    if not README_STATS_PATTERN.search(content):
        raise RuntimeError("Could not find stats markers in README.md.")
    updated = README_STATS_PATTERN.sub(replacement, content, count=1)
    readme_path.write_text(updated, encoding="utf-8")


def main() -> int:
    args = parse_args()
    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "github-stats.json"

    if args.demo:
        stats = dict(DEMO_STATS)
    else:
        if args.token:
            stats = fetch_stats(args.login, args.token)
        else:
            stats = load_cached_stats(json_path)

    readme_path = output_dir.parent / "README.md"

    json_path.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    update_readme(readme_path, stats)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
