#!/usr/bin/env python3
"""Fetch latest Indian paper-leak news via GDELT DOC 2.0 → news.json.

Runs from GitHub Actions on a 6h cron. Commits the result to the repo so
the static site can load same-origin (no client-side CORS proxy needed).
"""
import json, sys, time, urllib.parse, urllib.request

QUERY = '"paper leak" india exam sourcecountry:in'
URL = (
    "https://api.gdeltproject.org/api/v2/doc/doc"
    f"?query={urllib.parse.quote(QUERY)}"
    "&mode=ArtList&format=json&sort=DateDesc&maxrecords=25"
)
UA = "india-paper-leaks-site/1.0 (+https://github.com/RoyRonit/india-paper-leaks-map)"


def fetch(retries=4, base_delay=15):
    for i in range(retries):
        try:
            req = urllib.request.Request(URL, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            print(f"[fetch] attempt {i+1}/{retries} failed: {e}", file=sys.stderr)
            time.sleep(base_delay * (i + 1))
    raise SystemExit("gdelt fetch exhausted retries")


def main():
    raw = fetch()
    data = json.loads(raw)
    articles = data.get("articles", [])

    seen, uniq = set(), []
    for a in articles:
        t = (a.get("title") or "").strip().lower()
        if not t or t in seen:
            continue
        seen.add(t)
        uniq.append({
            "title": (a.get("title") or "").strip(),
            "url": a.get("url"),
            "domain": a.get("domain"),
            "seendate": a.get("seendate"),
            "image": a.get("socialimage") or None,
        })
        if len(uniq) >= 12:
            break

    out = {
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": "GDELT DOC 2.0 — query: " + QUERY,
        "items": uniq,
    }
    with open("news.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"wrote news.json with {len(uniq)} items")


if __name__ == "__main__":
    main()
