# Deployment Guide - Portergeist Art

## 🚀 Deploy to Vercel (Recommended)

### Prerequisites
- GitHub account (optional but recommended)
- Vercel account (free tier works)

### Option 1: Deploy via Vercel CLI (Fastest)

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to project
cd ~/clawd/portergeist-art

# Login to Vercel
vercel login

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name? portergeist-art
# - In which directory? ./
# - Override settings? N

# You'll get a URL like: portergeist-art.vercel.app
```

### Option 2: Deploy via Vercel Dashboard (Easy)

1. Push to GitHub:
```bash
cd ~/clawd/portergeist-art
git init
git add .
git commit -m "Initial commit - Portergeist Art portfolio"
gh repo create portergeist-art --public --source=. --push
```

2. Go to [vercel.com/new](https://vercel.com/new)
3. Import your GitHub repository
4. Leave all settings default
5. Click "Deploy"

Site will be live in ~1 minute at `portergeist-art.vercel.app`

### Production Deployment

After testing the preview URL:

```bash
# Deploy to production
vercel --prod
```

## 🌐 Custom Domain Setup

### Buy Domain
Recommended registrars:
- **Namecheap** — `portergeist.art` (~$10/year)
- **Porkbun** — `chanceporter.tattoo` (~$30/year for .tattoo TLD)
- **Google Domains** — `portergeistartwork.com` (~$12/year)

### Connect to Vercel

1. In Vercel dashboard, go to your project
2. Click "Settings" → "Domains"
3. Add your domain (e.g., `portergeist.art`)
4. Vercel will give you DNS records to add

**For root domain (portergeist.art):**
```
Type: A
Name: @
Value: 76.76.21.21
```

**For www subdomain:**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

5. Add these records in your domain registrar's DNS settings
6. Wait 5-60 minutes for DNS propagation
7. Vercel will auto-issue SSL certificate (HTTPS)

## 🔧 Other Deployment Options

### Netlify

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --dir=. --prod
```

Or drag-and-drop the entire folder in [Netlify Drop](https://app.netlify.com/drop)

### GitHub Pages

```bash
# Create gh-pages branch
git checkout -b gh-pages
git push origin gh-pages

# Enable in repo settings → Pages → Source: gh-pages branch
```

Site will be at `username.github.io/portergeist-art`

### Firebase Hosting

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Initialize
firebase init hosting

# Deploy
firebase deploy --only hosting
```

## 📧 Form Backend Setup

### Formspree (Recommended for simplicity)

1. Sign up at [formspree.io](https://formspree.io) (free tier: 50 submissions/month)
2. Create new form
3. Copy form endpoint
4. Update `index.html`:

```html
<form action="https://formspree.io/f/YOUR-FORM-ID" method="POST" class="consultation-form" id="consultationForm">
```

5. Remove JavaScript form handler or update to work with Formspree

### Netlify Forms (If using Netlify)

Just add `netlify` attribute:

```html
<form netlify name="consultation" class="consultation-form">
```

Submissions will appear in Netlify dashboard.

### Web3Forms (Alternative)

1. Get API key from [web3forms.com](https://web3forms.com)
2. Add hidden field:

```html
<input type="hidden" name="access_key" value="YOUR-ACCESS-KEY">
```

3. Update form action:

```html
<form action="https://api.web3forms.com/submit" method="POST">
```

## 🔒 Environment Variables (If needed)

If you add analytics or API keys:

```bash
# Create .env file (already in .gitignore)
echo "GA_TRACKING_ID=G-XXXXXXXXXX" >> .env
echo "FORMSPREE_KEY=xpxxxxxxx" >> .env

# Add to Vercel
vercel env add GA_TRACKING_ID
# Enter value when prompted
```

## 📊 Analytics Setup

### Google Analytics

1. Create property at [analytics.google.com](https://analytics.google.com)
2. Get Measurement ID (G-XXXXXXXXXX)
3. Add to `index.html` before `</head>`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Vercel Analytics (Easier)

1. In Vercel dashboard, go to "Analytics"
2. Click "Enable"
3. Add snippet to `index.html` before `</body>`:

```html
<script src="/_vercel/insights/script.js" defer></script>
```

## 🎯 SEO Enhancements

### robots.txt

Create `robots.txt`:

```
User-agent: *
Allow: /

Sitemap: https://portergeist.art/sitemap.xml
```

### sitemap.xml

Create `sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://portergeist.art/</loc>
    <lastmod>2026-03-01</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

### Open Graph Tags

Add to `<head>` in `index.html`:

```html
<meta property="og:title" content="Portergeist Art | Chance Porter - Tattoo Artist">
<meta property="og:description" content="Neo-traditional, blackwork, and illustrative tattoo artist at Red Raven Tattoo, Utica NY">
<meta property="og:image" content="https://portergeist.art/images/og-image.jpg">
<meta property="og:url" content="https://portergeist.art">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
```

## 🚨 Pre-Launch Checklist

- [ ] All placeholder images replaced with real photos
- [ ] Tip jar links updated (Venmo/CashApp/PayPal)
- [ ] Contact email verified
- [ ] Form backend configured and tested
- [ ] Social media links verified
- [ ] Tested on mobile devices (iOS Safari, Chrome)
- [ ] Tested on desktop (Chrome, Firefox, Safari)
- [ ] All images optimized (< 500KB each)
- [ ] Google Analytics added (optional)
- [ ] Custom domain configured (if applicable)
- [ ] SSL certificate active (automatic with Vercel)
- [ ] Final review by Chance Porter

## 🎉 Post-Launch

1. **Submit to Google Search Console**
   - Add property
   - Verify ownership
   - Submit sitemap

2. **Social Media Announcement**
   - Post on Instagram/TikTok with link
   - Pin story highlight with portfolio link
   - Update bio link

3. **Monitor**
   - Check analytics weekly
   - Monitor form submissions
   - Track conversion (consult requests)

4. **Iterate**
   - Add more portfolio images as work is completed
   - Update flash gallery when designs are claimed
   - Gather testimonials for future addition

---

**Built by Sudo Built Apps for Chance Porter / Portergeist Art**

Need updates? Contact jay.klinkowsky@outlook.com
