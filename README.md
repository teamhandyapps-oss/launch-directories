# launch-directories

An open dataset of directories and listing sites where indie products can be submitted. Each row records what the site itself says: where to submit, whether it is free, whether an account is needed, link type, review time, and the steps to follow. Anything not verified is left blank. No row has a guessed value.

Maintained by [Team Handyapps](https://teamhandyapps.github.io/). Also available as a page, JSON API and MCP tool at [postlaunchkit.com/launch-directories/](https://postlaunchkit.com/launch-directories/).

## Files

- `directories.json` - the data, an array of objects (see `schema.json`)
- `directories.csv` - the same data, with `submit_steps` joined by ` > `
- `schema.json` - JSON Schema for one row
- `scripts/build_data.py` - rebuilds the JSON and CSV from one source list
- `CHANGELOG.md`

## Columns

`name, url, submit_url, free_or_paid, requires_account, link_type, review_time, dr, dr_source, ai_agent_friendly, submit_steps, notes, last_verified`

- `free_or_paid`: `free`, `free_with_paid_options` or `paid`
- `link_type`: as stated by the site: `dofollow`, `nofollow` or `dofollow_with_badge`
- `dr`: only when a dated source is named in `dr_source`
- `ai_agent_friendly`: `yes` only when the site documents an agent route such as an MCP server
- `last_verified`: date the row was checked against the site's own pages

Sites change. Check the site before you rely on a row, and open an issue if one is out of date.

## Use it

```
curl https://postlaunchkit.com/api/v1/launch-directories?free=1&link_type=dofollow
```

Before you submit a product, run the free [launch check](https://postlaunchkit.com/audit/) on your site.

## Licence

Code is MIT (`LICENSE`). Data is CC BY 4.0 (`LICENSE-DATA`). Credit: "Team Handyapps, launch-directories".
