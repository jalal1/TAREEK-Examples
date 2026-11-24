# Contributing an example

You can share a completed [TAREEK](https://github.com/jalal1/TAREEK) run here.

1. **Fork this repository** and make a folder named `<region>-<author>-<YYYYMMDD>/` at
   the top level (for example `seattle-jdoe-20260623/`). Examples from the TAREEK
   maintainers do not include the author: `<region>-<YYYYMMDD>/`.

2. **Add a `README.md`** that tells what you ran, the region, your configuration and
   your results (figures and numbers are welcome). Use the existing examples as a guide:
   open one and follow the same structure. The first line must be a title such as
   `# My Region, ST experiment — 2026-11-17`.

3. **Make the experiment report in TAREEK.** In your TAREEK folder, run:

   ```bash
   python scripts/experiment_report.py experiments/<experiment-id> --no-pdf --link-images
   ```

   With `--link-images`, `report.html` links to the figures in `evaluation/` and does
   not embed them. Thus each image is stored only once. Copy `report.html` and all the
   images that it links to into your example folder (all of `evaluation/*.png` and the
   per-hour `count_error_hXX`, `counts_loglog_hXX` and `heatmap_hXX` figures). Open the
   copied `report.html` in a browser and make sure that it shows all the images.

4. **Add `config_used.json`, `config.xml`** and small result files (CSV, JSON, figures).
   Keep the folder small (less than 50 MB). Add the recipe and the results. Do not add
   large inputs or inputs that TAREEK can make again (OSM extracts, full MATSim networks
   or plans).

   > ⚠️ **Remove your secrets first.** `config_used.json` can contain real API keys
   > (for example `data.census_api_key`, or a key under `gtfs.api_keys`). Replace each key
   > with a placeholder such as `YOUR_CENSUS_API_KEY_HERE` before you commit. In your
   > README, list the services that a user needs a key for. Never commit a live key.

5. **Give the data sources.** In your README, give the source and the license of each
   input dataset (for example, OpenStreetMap data is ODbL). Make sure that you have the
   right to share the data.

6. **Add a row** to the table in [README.md](README.md).

7. **Open a pull request** against `main`. We will examine it and merge it.

## Show your example in the TAREEK web app

The TAREEK web app shows each example as a preset on its map. It reads only `README.md`,
`config_used.json` and `config.xml`. To add your example to the web app, also open a pull
request in [TAREEK](https://github.com/jalal1/TAREEK) that adds
`examples/<your-folder>/` with only these three files. Add this line at the top of that
README, before the title:

```markdown
> Full results: [TAREEK-examples/<your-folder>](https://github.com/jalal1/TAREEK-examples/tree/main/<your-folder>)
```

## License of your contribution

When you open a pull request, you agree that your example is available under the
[CC BY 4.0 license](LICENSE), as the other content of this repository. Third-party content
in your example keeps its own license; tell us about it in your README.
