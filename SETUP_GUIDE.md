# GitHub Profile Stats Generator — Step-by-Step Setup Guide

This guide walks anyone through setting up their own automated GitHub profile stats generator, similar to the one running on this profile.

---

## 🔒 Security Notice First
> **NEVER share your personal access token with anyone, and NEVER commit your `.env` file to Git.**  
> Keep your token in **GitHub Secrets** only.

---

## 📌 Prerequisites
1. A GitHub account
2. Basic knowledge of Git and terminal commands
3. Python 3.11 or higher (for optional local testing)

---

## 🚀 Step-by-Step Setup Instructions

### Step 1: Create Your Profile Repository
1. Go to [github.com/new](https://github.com/new).
2. Set the **Repository name** to your **exact GitHub username** (e.g., if your username is `octocat`, name the repository `octocat`).
3. Set visibility to **Public**.
4. Check **Add a README file**.
5. Click **Create repository**.

---

### Step 2: Copy the Source Files
You can clone or copy the project files into your newly created profile repository:
- `today.py` (the Python calculation script)
- `.github/workflows/build.yaml` (the automated daily build workflow)
- `cache/` (directory containing requirements and cache setup)
- `dark_mode.svg` and `light_mode.svg` (the SVG display templates)

---

### Step 3: Generate a Personal Access Token
1. Go to [GitHub Settings → Personal access tokens (fine-grained)](https://github.com/settings/tokens?type=beta).
2. Click **Generate new token**.
3. **Token name**: `github-stats-generator`
4. **Expiration**: 90 days (or custom duration).
5. **Repository access**: Select **All repositories** (required to count your total contributions and stars).
6. **Permissions needed**:
   - **Account permissions**:
     - `Followers`: **Read-only**
     - `Starring`: **Read-only**
   - **Repository permissions**:
     - `Commit statuses`: **Read-only**
     - `Contents`: **Read-only**
     - `Metadata`: **Read-only**
7. Click **Generate token** and copy the generated token immediately.

---

### Step 4: Add the Token to GitHub Secrets
1. Go to your repository on GitHub (`https://github.com/<YOUR_USERNAME>/<YOUR_USERNAME>`).
2. Navigate to **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. **Name**: `ACCESS_TOKEN` *(must match this exact spelling)*
5. **Secret**: Paste your token generated in Step 3.
6. Click **Add secret**.

---

### Step 5: Enable GitHub Actions Workflow Permissions
1. In your repository on GitHub, go to **Settings** → **Actions** → **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Check **Allow GitHub Actions to create and approve pull requests**.
5. Click **Save**.

---

### Step 6: Customize Configuration
In your cloned repository, update the following:

1. **`.github/workflows/build.yaml`**:
   Change `USER_NAME` to your GitHub username:
   ```yaml
   env:
     ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
     USER_NAME: YOUR_GITHUB_USERNAME
   ```

2. **`today.py`** (Optional):
   Update the birth date on line 451 if you want the age counter to reflect your details:
   ```python
   age_data, age_time = perf_counter(daily_readme, datetime.datetime(YYYY, M, D))
   ```

3. **`dark_mode.svg` and `light_mode.svg`**:
   Open these SVG files in a text editor to update your social links, website, and name.

---

### Step 7: Push & Trigger Your First Run
1. Commit and push your changes to your `main` branch:
   ```bash
   git add .
   git commit -m "Configure GitHub profile stats"
   git push origin main
   ```
2. Go to the **Actions** tab on your GitHub repository.
3. Select **README build** from the left sidebar.
4. Click **Run workflow** → **Run workflow** (green button).
5. Once the build finishes with a green checkmark, your stats are updated!

---

### Step 8: Display on Your Profile
Add the following snippet to your root `README.md`:

```markdown
# Hi there 👋

![Profile Stats](dark_mode.svg#gh-dark-mode-only)
![Profile Stats](light_mode.svg#gh-light-mode-only)
```

---

## 🛡️ Security Best Practices Checklist
- [x] `.env` is listed inside `.gitignore` and NEVER committed.
- [x] Tokens are only stored in GitHub Repository Secrets (`ACCESS_TOKEN`).
- [x] Token has minimum required read-only permissions.
- [x] If a token is ever accidentally shared, revoke it immediately at [github.com/settings/tokens](https://github.com/settings/tokens).
