# POIZON L10n Skill

A Claude Code skill for Chinese to American English localization following POIZON brand guidelines.

## Features

- **Style guide** - Brand voice, tone, grammar, and formatting rules
- **Glossary** - 4,000+ approved term translations from Crowdin
- **Auto-sync** - GitHub Actions refreshes glossary daily

## Quick Start

### For Team Members

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_ORG/skill_L10n.git
   ```

2. Create a symlink to your Claude skills folder:
   ```bash
   ln -s /path/to/skill_L10n ~/.claude/skills/poizon-l10n
   ```

3. Use in Claude Code:
   ```
   /poizon-l10n
   取消订单
   ```

### For Admins (Setting Up Auto-Sync)

1. Add your Crowdin API token as a GitHub secret:
   - Go to repo Settings → Secrets → Actions
   - Add `CROWDIN_API_TOKEN` with your token

2. The glossary will auto-update daily at 2 AM UTC

## Manual Glossary Refresh

```bash
# Set up config (first time only)
cp scripts/config.example.json scripts/config.json
# Edit scripts/config.json with your API token

# Refresh glossary
python3 scripts/glossary_client.py cache-multi 4,6,25
```

## Files

```
skill_L10n/
├── SKILL.md              # Claude Code skill definition
├── glossary_cache.md     # Cached glossary (4,000+ terms)
├── poizon-en-localization.md  # Full style guide
├── scripts/
│   ├── glossary_client.py    # Crowdin API client
│   └── config.example.json   # Config template
└── .github/
    └── workflows/
        └── sync-glossary.yml # Auto-sync workflow
```

## Glossary Sources

| ID | Name | Terms |
|----|------|-------|
| 4 | POIZON - User Facing (Legacy) | ~4,000 |
| 6 | POIZON - Internal Facing | ~300 |
| 25 | POIZON Product Terms | ~30 |

## CLI Commands

```bash
# List all glossaries
python3 scripts/glossary_client.py list

# View terms in a glossary
python3 scripts/glossary_client.py terms 4

# Search for a term
python3 scripts/glossary_client.py search 4 "出价"

# Export to CSV
python3 scripts/glossary_client.py csv 4 output.csv

# Cache single glossary
python3 scripts/glossary_client.py cache 4

# Cache multiple glossaries
python3 scripts/glossary_client.py cache-multi 4,6,25
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CROWDIN_API_TOKEN` | Crowdin API token |
| `CROWDIN_BASE_URL` | API base URL (default: poizonglobal.crowdin.com) |

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
