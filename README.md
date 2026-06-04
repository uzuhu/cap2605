# HUAYU Capacitor Website

Nantong Huayu Electronics Co., Ltd. official website — Jekyll + GitHub Pages.

## Local Development

```bash
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Deploy to GitHub Pages

1. Create repo `uzuhu.github.io` (or `capacitormanufacturer.com` with custom domain)
2. Push:
```bash
git init
git add .
git commit -m "Initial commit: HUAYU capacitor website"
git remote add origin git@github.com:uzuhu/uzuhu.github.io.git
git push -u origin main
```
3. Enable GitHub Pages in repo Settings → Pages → Build from `main` branch
4. (Optional) Add custom domain `capacitormanufacturer.com` in Settings → Pages → Custom domain

## Site Structure

```
├── _config.yml          # Site config
├── _layouts/           # Jekyll layouts
├── _includes/          # Header/footer/breadcrumb
├── _products/          # (future) product detail pages
├── _applications/      # Industry application pages
├── _blog/             # (future) blog posts
├── css/style.css       # Main stylesheet
├── js/main.js          # Mobile nav, filters
├── pdf/               # Datasheets & catalog
├── images/             # Product & industry photos
├── index.html          # Homepage
├── products.html        # Product listing + comparison
├── products/compare.html  # Parameter comparison table
├── technical.html      # Technical reference
├── about.html          # Company profile
├── contact.html        # Contact (email link)
└── applications.html    # Industry applications overview
```

## Customization Checklist

- [ ] Add real product photos to `images/products/` (see size hints in HTML)
- [ ] Add industry/application photos to `images/industries/`
- [ ] Replace placeholder `img-placeholder` divs with `<img>` tags
- [ ] Update `_config.yml` with real domain when deployed
- [ ] Configure Formspree ID in `contact.html` if using contact form
- [ ] Add Google Analytics / Microsoft Clarity tracking code if needed
