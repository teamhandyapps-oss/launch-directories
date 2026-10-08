# Changelog

## 2026-10-08

- Startup Fame: link_type changed from dofollow to dofollow_with_badge and requires_account set to yes. The site's FAQ (https://startupfa.me/) says the free listing needs a homepage badge and a review; a no-badge listing is paid. Rows with link_type=dofollow (no badge) are now 3.
- Synced the 2026-10-07 snapshot from the PostLaunchKit dataset: 26 directories (was 9). directories.json, directories.csv and scripts/build_data.py are regenerated together and match.
- Values still come from each site's own pages. Unknown values are blank. Rows are checked on 2026-10-05 or 2026-10-07 (see last_verified).

## 2026-10-05

- First release with 9 directories: Neeed Directory, Startup Fame, TinyLaunch, Dev Hunt, Findly, ToolFame, Nick Launches, Fazier, BetaList.
- Values come from each site's own pages, checked 2026-10-05. Unknown values are blank.
