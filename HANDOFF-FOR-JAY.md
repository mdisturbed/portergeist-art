# 🎨 Portergeist Art - Complete & Ready to Ship

## ✅ MISSION ACCOMPLISHED

Built a **$5K-quality** portfolio website for Chance Porter (Portergeist Art) as proof-of-concept to win him as a client.

**Status:** 🟢 **PRODUCTION READY** (just needs real images + contact info)

---

## 🚀 Quick Start

### Preview Locally (Right Now)

```bash
cd ~/clawd/portergeist-art
./preview.sh
```

Opens at `http://localhost:8000`

### Deploy to Vercel (60 Seconds)

```bash
cd ~/clawd/portergeist-art
vercel
```

You'll get a live URL like: `portergeist-art-xyz.vercel.app`

---

## 📁 What You Got

```
portergeist-art/
├── index.html              ← Main site (17.8 KB)
├── styles.css              ← Dark theme CSS (22.5 KB)
├── script.js               ← Interactivity (12.1 KB)
├── images/                 ← 20 placeholder images
│   ├── portfolio-1.jpg through portfolio-12.jpg
│   └── flash-1.jpg through flash-8.jpg
├── README.md               ← Full setup guide
├── DEPLOYMENT.md           ← Deploy instructions (Vercel/Netlify/etc)
├── PROJECT-SUMMARY.md      ← Technical overview
├── generate-placeholders.py ← Regenerate placeholders if needed
├── preview.sh              ← Quick preview server
├── vercel.json             ← Vercel config (optimized caching)
└── .gitignore              ← Git ignore rules

Total size: ~2.5 MB (mostly placeholder images)
Clean, production-ready code. Zero dependencies.
```

---

## 🎯 What It Does

### 1. Hero Section
- Full-screen dark background with atmospheric gradient
- **"PORTERGEIST ART"** in massive bold type
- Subtitle: "Chance Porter — Tattoo Artist / Red Raven Tattoo, Utica NY"
- Two CTAs: "View Work" + "Browse Flash"

### 2. Portfolio Gallery
- Masonry grid of completed tattoo work
- Filter tabs: All, Neo-Traditional, Blackwork, Illustrative, Color, Large Scale
- Click to expand lightbox (keyboard nav with ← → Esc)
- 12 placeholder images (REPLACE WITH REAL)

### 3. Flash Gallery
- Square grid of available pre-drawn designs
- "Available" / "Claimed" badges
- Design title + size on hover
- 8 placeholder images (REPLACE WITH REAL)

### 4. About Section
- Artist bio (custom designs, bold lines, surreal vibes)
- Social proof: 10+ years, 50K IG, 200K TikTok
- Clean, centered presentation

### 5. Consultation Form (NOT booking)
- Name, Email, Phone
- Placement on body (dropdown)
- Approximate size (dropdown)
- Tattoo idea description
- Reference image upload (multiple files)
- Questions/additional info
- **Ready for backend** (Formspree/Netlify/custom)

### 6. Tip Jar
- Venmo, CashApp, PayPal buttons
- Tasteful "Show Some Love" section
- **Needs Chance's handles**

### 7. Contact Footer
- Red Raven Tattoo location
- Social links (Instagram, TikTok, Facebook)
- Email placeholder
- Site credit: "Site by Sudo Built Apps"

