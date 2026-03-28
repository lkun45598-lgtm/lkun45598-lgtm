#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
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
        stargazerCount
      }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
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
    "updated_at": "demo mode",
}


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

        for repo in user["repositories"]["nodes"]:
            total_stars += repo["stargazerCount"]

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
        "updated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def format_number(value: int) -> str:
    return f"{value:,}"


def render_metric(x: int, label: str, value: str) -> str:
    return f"""
  <rect x="{x}" y="92" width="184" height="72" rx="16" fill="#FFFFFF" fill-opacity="0.72" stroke="#D9E2EC"/>
  <text x="{x + 20}" y="119" fill="#64748B" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1.6">{html.escape(label.upper())}</text>
  <text x="{x + 20}" y="150" fill="#0F172A" font-family="Georgia, 'Times New Roman', serif" font-size="28" font-weight="700">{html.escape(value)}</text>
"""


def render_svg(stats: dict[str, object]) -> str:
    login = html.escape(str(stats["login"]))
    updated_at = html.escape(str(stats["updated_at"]))
    metrics = [
        ("Public Repos", format_number(int(stats["public_repos"]))),
        ("Total Stars", format_number(int(stats["stars"]))),
        ("Followers", format_number(int(stats["followers"]))),
        ("Contributions (1y)", format_number(int(stats["contributions_last_year"]))),
        ("Commits (1y)", format_number(int(stats["commits_last_year"]))),
    ]
    metric_blocks = "".join(render_metric(42 + 208 * index, label, value) for index, (label, value) in enumerate(metrics))

    return f"""<svg width="1120" height="208" viewBox="0 0 1120 208" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">GitHub stats for {login}</title>
  <desc id="desc">Auto-updated GitHub statistics card.</desc>

  <defs>
    <linearGradient id="bg" x1="18" y1="18" x2="1098" y2="190" gradientUnits="userSpaceOnUse">
      <stop stop-color="#FBF8F3"/>
      <stop offset="0.5" stop-color="#F4FAF8"/>
      <stop offset="1" stop-color="#F2F6FF"/>
    </linearGradient>
    <linearGradient id="stripe" x1="28" y1="26" x2="28" y2="182" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0F766E"/>
      <stop offset="1" stop-color="#2563EB"/>
    </linearGradient>
    <filter id="shadow" x="-10" y="-10" width="1140" height="228" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g filter="url(#shadow)">
    <rect x="10" y="10" width="1100" height="188" rx="24" fill="url(#bg)"/>
    <rect x="10" y="10" width="1100" height="188" rx="24" stroke="#D9E2EC"/>
  </g>

  <rect x="24" y="24" width="6" height="160" rx="3" fill="url(#stripe)"/>

  <text x="44" y="46" fill="#0F766E" fill-opacity="0.92" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" letter-spacing="2.1">GITHUB PULSE</text>
  <text x="44" y="78" fill="#0F172A" font-family="Georgia, 'Times New Roman', serif" font-size="30" font-weight="700">Live GitHub Stats</text>
  <text x="44" y="104" fill="#334155" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="15">Public GitHub activity for {login}, refreshed automatically through GitHub Actions.</text>

{metric_blocks}

  <text x="44" y="184" fill="#64748B" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">UPDATED {updated_at}</text>
</svg>
"""


def main() -> int:
    args = parse_args()
    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.demo:
        stats = dict(DEMO_STATS)
    else:
        if not args.token:
            raise RuntimeError("GITHUB_TOKEN is required unless --demo is used.")
        stats = fetch_stats(args.login, args.token)

    json_path = output_dir / "github-stats.json"
    svg_path = output_dir / "github-stats.svg"

    json_path.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    svg_path.write_text(render_svg(stats), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
