# 🎨 Portergeist Art - Quick Reference Card

## 🚀 One-Liners

```bash
# Preview locally
cd ~/clawd/portergeist-art && ./preview.sh

# Deploy to Vercel
cd ~/clawd/portergeist-art && vercel

# Deploy to production
cd ~/clawd/portergeist-art && vercel --prod
```

---

## 📝 Must Update Before Launch

### 1. Replace Images
- **Location:** `~/clawd/portergeist-art/images/`
- **Portfolio:** 12 images (600x800px portrait)
- **Flash:** 8 images (600x600px square)
- **Source:** Download from @portergeist_art Instagram/TikTok

### 2. Contact Info (in `index.html`)
- **Line ~315:** Venmo, CashApp, PayPal links
- **Line ~440:** Contact email

### 3. Form Backend (optional)
- **Formspree:** Sign up, add endpoint to form action
- **Netlify:** Add `netlify` attribute to form
- **Custom:** Update `script.js` form handler

---

## 📁 File Structure

```
index.html        ← Main site
styles.css        ← All styles (dark theme)
script.js         ← Interactivity
images/           ← Portfolio + flash images
README.md         ← Full guide
DEPLOYMENT.md     ← Deploy instructions
HANDOFF-FOR-JAY.md ← This handoff doc
```

---

## 🎯 Key Features

- ✅ Dark theme (blood red accents)
- ✅ Responsive (mobile-first)
- ✅ Portfolio gallery (filterable)
- ✅ Flash gallery (Available/Claimed)
- ✅ Consultation form
- ✅ Tip jar (Venmo/CashApp/PayPal)
- ✅ Lightbox (click to expand)
- ✅ Scroll animations
- ✅ No frameworks (pure HTML/CSS/JS)

---

## 🌐 Deployment URLs

| Platform | Command | Free Tier | Custom Domain |
|----------|---------|-----------|---------------|
| Vercel | `vercel` | ✅ Yes | ✅ Free |
| Netlify | `netlify deploy --prod` | ✅ Yes | ✅ Free |
| GitHub Pages | Enable in settings | ✅ Yes | ✅ Free |

---

## 💰 Value

**This site would cost $5,000 if built by an agency.**

Built as favor/proof-of-concept to win Chance as client.

---

## 📞 Chance Porter Info

- **Instagram:** [@portergeist_art](https://instagram.com/portergeist_art) (50K+)
- **TikTok:** [@chance_portergeist](https://tiktok.com/@chance_portergeist) (200K+)
- **Studio:** Red Raven Tattoo, Utica, NY
- **Style:** Neo-traditional, blackwork, illustrative

---

## ✅ Pre-Launch Checklist

- [ ] Preview locally
- [ ] Replace images (6+ portfolio, 4+ flash minimum)
- [ ] Update tip jar links
- [ ] Update contact email
- [ ] Deploy to Vercel
- [ ] Share preview with Chance
- [ ] Get approval
- [ ] Deploy to production
- [ ] Optional: custom domain
- [ ] Launch!

---

## 🆘 Troubleshooting

**Preview won't start?**
```bash
cd ~/clawd/portergeist-art
python3 -m http.server 8000
# Then open http://localhost:8000
```

**Vercel deploy fails?**
```bash
vercel login
# Then try again
```

**Images not showing?**
- Check file names match exactly (case-sensitive)
- Ensure images are in `images/` folder
- Check browser console for 404 errors

**Form not working?**
- Set up Formspree or Netlify Forms
- See DEPLOYMENT.md for instructions

---

**Ready to ship. ⚔️**
