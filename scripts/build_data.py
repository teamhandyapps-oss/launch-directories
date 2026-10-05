"""Builds directories.json and directories.csv from the rows below. MIT licensed."""
import csv, json

FIELDS = ["name", "url", "submit_url", "free_or_paid", "requires_account", "link_type", "review_time",
          "dr", "dr_source", "ai_agent_friendly", "submit_steps", "notes", "last_verified"]
V = "2026-10-05"

ROWS = [
    {"name": "Neeed Directory", "url": "https://neeed.directory", "submit_url": "https://neeed.directory/submit",
     "free_or_paid": "free_with_paid_options", "requires_account": "yes", "link_type": "dofollow",
     "review_time": "Live right away after an automatic check",
     "submit_steps": ["Pick a listing type", "Sign in", "Fill in the form", "Automatic check runs", "Listing goes live right away"],
     "notes": "Software and digital products only. Free plan plus one-time paid options. Link type is the site's own statement.",
     "last_verified": V},
    {"name": "Startup Fame", "url": "https://startupfa.me", "free_or_paid": "free_with_paid_options",
     "link_type": "dofollow", "review_time": "Several business days",
     "notes": "Submit URL not found (/submit returns 404). Free listing requires a badge on your site. Paid: Highlight $19/month, Spotlight $149/month. Link type is the site's own statement.",
     "last_verified": V},
    {"name": "TinyLaunch", "url": "https://tinylaunch.com", "submit_url": "https://tinylaunch.com/submit",
     "free_or_paid": "free_with_paid_options", "requires_account": "yes", "link_type": "dofollow_with_badge",
     "submit_steps": ["Sign in with email, Google, GitHub or X", "Submit the launch form", "Embed the TinyLaunch badge on your site to get a dofollow link"],
     "notes": "Free launch gets a dofollow link when the badge is embedded. Premium and done-for-you options are paid.",
     "last_verified": V},
    {"name": "Dev Hunt", "url": "https://devhunt.org", "free_or_paid": "free_with_paid_options",
     "notes": "Submit URL not found. Launches are shown as Free. Ads cost $89/week.", "last_verified": V},
    {"name": "Findly", "url": "https://findly.tools", "submit_url": "https://findly.tools/submit",
     "free_or_paid": "free_with_paid_options", "requires_account": "yes", "link_type": "dofollow",
     "dr": "81", "dr_source": "Ahrefs, noted by Team Handyapps 2026-10-02",
     "submit_steps": ["Sign in with email, GitHub or Google", "Submit the product on /submit"],
     "notes": "Free listing. Paid done-for-you option.", "last_verified": V},
    {"name": "ToolFame", "url": "https://toolfame.com", "submit_url": "https://toolfame.com/submit",
     "requires_account": "yes", "submit_steps": ["Sign in with email, Google or GitHub", "Submit the product on /submit"],
     "notes": "Link type, pricing and review time not stated on the site.", "last_verified": V},
    {"name": "Nick Launches", "url": "https://nicklaunches.com", "submit_url": "https://nicklaunches.com/submit",
     "ai_agent_friendly": "yes",
     "submit_steps": ["Open the submit form", "Add a logo and screenshots", "Pick a plan and a launch week", "Save as a draft if needed"],
     "notes": "Has an MCP server: claude mcp add --transport http nicklaunches https://nicklaunches.com/api/mcp/ (no key; approve in the browser; the agent drafts, a human finishes). Prices not read.",
     "last_verified": V},
    {"name": "Fazier", "url": "https://fazier.com", "submit_url": "https://fazier.com/submit",
     "free_or_paid": "free_with_paid_options", "review_time": "Within 30 days (Basic plan)",
     "notes": "Basic plan is free. Paid tiers $29 and $49. A high-authority dofollow link is a paid perk.",
     "last_verified": V},
    {"name": "BetaList", "url": "https://betalist.com", "submit_url": "https://betalist.com/submit",
     "requires_account": "yes", "submit_steps": ["Sign in with X or a magic link", "Submit the startup on /submit"],
     "notes": "Free or paid and link type not stated on the page read.", "last_verified": V},
]

def full(row):
    out = {k: row.get(k, "") for k in FIELDS}
    out["submit_steps"] = row.get("submit_steps", [])
    return out

def main():
    data = [full(r) for r in ROWS]
    with open("directories.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open("directories.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(FIELDS)
        for r in data:
            w.writerow([" > ".join(r[k]) if k == "submit_steps" else r[k] for k in FIELDS])

if __name__ == "__main__":
    main()
