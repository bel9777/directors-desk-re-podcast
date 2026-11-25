# Director's Desk: Institutional Real Estate

Daily two-host briefing on institutional, healthcare, and higher-education commercial real estate.

- **Feed URL:** `https://bel9777.github.io/directors-desk-re-podcast/feed.xml`
- **Schedule:** Daily 07:00 local time (Task Scheduler: `Directors Desk RE Podcast daily`)
- **Engine:** `podcast.py` (Gemini 3.8 Flash script + Gemini 3.8 Flash TTS, Alex=Sulafat / Morgan=Puck, normalized -16 LUFS, strict loudness/dip/silence gates)
- **Billing isolation:** Uses dedicated Gemini key `~\.ai-keys\gemini-applied-api-key.txt` (`key:dedicated`).
- **Privacy rule:** Public GitHub Pages feed. Every script must pass the `BLOCK` content guard before TTS and commit; never include employer names, colleagues, specific properties, vendors, or real figures.
- **Git identity:** `bel9777` / `283009259+bel9777@users.noreply.github.com` (enforced by `check_git_identity()`).
