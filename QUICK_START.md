# ⚡ Quick Start - GitHub Stats Fix

## 3-Minute Setup

### 1️⃣ Install packages (30 seconds)
```bash
pip install requests python-dateutil lxml
```

### 2️⃣ Get GitHub token (1 minute)
- Go to: https://github.com/settings/tokens
- Click "Generate new token (classic)"
- Select: `repo`, `read:user`, `repo:status`
- Generate and copy the token

### 3️⃣ Create .env file (30 seconds)
Create a file called `.env` in this folder with:
```
ACCESS_TOKEN=paste_your_token_here
USER_NAME=Anurag0577
```

### 4️⃣ Run the script (30 seconds)
```bash
python run.py
```

## ✅ Done!

Your SVG files now have **real GitHub stats** instead of hardcoded values!

---

## Files to Check

- ✓ `dark_mode.svg` - Updated with real stats
- ✓ `light_mode.svg` - Updated with real stats
- ✓ `cache/` folder - Contains cache for faster runs

## Next Time

Just run:
```bash
python run.py
```

It's much faster on subsequent runs! 🚀

---

## Need Help?

See `FIX_HARDCODED_STATS.md` for detailed instructions
