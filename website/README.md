# Website for cookiecutter-fastapi-mongo

This directory contains the GitHub Pages website for the cookiecutter-fastapi-mongo template.

## Structure
```
website/
├── package.json       # Node.js dependencies
├── public/            # Static website files
│   ├── index.html     # Main website page
│   └── .nojekyll      # GitHub Pages config
└── README.md          # This file
```

## Deployment

### Install Dependencies
```bash
cd website
npm install
```

### Deploy to GitHub Pages
```bash
npm run deploy
```

This will deploy the `public/` directory to the `gh-pages` branch using the `gh-pages` package.

## Development

To view the website locally, simply open `public/index.html` in your browser or use a local server:

```bash
cd public
python -m http.server 8000
```

Then visit `http://localhost:8000`

## Support

If you find this project helpful, consider supporting its development:


[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/klee1611)

Or visit: https://www.buymeacoffee.com/klee1611

