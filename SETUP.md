# GitHub Stats SVG Setup Guide

This project automatically generates a dynamic SVG with your GitHub statistics.

## Prerequisites

1. **Python 3.x** with required packages installed:
   ```bash
   pip install requests python-dateutil lxml
   ```

2. **GitHub Personal Access Token**
   - Go to: GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token"
   - Select scopes:
     - `read:user`
     - `public_repo`
     - `repo:status`
   - Copy the token (you'll only see it once!)

## Setup

### 1. Create `.env` file (recommended)
Create a `.env` file in the project root:
```bash
ACCESS_TOKEN=your_github_token_here
USER_NAME=your_github_username
```

### 2. OR Set Environment Variables

**Linux/Mac:**
```bash
export ACCESS_TOKEN="your_github_token"
export USER_NAME="your_github_username"
```

**Windows (PowerShell):**
```powershell
$env:ACCESS_TOKEN="your_github_token"
$env:USER_NAME="your_github_username"
```

## Usage

Run the script to generate/update the SVG files:
```bash
python today.py
```

This will:
- Fetch your GitHub stats (repos, stars, commits, followers, lines of code)
- Update `dark_mode.svg`
- Update `light_mode.svg`

## What Gets Updated

The script fetches and updates:
- Repository count
- Stars received
- Total commits
- Followers
- Lines of code (added/deleted)
- Contributed repositories

## Important Notes

- The script runs GraphQL API queries to fetch data
- Results are cached in the `cache/` directory for performance
- First run may take a few seconds as it processes all repositories
- Subsequent runs use cached data (much faster)
- Token should be kept secret - don't commit `.env` file to git!
