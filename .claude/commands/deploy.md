---
description: "Deploy project to GitHub and Vercel"
---

# Deploy

Deploy the project to GitHub and go live on Vercel.

## Workflow

### 1. GitHub Setup

Check if git is initialized:
```
git status
```

If not initialized:
```
git init
git add .
git commit -m "Initial commit"
```

Check GitHub CLI auth:
```
gh --version
gh auth status
```

If not authenticated:
```
gh auth login --web --git-protocol https
```

Create the GitHub repo and push:
```
gh repo create [project-name] --private --source=. --push
```

Confirm with:
```
gh repo view --web
```

### 2. Vercel Deployment

Check if Vercel CLI is installed:
```
vercel --version
```

If not installed:
```
npm i -g vercel
```

Login and deploy:
```
vercel login
vercel --prod --yes
```

Open the live URL:
```
open [vercel-url]
```

## Notes

- Use TodoWrite to track deployment steps
- Ensure the user has GitHub and Vercel accounts before starting
- The `--yes` flag skips interactive prompts
- Vercel auto-deploys on future git pushes
- Return the live URL to the user when complete
