# How to Fix Hardcoded GitHub Stats in SVG

## The Issue

Your `dark_mode.svg` has **hardcoded values** instead of fetching real data from GitHub:
- Repository count: 95 (hardcoded)
- Stars: 342 (hardcoded)
- Commits: 2,116 (hardcoded)
- Followers: 196 (hardcoded)
- Lines of code: 446,276 (hardcoded)

## The Solution

The `today.py` script is already set up to **fetch real data dynamically** from GitHub API. You just need to run it!

## Step-by-Step Fix

### Step 1: Install Dependencies
```bash
pip install requests python-dateutil lxml
```

### Step 2: Get Your GitHub Token
1. Visit: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name
4. Select these scopes:
   - ✅ repo (public_repo is enough)
   - ✅ read:user
5. Generate and copy the token

### Step 3: Set Up .env File
Create a file named `.env` in the project root:
```
ACCESS_TOKEN=your_token_here
USER_NAME=Anurag0577
```

### Step 4: Run the Generator
```bash
python run.py
```

Or directly:
```bash
python today.py
```

## What Happens

The script will:
1. Connect to GitHub API with your token
2. Fetch your real stats (repos, stars, commits, followers, LOC)
3. Update `dark_mode.svg` with actual data
4. Update `light_mode.svg` with actual data
5. Cache results locally for faster future runs

## Result

Your SVG will now display **real GitHub stats** that update automatically!

Example of updated stats:
```
✓ Repos: 95
✓ Stars: 342
✓ Commits: 2,116
✓ Followers: 196
✓ LOC: 446,276
```

## Automate It

Once working, you can:
- Run it manually whenever needed
- Add to a cron job (Linux/Mac) to update daily
- Set up GitHub Actions to run automatically

## Files Added/Created

- `run.py` - Easy Python runner with environment checks
- `run.sh` - Bash script for Linux/Mac
- `.env.example` - Template for your config
- `SETUP.md` - Detailed setup guide
- `GITHUB_STATS_README.md` - Complete documentation

## Already Done ✓

- `today.py` IS properly configured to fetch from GitHub
- `dark_mode.svg` and `light_mode.svg` have the right element IDs
- Cache mechanism is in place

## Troubleshooting

**Q: "Too many requests" error?**
A: Wait a few minutes, GitHub API has rate limits

**Q: Token rejected?**
A: Make sure token has the right scopes and hasn't expired

**Q: Can't find .env file?**
A: Run script from the project root directory

**Q: SVG not updating?**
A: Check Python script output for error messages

---

**TL;DR**: 
1. Create `.env` with your GitHub token and username
2. Run `python run.py`
3. Done! Your SVG now shows real GitHub stats
