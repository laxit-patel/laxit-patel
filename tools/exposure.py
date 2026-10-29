"""Generate EXPOSURE.md from inventory.json: every technology, how many projects used it, how recently, and in what capacity.

    python3 tools/exposure.py          # write EXPOSURE.md
    python3 tools/exposure.py --check  # fail if EXPOSURE.md is out of date (CI)
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUPS = [
    ("languages", "Languages"),
    ("frameworks", "Frameworks and libraries"),
    ("data", "Data stores and formats"),
    ("infra", "Infrastructure, cloud and delivery"),
    ("ai", "AI and LLM"),
    ("platforms", "Platforms"),
]
REQUIRED = {"id", "name", "ownership", "role", "status", "visibility", "last_activity", "summary"}
ALLOWED = {
    "ownership": {"personal", "client", "employer", "learning"},
    "role": {"author", "lead", "contributor"},
    "status": {"live", "working", "prototype", "skeleton", "archived"},
    "visibility": {"public", "private", "anonymised"},
}


def load() -> dict:
    inventory = json.loads((ROOT / "inventory.json").read_text())
    ids = set()
    for p in inventory["projects"]:
        missing = REQUIRED - p.keys()
        if missing:
            sys.exit(f"{p.get('id', '?')}: missing {sorted(missing)}")
        for field, allowed in ALLOWED.items():
            if p[field] not in allowed:
                sys.exit(f"{p['id']}: {field} '{p[field]}' is not one of {sorted(allowed)}")
        if p["id"] in ids:
            sys.exit(f"duplicate id {p['id']}")
        ids.add(p["id"])
    return inventory


def render(inventory: dict) -> str:
    projects = inventory["projects"]
    lines = [
        "# Tech exposure",
        "",
        f"Generated from [inventory.json](inventory.json) ({len(projects)} projects, updated {inventory['updated']}) by "
        "`tools/exposure.py`. Do not edit by hand.",
        "",
        "**Projects** counts every project that used it; **production** counts those that are live or working;",
        "**last used** is the latest activity among them. Client and employer work appears under descriptive names only.",
        "",
        "| Ownership | Projects |",
        "| --- | --- |",
    ]
    aims = inventory.get("aims", {})
    if aims:
        lines[-2:-2] = [
            f"**Aiming for:** {' or '.join(aims.get('roles', []))}, working in {' and '.join(aims.get('technologies', []))}.",
            "",
        ]
        for tech in aims.get("technologies", []):
            ps = [p for p in projects if any(re.sub(r"\s+[\d./]+$", "", t) == tech for t in p.get("languages", []))]
            if ps:
                lines[-2:-2] = [
                    f"- **{tech}:** {len(ps)} projects, {sum(p['status'] in ('live', 'working') for p in ps)} reached production, "
                    f"last used {max(p['last_activity'] for p in ps)}",
                ]
        lines[-2:-2] = [""]
    by_owner = defaultdict(int)
    for p in projects:
        by_owner[p["ownership"]] += 1
    lines += [f"| {k} | {v} |" for k, v in sorted(by_owner.items(), key=lambda kv: -kv[1])]

    for key, title in GROUPS:
        uses = defaultdict(list)
        for p in projects:
            # "Laravel 13" and "Laravel 7/8" count as Laravel: the inventory keeps versions, the exposure does not.
            for tech in {re.sub(r"\s+[\d./]+$", "", t) for t in p.get(key, [])}:
                uses[tech].append(p)
        if not uses:
            continue
        lines += ["", f"## {title}", "", "| Technology | Projects | Production | Last used | Used in |", "| --- | ---: | ---: | --- | --- |"]
        ranked = sorted(uses.items(), key=lambda kv: (-len(kv[1]), -max(int(p["last_activity"].replace("-", "")) for p in kv[1]), kv[0].lower()))
        for tech, ps in ranked:
            production = sum(p["status"] in ("live", "working") for p in ps)
            last = max(p["last_activity"] for p in ps)
            names = ", ".join(p["name"] for p in sorted(ps, key=lambda p: p["last_activity"], reverse=True))
            lines.append(f"| {tech} | {len(ps)} | {production} | {last} | {names} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    output = render(load())
    target = ROOT / "EXPOSURE.md"
    if "--check" in sys.argv:
        if not target.exists() or target.read_text() != output:
            sys.exit("EXPOSURE.md is out of date: run python3 tools/exposure.py")
        return
    target.write_text(output)
    print(f"wrote {target.name}")


if __name__ == "__main__":
    main()
