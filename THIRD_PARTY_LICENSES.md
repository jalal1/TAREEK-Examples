# Third-party software and data

The results in this repository are available under CC BY 4.0 (see [LICENSE](LICENSE)).
Some files, or parts of files, come from other sources. CC BY 4.0 does not apply to
these parts. Each part keeps its own license.

## Results that use OpenStreetMap data

The road networks in the TAREEK runs come from OpenStreetMap. The results in this
repository (for example `report.html`, the figures in `evaluation/`, `counts.xml`,
`matched_devices.csv` and the pages in `graphs/`) use these networks.

Map data © OpenStreetMap contributors, available under the
[Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/).
See https://www.openstreetmap.org/copyright.

If you publish results from this repository, give the same credit.

## Data used in the examples

The examples use these datasets. The TAREEK repository contains them, or TAREEK
downloads them when it runs.

| Data | Examples | Source | License |
|---|---|---|---|
| County boundaries and population | All | U.S. Census Bureau, cartographic boundary files 2022 and American Community Survey | U.S. Government work, public domain |
| Traffic counts | All | Federal Highway Administration (FHWA), Travel Monitoring Analysis System | U.S. Government work, public domain |
| National Household Travel Survey | All (`twincities-tbi-20260930/` loads it with weight 0) | FHWA, NHTS 2022 public-use files | U.S. Government work, public domain |
| Twin Cities Travel Behavior Inventory 2023 | `twincities-tbi-20260930/` | Metropolitan Council | Public domain. See the [TBI README](https://github.com/jalal1/TAREEK/blob/main/data/surveys/twincities_tbi_2023/README.md). |
| Custom count stations and volumes | Twin Cities examples | Minnesota Department of Transportation (MnDOT) traffic counts, Twin Cities | Public government data. No license is stated. |
| Birmingham local survey | `birmingham-localsurvey-20261001/` | Jalal Khalil | MIT License. See the [survey README](https://github.com/jalal1/TAREEK/blob/main/data/surveys/birmingham_al_local/README.md). |

## Software in this repository

### overLIB

| Item | Value |
|---|---|
| Files | `*/graphs/div/overlib.js` |
| Version | overLIB 4.21 |
| Copyright | Copyright Erik Bosrup 1998-2004. All rights reserved. |
| License | The overLIB license agreement, at http://www.bosrup.com/web/overlib/ |

MATSim writes this file into its count output, and we keep it unchanged in the
examples. CC BY 4.0 does not apply to it. Do not remove or change its copyright notice.

### MATSim output

MATSim (GPL-2.0-or-later, https://www.matsim.org/) made the files in `graphs/` and
`matsim_output/`. These files are the output of the program, not a part of it.
