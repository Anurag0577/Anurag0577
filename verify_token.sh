#!/bin/bash
# Quick test script to verify your GitHub token works

echo "GitHub Token Verification Test"
echo "=============================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file for local testing..."
    echo "ACCESS_TOKEN=paste_your_token_here" > .env
    echo "USER_NAME=Anurag0577" >> .env
    echo ""
    echo "⚠️  Please edit .env and add your actual token:"
    echo "   nano .env"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Load .env
export $(cat .env | grep -v '^#' | xargs)

# Check if token is set
if [ -z "$ACCESS_TOKEN" ] || [ "$ACCESS_TOKEN" = "paste_your_token_here" ]; then
    echo "❌ ACCESS_TOKEN not set in .env"
    echo "   Edit .env and add your token, then run this again."
    exit 1
fi

echo "Testing GitHub API connection..."
echo ""

# Test the token
response=$(curl -s -H "Authorization: token $ACCESS_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user)

# Check if successful
if echo "$response" | grep -q "login"; then
    username=$(echo "$response" | grep -o '"login": *"[^"]*"' | head -1 | sed 's/"login": *"\([^"]*\)"/\1/')
    name=$(echo "$response" | grep -o '"name": *"[^"]*"' | head -1 | sed 's/"name": *"\([^"]*\)"/\1/')

    echo "✅ Token is VALID!"
    echo ""
    echo "   Authenticated as: $username"
    echo "   Name: $name"
    echo ""
    echo "🎉 Your token works! You can now:"
    echo "   1. Add it as ACCESS_TOKEN secret on GitHub"
    echo "   2. Or run: python run.py (to test locally)"
else
    echo "❌ Token is INVALID or EXPIRED"
    echo ""
    echo "Error response:"
    echo "$response" | head -5
    echo ""
    echo "Please generate a new token at:"
    echo "https://github.com/settings/tokens?type=beta"
fi
