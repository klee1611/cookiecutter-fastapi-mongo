# Website for cookiecutter-fastapi-mongo

This directory contains the GitHub Pages website for the cookiecutter-fastapi-mongo template.

## Structure
```
website/
├── package.json       # Node.js dependencies (for manual deployment)
├── public/            # Static website files
│   ├── index.html     # Main website page
│   └── .nojekyll      # GitHub Pages config
└── README.md          # This file
```

## Deployment

### Automatic Deployment (Primary Method)

The website is automatically deployed via GitHub Actions when changes are pushed to `main` or `develop` branches.

- **Workflow:** `.github/workflows/deploy-pages.yml`
- **Source:** `website/public/` directory
- **Trigger:** Push to `main` or `develop`, or manual workflow dispatch

This is the **authoritative deployment method**. Changes pushed to these branches will automatically deploy to GitHub Pages.

### Manual Deployment (Optional)

For testing or emergency updates, you can manually deploy using npm:

#### Install Dependencies
```bash
cd website
npm install
```

#### Deploy to GitHub Pages
```bash
npm run deploy
```

**Note:** This deploys the `public/` directory to the `gh-pages` branch. Use this only for:
- Testing deployment locally before pushing
- Emergency hotfixes that can't wait for the normal CI/CD process
- Development and preview purposes

The GitHub Actions workflow is the preferred and authoritative deployment method for production.

## Development

To view the website locally, simply open `public/index.html` in your browser or use a local server:

```bash
cd public
python -m http.server 8000
```

Then visit `http://localhost:8000`
