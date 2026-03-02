# Portergeist Art - Portfolio Website

Premium dark-themed portfolio website for **Chance Porter**, tattoo artist at Red Raven Tattoo in Utica, NY.

**Brand:** Portergeist Art  
**Instagram:** [@portergeist_art](https://instagram.com/portergeist_art) (50K+ followers)  
**TikTok:** [@chance_portergeist](https://tiktok.com/@chance_portergeist) (200K+ followers)  
**Facebook:** Chance Porter  

## 🎨 Design Inspiration

Inspired by [davidpeyote.com](https://davidpeyote.com) — dark, minimal, art-forward, portfolio-first approach.

## ✨ Features

- **Hero Section** — Full-bleed atmospheric hero with bold typography
- **Portfolio Gallery** — Filterable masonry grid of completed tattoo work
- **Flash Designs** — Separate gallery for available pre-drawn designs with Available/Claimed badges
- **About Section** — Artist bio with social proof stats
- **Consultation Form** — Initial consultation request (name, email, phone, tattoo description, placement, size, references)
- **Tip Jar** — Venmo/CashApp/PayPal support links
- **Lightbox** — Click to expand images with keyboard navigation
- **Scroll Reveal Animations** — Smooth fade-in on scroll
- **Dark Theme Throughout** — Deep blacks, blood red accents (#8B0000)
- **Fully Responsive** — Mobile-first design, hamburger nav
- **No Frameworks** — Pure HTML/CSS/JS for fast loading

## 🚀 Quick Start

### 1. Replace Placeholder Images

The site currently uses gradient placeholders. **Replace with real images:**

```bash
# Portfolio images (completed work)
images/portfolio-1.jpg through portfolio-12.jpg
# Recommended: 600x800px (portrait), high quality JPEGs

# Flash designs (available pieces)
images/flash-1.jpg through flash-8.jpg
# Recommended: 600x600px (square), high quality JPEGs
```

**Downloading from Instagram:**
- Use a tool like [Instaloader](https://instaloader.github.io/) or [4K Stogram](https://www.4kdownload.com/products/stogram)
- Or manually screenshot and crop from [@portergeist_art](https://instagram.com/portergeist_art)

### 2. Update Contact Info

Edit `index.html` and update:

```html
<!-- Line ~400: Tip jar links -->
<a href="https://venmo.com/YOUR-HANDLE" class="tip-btn tip-venmo">
<a href="https://cash.app/$YOUR-HANDLE" class="tip-btn tip-cashapp">
<a href="https://paypal.me/YOUR-HANDLE" class="tip-btn tip-paypal">

<!-- Line ~450: Contact email -->
<p><a href="mailto:YOUR-EMAIL@example.com">YOUR-EMAIL@example.com</a></p>
```

### 3. Configure Form Backend (Optional)

The consultation form currently just logs to console. To make it functional:

**Option A: Formspree (Easy, Free)**
```html
<form action="https://formspree.io/f/YOUR-FORM-ID" method="POST" class="consultation-form">
```

**Option B: Netlify Forms**
```html
<form netlify class="consultation-form">
```

**Option C: Custom Backend**
- Set up API endpoint
- Update `script.js` form handler to POST to your endpoint

### 4. Test Locally

```bash
# Simple HTTP server
python3 -m http.server 8000

# Or use VS Code Live Server extension
# Or any static file server
```

Visit `http://localhost:8000`

## 📦 Deploy to Vercel

### One-Click Deploy

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

Follow prompts, then your site will be live at `your-project.vercel.app`

### Custom Domain

1. Add domain in Vercel dashboard
2. Update DNS records as instructed
3. Enable HTTPS (automatic)

Suggested domains:
- `portergeist.art`
- `chanceporter.tattoo`
- `portergeistartwork.com`

## 🎨 Customization Guide

### Colors

Edit `styles.css` `:root` variables:

```css
:root {
    --color-bg: #0a0a0a;              /* Main background */
    --color-accent: #8B0000;          /* Deep red accent */
    --color-text: #e8e8e8;            /* Main text */
    --color-text-muted: #a0a0a0;      /* Secondary text */
}
```

### Typography

Using Google Fonts:
- **Display (Titles):** Bebas Neue
- **Headings:** Oswald
- **Body:** Inter

To change fonts, update the Google Fonts link in `index.html` and CSS variables.

### Gallery Images

**To add more images:**

1. Edit `script.js` arrays:

```javascript
const portfolioImages = [
    { id: 13, src: 'images/portfolio-13.jpg', category: 'blackwork', caption: 'Your Caption' },
    // ... add more
];

const flashDesigns = [
    { id: 9, src: 'images/flash-9.jpg', title: 'Design Name', size: '4x6"', available: true },
    // ... add more
];
```

2. Add corresponding image files to `images/` folder

### Navigation

To add "Gear" or other sections later:

1. Add nav link in `index.html`:
```html
<li><a href="#gear" class="nav-link">Gear</a></li>
```

2. Add section:
```html
<section id="gear" class="gear">
    <!-- Your content -->
</section>
```

## 📁 File Structure

```
portergeist-art/
├── index.html              # Main HTML
├── styles.css              # All styles (dark theme)
├── script.js               # Interactivity (gallery, lightbox, forms)
├── images/                 # Portfolio and flash images
│   ├── portfolio-1.jpg
│   ├── flash-1.jpg
│   └── ...
├── generate-placeholders.py  # Script to regenerate placeholders
├── README.md               # This file
└── vercel.json             # Vercel deployment config
```

## 🔧 Advanced Features

### Add Google Analytics

```html
<!-- Add before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Add Instagram Feed

Use [Juicer.io](https://www.juicer.io/) or [SnapWidget](https://snapwidget.com/) to embed live Instagram feed.

### SEO Optimization

Already includes:
- Semantic HTML
- Meta description
- Alt tags on images
- Fast loading (no frameworks)

Additional improvements:
- Add `robots.txt`
- Add `sitemap.xml`
- Optimize images (compress JPEGs)
- Add Open Graph tags for social sharing

## 💡 Tips for Best Results

1. **Image Quality** — Use high-resolution photos (at least 1200px width)
2. **Consistent Aspect Ratios** — Portfolio: 3:4 portrait, Flash: 1:1 square
3. **File Sizes** — Compress images to < 500KB each for fast loading
4. **Real Content** — Replace ALL placeholders before launching
5. **Test on Mobile** — Most visitors will be on phones
6. **Social Links** — Verify all Instagram/TikTok/Facebook links work

## 🛠️ Troubleshooting

**Images not showing?**
- Check file paths match exactly (case-sensitive)
- Ensure images are in `images/` folder
- Check browser console for 404 errors

**Form not submitting?**
- Set up Formspree or Netlify Forms
- Check browser console for errors
- Test with valid email format

**Layout breaking on mobile?**
- Clear browser cache
- Test in multiple browsers
- Check for CSS syntax errors

## 📞 Support

Built by **Sudo Built Apps** for Chance Porter.

For updates or changes, contact:
- Jay Klinkowsky
- Email: jay.klinkowsky@outlook.com

## 📄 License

© 2026 Portergeist Art / Chance Porter. All rights reserved.

---

## 🚀 LAUNCH CHECKLIST

Before going live:

- [ ] Replace all 12 portfolio placeholder images
- [ ] Replace all 8 flash design placeholder images
- [ ] Update tip jar links (Venmo, CashApp, PayPal)
- [ ] Verify contact email
- [ ] Set up form backend (Formspree/Netlify)
- [ ] Test on mobile devices
- [ ] Verify all social links work
- [ ] Add Google Analytics (optional)
- [ ] Test form submission
- [ ] Check all images load
- [ ] Deploy to Vercel
- [ ] Set up custom domain (optional)
- [ ] Share with Chance for approval

**When ready, this site will look like a $5K+ custom build. Ship it with pride. ⚔️**
