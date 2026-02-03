#!/usr/bin/env bash
set -euo pipefail
# deploy_frontend.sh
# Deploys the `frontend/` folder to the `gh-pages` branch for GitHub Pages

FRONTEND_DIR="frontend"
BRANCH="gh-pages"
TMP_DIR=".gh-pages-worktree"

if [ ! -d "$FRONTEND_DIR" ]; then
  echo "Error: $FRONTEND_DIR not found"
  exit 1
fi

echo "Preparing to deploy $FRONTEND_DIR to branch $BRANCH"

# Ensure latest remote refs
git fetch origin

# Create or reset temporary worktree for the branch
if [ -d "$TMP_DIR" ]; then
  git worktree remove -f "$TMP_DIR" || true
fi

# If branch exists on remote, check it out; otherwise create orphan branch
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  git worktree add "$TMP_DIR" origin/$BRANCH
else
  git worktree add -B $BRANCH "$TMP_DIR"
fi

echo "Copying frontend files..."
rm -rf "$TMP_DIR"/*
cp -r "$FRONTEND_DIR"/* "$TMP_DIR"/

cd "$TMP_DIR"
git add --all
if git commit -m "Deploy frontend to GitHub Pages"; then
  git push origin $BRANCH
  echo "Deployed to branch $BRANCH"
else
  echo "No changes to deploy"
fi

cd - >/dev/null
git worktree remove -f "$TMP_DIR" || true

echo "Done. Configure GitHub Pages to serve branch '$BRANCH' (root) in repository Settings."
