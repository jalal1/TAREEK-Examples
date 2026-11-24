# SPDX-License-Identifier: CC-BY-4.0
"""Build the GitHub Pages site: a map of the examples, plus the example folders.

    python site/build.py _site

Every top-level folder with a config_used.json is an example. Nothing here
lists the examples by hand: a new folder gets its pin on the next build. The
metadata comes from the example itself, by the same rules as the TAREEK web
app (webapp/backend/preset_service.py):

- region: the README title before " experiment" or " — "; examples with the
  same region share one pin.
- pin: the population-weighted mean of the county centroids in
  site/county_points.csv (region.counties of config_used.json).
- results: experiment_summary.json (evaluation section).

Uses only the Python standard library.
"""
import csv
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent
PAGES = "https://jalal1.github.io/TAREEK-examples"
GITHUB = "https://github.com/jalal1/TAREEK-examples"

SURVEY_LABELS = {"nhts": "NHTS", "tbi": "TBI", "bham_local": "Local survey"}


def warn(message):
    # GitHub Actions shows ::warning:: lines as annotations on the run.
    print(f"::warning::{message}", file=sys.stderr)


def load_county_points():
    with open(SITE / "county_points.csv", encoding="utf-8") as f:
        return {r["geoid"]: (float(r["lat"]), float(r["lng"]), int(r["population"]))
                for r in csv.DictReader(f)}


def locate(counties, points):
    """Population-weighted mean of the county centroids, or None."""
    found = [points[c] for c in counties if c in points]
    if not found:
        return None
    total = sum(p[2] for p in found)
    weights = [p[2] / total for p in found] if total > 0 else [1 / len(found)] * len(found)
    return (round(sum(w * p[0] for w, p in zip(weights, found)), 4),
            round(sum(w * p[1] for w, p in zip(weights, found)), 4))


def readme_parts(folder):
    """(title, first paragraph after the title) of the example README."""
    try:
        lines = (folder / "README.md").read_text(encoding="utf-8").splitlines()
    except OSError:
        return None, ""
    title, paragraph = None, []
    for line in lines:
        if title is None:
            if line.startswith("# "):
                title = line[2:].strip()
            continue
        if line.strip():
            if line.startswith(("#", "|", "```", "- ", "* ")):
                break
            paragraph.append(line.strip().lstrip("> ").replace("**", "").replace("`", ""))
        elif paragraph:
            break
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", " ".join(paragraph))  # drop link targets
    text = re.sub(r"(?<!\w)[*_]([^*_]+)[*_](?!\w)", r"\1", text)  # drop *italic* marks
    if len(text) > 320:
        text = text[:319].rsplit(" ", 1)[0] + "…"
    return title, text


def example(folder, points):
    config = json.loads((folder / "config_used.json").read_text(encoding="utf-8"))
    title, summary = readme_parts(folder)
    region = re.split(r" experiment\b| — ", title, maxsplit=1)[0].strip() if title else ""
    region = region or folder.name.split("-", 1)[0].title()
    match = re.search(r"(\d{4})(\d{2})(\d{2})$", folder.name)
    date = f"{match[1]}-{match[2]}-{match[3]}" if match else None

    surveys = [s for s in config.get("data", {}).get("surveys", []) if isinstance(s, dict)]
    main = next((s for s in surveys if (s.get("weight") or 0) > 0), surveys[0] if surveys else {})
    survey = SURVEY_LABELS.get(main.get("type"), str(main.get("type") or "survey"))
    if re.fullmatch(r"\d{4}", str(main.get("year") or "")):
        survey = f"{survey} {main['year']}"

    counties = config.get("region", {}).get("counties") or []
    location = locate(counties, points)
    if location is None:
        warn(f"{folder.name}: no known county in region.counties, so it has no map pin")

    results = {}
    try:
        evaluation = json.loads((folder / "experiment_summary.json").read_text(encoding="utf-8"))
        evaluation = evaluation.get("evaluation") or {}
        results = {"sim_obs": evaluation.get("aggregate_sim_obs_ratio"),
                   "cv": evaluation.get("station_ratio_cv"),
                   "stations": evaluation.get("num_stations_with_ratio")}
    except (OSError, ValueError):
        warn(f"{folder.name}: no readable experiment_summary.json, so the map shows no results")

    has_report = (folder / "report.html").is_file()
    if not has_report:
        warn(f"{folder.name}: no report.html")
    return {
        "id": folder.name,
        "region": region,
        "title": title or folder.name,
        "date": date,
        "survey": survey,
        "summary": summary,
        "counties": len(counties),
        "sample": config.get("plan_generation", {}).get("scaling_factor"),
        "freight": bool(config.get("freight", {}).get("enabled")),
        "results": results,
        "location": {"lat": location[0], "lng": location[1]} if location else None,
        "report": f"{folder.name}/report.html" if has_report else None,
        "readme": f"{GITHUB}/tree/main/{folder.name}",
    }


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python site/build.py <output folder>")
    out = Path(sys.argv[1]).resolve()
    if out == REPO or REPO in out.parents and out.parent != REPO:
        sys.exit("the output folder must be a new top-level folder such as _site")
    points = load_county_points()

    examples = []
    for config in sorted(REPO.glob("*/config_used.json")):
        folder = config.parent
        if folder.name.startswith(("_", ".")) or folder.resolve() == out:
            continue
        try:
            examples.append(example(folder, points))
        except (OSError, ValueError, AttributeError) as exc:
            warn(f"{folder.name}: skipped ({type(exc).__name__}: {exc})")
    if not examples:
        sys.exit("no examples found")
    examples.sort(key=lambda e: (e["date"] or "", e["id"]), reverse=True)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for e in examples:
        shutil.copytree(REPO / e["id"], out / e["id"])
    shutil.copy2(REPO / "LICENSE", out / "LICENSE")

    data = json.dumps({"examples": examples, "github": GITHUB}, ensure_ascii=False, indent=1)
    (out / "examples.json").write_text(data, encoding="utf-8")
    page = (SITE / "index.html").read_text(encoding="utf-8")
    embedded = data.replace("</", "<\\/")  # cannot close the <script> element early
    (out / "index.html").write_text(page.replace("/*EXAMPLES_JSON*/{}", embedded), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")

    pins = len({e["region"] for e in examples if e["location"]})
    print(f"{len(examples)} examples, {pins} map pins -> {out}")


if __name__ == "__main__":
    main()
