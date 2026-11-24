# TAREEK examples

This repository contains the results of complete [TAREEK](https://github.com/jalal1/TAREEK)
runs for real regions. Each folder has the configuration of one run, the full
experiment report, the evaluation figures and data, and a `README.md` that explains the
run and its results.

TAREEK is the program that makes the runs. This repository has no program code. To make
your own run, install TAREEK. Its web app and its smoke tests use only a small copy of each
example (`README.md`, `config_used.json` and `config.xml`), which stays in TAREEK's
[`examples/`](https://github.com/jalal1/TAREEK/tree/main/examples) folder.

## Examples

"sim/obs" is the total simulated count divided by the total observed count at the count
stations (1.0 is a perfect total).

| Region | Date | Main result |
|--------|------|-------------|
| [Los Angeles, CA](losangeles-20261006/) | 2026-10-06 | 2 counties (Los Angeles, Orange), 10% sample, 1.70 million agents. sim/obs 0.935, CV 0.491, 35 count stations. Edge stations are too low. ([report](https://jalal1.github.io/TAREEK-examples/losangeles-20261006/report.html)) |
| [New York, NY-NJ](newyork-20261006/) | 2026-10-06 | 10 counties, 10% sample, 1.65 million agents. sim/obs 0.827, CV 0.807, 46 count stations. Congested (15% stuck); PATH is missing. ([report](https://jalal1.github.io/TAREEK-examples/newyork-20261006/report.html)) |
| [Chicago, IL](chicago-20261003/) | 2026-10-03 | 3 counties (Cook, DuPage, Lake), 20% sample, 1.79 million agents. sim/obs 0.887, CV 0.549, 42 count stations. The afternoon peak is low. ([report](https://jalal1.github.io/TAREEK-examples/chicago-20261003/report.html)) |
| [Birmingham, AL, local survey](birmingham-localsurvey-20261001/) | 2026-10-01 | First run with the Birmingham local survey (451 people). sim/obs 0.965, 58 count stations. More tuning is necessary. ([report](https://jalal1.github.io/TAREEK-examples/birmingham-localsurvey-20261001/report.html)) |
| [Twin Cities, MN-WI, TBI 2023 survey](twincities-tbi-20260930/) | 2026-09-30 | 15 counties, 15% sample, the TBI 2023 local survey in place of NHTS. sim/obs 0.925, CV 0.277, 96 count stations. ([report](https://jalal1.github.io/TAREEK-examples/twincities-tbi-20260930/report.html)) |
| [Twin Cities, MN-WI](twincities-20260928/) | 2026-09-28 | 15 counties, 15% sample, NHTS 2022. sim/obs 0.868, CV 0.276, 94 count stations. ([report](https://jalal1.github.io/TAREEK-examples/twincities-20260928/report.html)) |
| [Birmingham, AL](birmingham-20260928/) | 2026-09-28 | 2 counties (Jefferson, Shelby), 25% sample, NHTS 2022. sim/obs 0.912, CV 0.717, 53 count stations. ([report](https://jalal1.github.io/TAREEK-examples/birmingham-20260928/report.html)) |
| [Madison, WI](madison-20260928/) | 2026-09-28 | Dane County, 25% sample, NHTS 2022. sim/obs 0.813, CV 0.148, only 10 count stations. ([report](https://jalal1.github.io/TAREEK-examples/madison-20260928/report.html)) |

All runs use 10 MATSim iterations, the Hermes mobsim, person-first demand and freight.
The README of each example gives the settings and the full results.

## How to open a report

Click **report** in the table above. The reports are on GitHub Pages
(`https://jalal1.github.io/TAREEK-examples/<example>/report.html`).

To open a report offline, clone this repository:

```bash
git clone --depth 1 https://github.com/jalal1/TAREEK-examples.git
```

Or, on the GitHub page, click **Code → Download ZIP** and extract it. Then open
`<example>/report.html` in a web browser. The report loads its images from the `evaluation/`
folder next to it. If you copy a report to a different location, copy its `evaluation/` folder
with it. If you download only `report.html`, the report shows no images.

## Folder contents

Each example folder has these items:

| Item | Contents |
|------|----------|
| `README.md` | The run, its settings and its results |
| `report.html` | The full experiment report (verdict, demand check, count validation, freight, figures) |
| `config_used.json` | The TAREEK configuration of the run (API keys are replaced with placeholders) |
| `config.xml` | The MATSim configuration of the run |
| `evaluation/` | Evaluation figures and data, including the per-hour figures of the report |
| `graphs/` | MATSim count comparison pages |
| `matsim_output/` | Small MATSim output files (count comparison, statistics) |
| `counts.xml`, `matched_devices.csv` | The count stations and their match to the road network |
| `experiment_summary.json`, `demand_budget.json`, `freight_summary.json`, `od_matrix_diagnostics.json` | Summary numbers of the run |
| `experiment_*.log` | The log of the run |

## Add your example

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

The results in this repository are available under the
[Creative Commons Attribution 4.0 International license (CC BY 4.0)](LICENSE).
When you use them, give credit to "TAREEK examples, https://github.com/jalal1/TAREEK-examples".

Some content comes from other sources and has its own license. For example, the road
networks come from OpenStreetMap (© OpenStreetMap contributors, ODbL). See
[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).

The TAREEK program has a different license (GPL-3.0-or-later). See the
[TAREEK repository](https://github.com/jalal1/TAREEK).