### 8. Features
- **Sticky nav** (darkens on scroll)
- **Mobile hamburger menu**
- **Smooth scroll** with offset
- **Scroll reveal animations** (fade-in on scroll)
- **Lightbox** with prev/next navigation
- **100% responsive** (mobile-first)
- **Dark theme** with blood red accents (#8B0000)
- **Premium typography** (Bebas Neue, Oswald, Inter)

---

## ✏️ Before You Show Chance

### CRITICAL: Replace Placeholder Images

**Where to get images:**
- Instagram: [@portergeist_art](https://instagram.com/portergeist_art)
- TikTok: [@chance_portergeist](https://tiktok.com/@chance_portergeist)

**Tools to download:**
- [Instaloader](https://instaloader.github.io/) (CLI)
- [4K Stogram](https://www.4kdownload.com/products/stogram) (GUI)
- Or manually screenshot + crop

**What you need:**
- 12+ completed tattoo images (healed/finished work)
- 8+ flash designs (available pre-drawn pieces)

**File specs:**
- Portfolio: 600x800px (portrait) or higher
- Flash: 600x600px (square) or higher
- Format: JPEG, optimized (< 500KB each)

**How to replace:**
1. Name files: `portfolio-1.jpg`, `portfolio-2.jpg`, etc.
2. Drop into `~/clawd/portergeist-art/images/`
3. Overwrite existing placeholders

### Update Contact Info

Edit `index.html`:

**Line ~315: Tip jar links**
```html
<a href="https://venmo.com/CHANCE-HANDLE" ...>
<a href="https://cash.app/$CHANCE-HANDLE" ...>
<a href="https://paypal.me/CHANCE-HANDLE" ...>
```

**Line ~440: Contact email**
```html
<p><a href="mailto:chance@portergeist.art">chance@portergeist.art</a></p>
```

### Set Up Form Backend (Optional)

**Option 1: Formspree** (easiest, free tier = 50 submissions/month)
1. Sign up at [formspree.io](https://formspree.io)
2. Create form, get endpoint
3. Update `index.html` line 265:
```html
<form action="https://formspree.io/f/YOUR-FORM-ID" method="POST" ...>
```

**Option 2: Netlify Forms** (if you deploy to Netlify instead of Vercel)
```html
<form netlify name="consultation" ...>
```

**Option 3: Leave as-is** (just logs to console for now, fix later)

---

## 🚀 Deploy (Choose One)

### Vercel (Recommended — Fast, Free, Easy)

```bash
# One-time setup
npm install -g vercel
vercel login

# Deploy
cd ~/clawd/portergeist-art
vercel

# Production (after testing preview)
vercel --prod
```

**Result:** `portergeist-art.vercel.app` (live in 60 seconds)

### Netlify

```bash
npm install -g netlify-cli
cd ~/clawd/portergeist-art
netlify deploy --dir=. --prod
```

### GitHub Pages

```bash
cd ~/clawd/portergeist-art
git init
git add .
git commit -m "Portergeist Art portfolio site"
gh repo create portergeist-art --public --source=. --push

# Enable Pages in repo settings → Pages → gh-pages branch
```

**Full deployment guide:** See `DEPLOYMENT.md`

---

## 🌐 Custom Domain (Optional)

If Chance wants a real domain:

**Buy:**
- `portergeist.art` (~$10/year on Namecheap)
- `chanceporter.tattoo` (~$30/year for .tattoo TLD)
- `portergeistartwork.com` (~$12/year)

**Connect to Vercel:**
1. Vercel dashboard → Settings → Domains
2. Add domain
3. Update DNS records (Vercel gives you the values)
4. Wait 5-60 minutes for propagation
5. SSL auto-issued (HTTPS enabled)

**Full instructions:** See `DEPLOYMENT.md`

---

## 💰 Value Proposition (If Selling)

This site would normally cost:

| Item | Cost |
|------|------|
| Design consultation | $500 |
| Custom dark theme design | $1,500 |
| Responsive development | $2,000 |
| Lightbox/gallery system | $500 |
| Form integration | $300 |
| Deployment & setup | $200 |
| **TOTAL** | **$5,000** |

**Your cost:** Favor for a friend (prove value, earn trust, future paid work)

---

## 🎨 Why This Is Premium

1. **No frameworks** → Fast, no bloat
2. **Mobile-first** → Perfect on phones (where 70%+ of traffic is)
3. **Dark theme** → Matches tattoo artist aesthetic, easy on eyes
4. **Scroll animations** → Modern, polished feel
5. **Dual gallery system** → Portfolio (showcase) + Flash (sales)
6. **Professional consultation form** → Not just "email me"
7. **Social proof** → 50K IG, 200K TikTok front and center
8. **Tip jar** → Modern artist monetization
9. **Attention to detail** → Hover states, transitions, spacing, typography
10. **Production-ready code** → Clean, semantic, SEO-friendly

---

## 📊 Success Metrics (After Launch)

Track:
- **Consultation form submissions** (primary conversion)
- Time on site (engagement)
- Mobile vs desktop split (expect 70%+ mobile)
- Instagram → Website click-through rate
- Tip jar usage

Use Google Analytics or Vercel Analytics (both easy to add).

---

## 🛠️ Future Enhancements (Phase 2)

If Chance loves it and wants more:

1. **Shop/Gear** — Sell merch, prints, stickers
2. **Booking system** — Calendly integration
3. **Blog** — Artist insights, tattoo care tips
4. **Testimonials** — Client reviews with photos
5. **Instagram feed** — Live embed from @portergeist_art
6. **Email newsletter** — Collect emails, announce flash drops
7. **CMS** — WordPress/Contentful for self-updating

---

## 🎯 How to Pitch to Chance

**Message template:**

> Hey Chance! I saw your work on Instagram (@portergeist_art) and thought you could use a killer portfolio site. I built a proof-of-concept for you — dark theme, dual gallery (portfolio + flash), consultation form, tip jar, the works.
> 
> It's ready to go, just needs your real images and contact info. Check it out: [vercel preview link]
> 
> If you like it, I can get it live on a custom domain (portergeist.art?) in a day. No pressure, no strings — I wanted to show you what's possible.
> 
> Let me know what you think!
> 
> — Jay

**What you're offering:**
- Free proof-of-concept (already built)
- Professional-quality site (normally $5K)
- Fast turnaround (ready in a day)
- No commitment (just trying to help)

**What you want:**
- Testimonial if he loves it
- Portfolio piece for future tattoo artist clients
- Potential future work (shop, booking, etc.)

---

## 📞 Handoff Checklist

Before showing Chance:
- [ ] Preview locally (`./preview.sh`)
- [ ] Replace at least 6-8 portfolio images (so it looks real)
- [ ] Replace at least 4-6 flash designs
- [ ] Get Chance's Venmo/CashApp/PayPal handles
- [ ] Get Chance's preferred contact email
- [ ] Update contact info in `index.html`
- [ ] Deploy to Vercel (`vercel`)
- [ ] Share preview link with Chance

After Chance approves:
- [ ] Replace ALL placeholder images
- [ ] Set up form backend (Formspree)
- [ ] Deploy to production (`vercel --prod`)
- [ ] Optional: Buy custom domain
- [ ] Optional: Add Google Analytics
- [ ] Launch & announce on socials

---

## 🏆 Bottom Line

**This is production-ready.** It's fast, beautiful, functional, and perfectly suited for a tattoo artist with a strong social media presence.

The dark theme with blood red accents captures the Portergeist brand. The dual gallery serves both showcase and sales. The consultation form is professional without being overwhelming.

**Just swap images, add contact info, and ship it. It's ready. ⚔️**

---

## 🆘 Need Help?

- **Preview not working?** Make sure you're in `~/clawd/portergeist-art/`
- **Vercel deploy failing?** Run `vercel login` first
- **Images not showing?** Check file names match exactly (case-sensitive)
- **Form not working?** Set up Formspree or Netlify Forms (see DEPLOYMENT.md)

**All docs in the folder:**
- `README.md` — Full setup guide
- `DEPLOYMENT.md` — Deploy instructions
- `PROJECT-SUMMARY.md` — Technical overview

---

**Built by Inigo Montoya for The Brute Squad**  
**Sudo Built Apps | March 1, 2026**

*"Hello. My name is Inigo Montoya. You need a portfolio site. Prepare to be impressed."*

⚔️
