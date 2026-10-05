#!/usr/bin/env python3
"""
Test script to verify GitHub Stats Generator setup
"""

import os
import sys
from pathlib import Path

def test_env_file():
    """Check if .env file exists and has required variables"""
    print("=" * 60)
    print("TEST 1: Checking .env file")
    print("=" * 60)

    env_path = Path('.env')
    if not env_path.exists():
        print("❌ FAIL: .env file not found")
        print("   Create it with:")
        print("   ACCESS_TOKEN=your_token_here")
        print("   USER_NAME=your_username")
        return False

    print("✓ .env file exists")

    # Read and check variables
    with open('.env') as f:
        lines = f.readlines()

    has_token = False
    has_user = False

    for line in lines:
        line = line.strip()
        if line.startswith('ACCESS_TOKEN='):
            has_token = True
            token_value = line.split('=', 1)[1]
            if token_value and token_value != 'your_token_here':
                print("✓ ACCESS_TOKEN is set")
            else:
                print("❌ ACCESS_TOKEN is empty or placeholder")
                return False

        if line.startswith('USER_NAME='):
            has_user = True
            user_value = line.split('=', 1)[1]
            if user_value and user_value != 'your_username':
                print(f"✓ USER_NAME is set to: {user_value}")
            else:
                print("❌ USER_NAME is empty or placeholder")
                return False

    if not has_token or not has_user:
        print("❌ FAIL: Missing required variables")
        return False

    print("✓ All required environment variables present\n")
    return True


def test_dependencies():
    """Check if required Python packages are installed"""
    print("=" * 60)
    print("TEST 2: Checking Python dependencies")
    print("=" * 60)

    required = {
        'requests': 'requests',
        'dateutil': 'python-dateutil',
        'lxml': 'lxml'
    }

    missing = []

    for package, pip_name in required.items():
        try:
            __import__(package)
            print(f"✓ {pip_name} is installed")
        except ImportError:
            print(f"❌ {pip_name} is NOT installed")
            missing.append(pip_name)

    if missing:
        print(f"\n❌ FAIL: Missing packages")
        print(f"   Install with: pip install {' '.join(missing)}")
        return False

    print("✓ All dependencies installed\n")
    return True


def test_files():
    """Check if required files exist"""
    print("=" * 60)
    print("TEST 3: Checking required files")
    print("=" * 60)

    required_files = [
        'today.py',
        'run.py',
        'dark_mode.svg',
        'light_mode.svg',
        'cache/requirements.txt',
        '.github/workflows/build.yaml'
    ]

    all_exist = True

    for filepath in required_files:
        if Path(filepath).exists():
            print(f"✓ {filepath}")
        else:
            print(f"❌ {filepath} NOT FOUND")
            all_exist = False

    if not all_exist:
        print("\n❌ FAIL: Missing required files")
        return False

    print("✓ All required files present\n")
    return True


def test_github_api():
    """Test GitHub API connection with the token"""
    print("=" * 60)
    print("TEST 4: Testing GitHub API connection")
    print("=" * 60)

    # Load .env
    try:
        with open('.env') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    except FileNotFoundError:
        print("❌ Cannot load .env file")
        return False

    try:
        import requests

        token = os.environ.get('ACCESS_TOKEN')
        username = os.environ.get('USER_NAME')

        if not token or not username:
            print("❌ ACCESS_TOKEN or USER_NAME not set")
            return False

        # Test simple GraphQL query
        headers = {'authorization': f'token {token}'}
        query = '''
        query($login: String!) {
            user(login: $login) {
                id
                login
                name
                createdAt
            }
        }'''

        response = requests.post(
            'https://api.github.com/graphql',
            json={'query': query, 'variables': {'login': username}},
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and data['data']['user']:
                user_data = data['data']['user']
                print(f"✓ Successfully connected to GitHub API")
                print(f"  User: {user_data['login']}")
                print(f"  Name: {user_data.get('name', 'N/A')}")
                print(f"  Account created: {user_data['createdAt'][:10]}")
                print("\n✓ Your token and username are correct!\n")
                return True
            elif 'errors' in data:
                print(f"❌ API Error: {data['errors'][0]['message']}")
                return False
        elif response.status_code == 401:
            print("❌ FAIL: Invalid ACCESS_TOKEN")
            print("   Your token is incorrect or expired")
            print("   Generate a new token at: https://github.com/settings/tokens")
            return False
        elif response.status_code == 404:
            print(f"❌ FAIL: User '{username}' not found")
            print("   Check your USER_NAME in .env")
            return False
        else:
            print(f"❌ FAIL: HTTP {response.status_code}")
            print(f"   {response.text}")
            return False

    except ImportError:
        print("❌ 'requests' library not installed")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_cache_directory():
    """Check cache directory"""
    print("=" * 60)
    print("TEST 5: Checking cache directory")
    print("=" * 60)

    cache_dir = Path('cache')
    if not cache_dir.exists():
        print("❌ cache/ directory not found")
        return False

    print("✓ cache/ directory exists")

    # Check for cache file
    import hashlib
    username = os.environ.get('USER_NAME', 'Anurag0577')
    cache_file = cache_dir / f"{hashlib.sha256(username.encode('utf-8')).hexdigest()}.txt"

    if cache_file.exists():
        print(f"✓ Cache file exists: {cache_file.name}")
        with open(cache_file) as f:
            lines = f.readlines()
        print(f"  Contains {len(lines)} lines (comment + repo data)")
    else:
        print("ℹ  Cache file will be created on first run")

    print()
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("GITHUB PROFILE STATS GENERATOR - SETUP TEST")
    print("=" * 60 + "\n")

    results = []

    # Run tests
    results.append(("Environment file", test_env_file()))
    results.append(("Dependencies", test_dependencies()))
    results.append(("Required files", test_files()))
    results.append(("Cache directory", test_cache_directory()))
    results.append(("GitHub API", test_github_api()))

    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    all_passed = True
    for test_name, passed in results:
        status = "✓ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("\nYou're ready to run the generator:")
        print("  python run.py")
        print("\nOr push to GitHub and let Actions run it automatically.")
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("Fix the issues above before running the generator.")
        sys.exit(1)


if __name__ == '__main__':
    main()
