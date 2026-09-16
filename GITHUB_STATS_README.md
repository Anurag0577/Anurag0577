# GitHub Profile Stats SVG Generator

This tool automatically generates an SVG displaying your GitHub statistics including repositories, stars, commits, followers, and lines of code.

## ✨ Features

- **Dynamic GitHub Stats**: Fetches real-time data from GitHub API
- **Automatic Cache**: Caches repository data for faster subsequent runs
- **Two Themes**: Dark and light mode SVG variants
- **Detailed Metrics**:
  - Repository count
  - Stars received
  - Total commits
  - Followers
  - Lines of code (additions/deletions)
  - Contributed repositories

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install requests python-dateutil lxml
```

### 2. Get GitHub Token

1. Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "Stats Generator")
4. Select scopes:
   - ✅ `public_repo`
   - ✅ `read:user`
   - ✅ `repo:status`
5. Click "Generate token" and **copy it immediately** (you won't see it again!)

### 3. Configure Environment

**Option A: Using .env file (Recommended)**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your credentials
# ACCESS_TOKEN=your_token_here
# USER_NAME=your_username_here
```

**Option B: Set directly in terminal**

Linux/Mac:
```bash
export ACCESS_TOKEN="your_github_token"
export USER_NAME="your_username"
```

Windows (PowerShell):
```powershell
$env:ACCESS_TOKEN="your_github_token"
$env:USER_NAME="your_username"
```

### 4. Run the Generator

**Easiest way (Python):**
```bash
python run.py
```

**Or directly:**
```bash
python today.py
```

**Or with bash script (Linux/Mac):**
```bash
bash run.sh
```

## 📊 What Gets Updated

The script fetches and updates:

| Metric | Description |
|--------|-------------|
| **Repos** | Total public repositories owned |
| **Stars** | Stars received on repositories |
| **Commits** | Total commits in repositories |
| **Followers** | GitHub followers count |
| **LOC** | Lines of code (additions/deletions) |
| **Contributed** | Repositories you've collaborated on |

## 📁 File Structure

```
├── today.py                # Main stats generator script
├── run.py                  # Python runner (auto-loads .env)
├── run.sh                  # Bash runner (for Linux/Mac)
├── dark_mode.svg           # Generated dark theme SVG
├── light_mode.svg          # Generated light theme SVG
├── .env.example            # Example environment config
├── cache/                  # Caching directory
│   └── [username_hash].txt # Cache file (created on first run)
└── README.md              # This file
```

## 🔧 How It Works

1. **Fetches Data**: Uses GitHub GraphQL API to get your stats
2. **Caches Results**: Stores data locally to avoid hitting API rate limits
3. **Updates SVG**: Modifies `dark_mode.svg` and `light_mode.svg` with new data
4. **Automatic Refresh**: Detects when repos change and updates accordingly

## ⚙️ Performance

- **First run**: ~10-30 seconds (processes all repositories)
- **Cached runs**: ~2-5 seconds (uses cached data)
- **Cache invalidation**: Automatic when repository count changes

## 🔐 Security Notes

- Never commit your `.env` file to Git
- Add `.env` to `.gitignore`:
  ```
  .env
  ```
- Token is only used to query GitHub API
- No data is sent anywhere else
- You can revoke the token anytime in GitHub settings

## ❓ Troubleshooting

### "ACCESS_TOKEN and USER_NAME must be set"
- Ensure your `.env` file is in the project root
- Check that `ACCESS_TOKEN` and `USER_NAME` lines are properly formatted
- No spaces around `=` sign

### "Too many requests" error
- You've hit GitHub API rate limits
- Wait a few minutes before running again
- Consider adjusting `QUERY_COUNT` settings

### SVG not updating
- Run `python run.py` for detailed error messages
- Check that token has required scopes
- Ensure token is still valid (hasn't expired)

### "No such file or directory"
- Run the script from the project root directory
- Check that `dark_mode.svg` and `light_mode.svg` exist

## 📝 Customization

### Cache Comment Block
The script reserves the first 7 lines of the cache file for comments. Edit them:

```python
# In today.py, look for cache_builder calls:
total_loc, loc_time = perf_counter(loc_query, ['OWNER', 'COLLABORATOR', 'ORGANIZATION_MEMBER'], 7)
#                                                                                                ^ comment lines
```

### Modify SVG layout
Edit `dark_mode.svg` and `light_mode.svg` directly, but keep the tspan elements with these IDs for auto-updates:
- `repo_data`, `repo_data_dots`
- `star_data`, `star_data_dots`
- `commit_data`, `commit_data_dots`
- `follower_data`, `follower_data_dots`
- `contrib_data`
- `loc_data`, `loc_data_dots`
- `loc_add`
- `loc_del`, `loc_del_dots`

## 📚 API Details

Uses GitHub GraphQL API v4 with queries for:
- User profile info (ID, creation date)
- Repository stats (count, stars, commits)
- Contribution history
- Follower count
- Lines of code per repository

All queries are optimized and rate-limited.

## 📄 License

This project inherits the license from its original repository.

## 🤝 Contributing

Feel free to fork and modify for your own use!

---

**Last Updated**: 2024
**Author**: Original by Andrew6rant, modified for dynamic GitHub integration
