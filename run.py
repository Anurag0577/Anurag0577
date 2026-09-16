#!/usr/bin/env python3
"""
GitHub Stats SVG Generator - Environment runner
Loads environment variables from .env and runs the stats generator
"""

import os
import sys
import subprocess
from pathlib import Path

def load_env_file(env_file='.env'):
    """Load environment variables from .env file"""
    if not Path(env_file).exists():
        print("Error: .env file not found")
        print("\nPlease create a .env file with:")
        print("  ACCESS_TOKEN=your_github_token")
        print("  USER_NAME=your_github_username")
        return False
    
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    
    return True

def check_requirements():
    """Check if all required environment variables are set"""
    required = ['ACCESS_TOKEN', 'USER_NAME']
    missing = [var for var in required if not os.environ.get(var)]
    
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        return False
    return True

def check_dependencies():
    """Check if required Python packages are installed"""
    required_packages = ['requests', 'dateutil', 'lxml']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"Error: Missing required packages: {', '.join(missing)}")
        print(f"\nInstall them with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    return True

def main():
    print("GitHub Stats Generator")
    print("=" * 50)
    
    # Load environment variables
    print("\n1. Loading environment variables...")
    if not load_env_file():
        sys.exit(1)
    print("   ✓ Environment variables loaded")
    
    # Check requirements
    print("\n2. Checking requirements...")
    if not check_requirements():
        sys.exit(1)
    print("   ✓ All required variables set")
    
    print(f"   ✓ Username: {os.environ.get('USER_NAME')}")
    
    # Check dependencies
    print("\n3. Checking Python dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("   ✓ All dependencies installed")
    
    # Run the main script
    print("\n4. Running stats generator...")
    print("-" * 50)
    try:
        subprocess.run([sys.executable, 'today.py'], check=True)
        print("-" * 50)
        print("\n✓ GitHub stats updated successfully!")
        print("  Check dark_mode.svg and light_mode.svg")
    except subprocess.CalledProcessError as e:
        print(f"\nError running script: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
