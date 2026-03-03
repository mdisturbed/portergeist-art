# Deployment Status: portergeist.art

**Date:** March 2, 2026  
**Status:** ✅ Site deployed, awaiting DNS configuration

---

## ✅ Completed

1. **GitHub Repository**
   - Created: https://github.com/mdisturbed/portergeist-art
   - Branch: `main`
   - All site files pushed

2. **GitHub Pages**
   - Enabled on `main` branch
   - Custom domain configured: `portergeist.art`
   - CNAME file added and pushed

3. **Temporary URL**
   - Site live at: https://mdisturbed.github.io/portergeist-art/
   - Fully functional and ready

4. **Documentation**
   - SOP written: `~/clawd/wiki/docs/processes/client-site-deployment.md`
   - Handoff guide included
   - Email options documented

---

## 🔴 ACTION REQUIRED: DNS Configuration

**Jay must add these DNS records on Porkbun:**

### DNS Records to Add

| Record Type | Name | Value | TTL |
|-------------|------|-------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | mdisturbed.github.io | 3600 |

### How to Add (Porkbun)

1. Log in to Porkbun
2. Go to **Domain Management** → Select `portergeist.art`
3. Click **DNS Records**
4. Add each A record:
   - Type: **A**
   - Host: **@** (leave blank or enter @)
   - Answer: **[GitHub IP]**
   - TTL: **3600**
5. Add CNAME record:
   - Type: **CNAME**
   - Host: **www**
   - Answer: **mdisturbed.github.io**
   - TTL: **3600**
6. **Save all changes**

### Verification

**Wait 5-60 minutes**, then test:

```bash
dig portergeist.art +short
```

Should return:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Online check:** https://dnschecker.org/#A/portergeist.art

---

## 🔐 Next Step: Enable HTTPS

**AFTER DNS propagates and site loads at http://portergeist.art:**

```bash
gh api -X PUT repos/mdisturbed/portergeist-art/pages -f "https_enforced=true"
```

**Or** via GitHub UI:
1. Go to repo settings
2. Click **Pages**
3. Check **Enforce HTTPS**

**Timeline:** Certificate provisioning takes 5-30 minutes after DNS propagation

---

## 📧 Email Forwarding Options

**Two options for Chance's email (booking@portergeist.art, etc.):**

### Option A: Cloudflare Email Routing (Recommended)

**Pros:**
- Free unlimited forwarding
- Reliable, fast delivery
- Easy to manage
- Catch-all support

**Cons:**
- Requires moving DNS to Cloudflare (nameserver change at Porkbun)

**Setup:**
1. Add domain to Cloudflare (free account)
2. Copy nameservers from Cloudflare
3. Update nameservers at Porkbun
4. Add DNS records in Cloudflare (same A + CNAME as above)
5. Enable Email Routing in Cloudflare
6. Add forwarding addresses:
   - `booking@portergeist.art` → Chance's email
   - `info@portergeist.art` → Chance's email
   - `chance@portergeist.art` → Chance's email

**Time:** 30 minutes + 24-48 hours nameserver propagation

---

### Option B: Porkbun Email Forwarding

**Pros:**
- No DNS migration
- Simple setup
- Free (up to 10 addresses)

**Cons:**
- Limited features
- Less reliable than Cloudflare

**Setup:**
1. Log in to Porkbun
2. Go to `portergeist.art` → **Email Forwarding**
3. Click **Enable Email Forwarding**
4. Add forwarding rules:
   - `booking@portergeist.art` → Chance's email
   - `info@portergeist.art` → Chance's email
   - `chance@portergeist.art` → Chance's email
5. Verify destination email (Porkbun sends confirmation)

**Time:** 10 minutes

---

## 📋 Go-Live Checklist

Once DNS propagates:

- [ ] Site loads at `https://portergeist.art`
- [ ] Site loads at `https://www.portergeist.art`
- [ ] Green padlock (HTTPS)
- [ ] All images load
- [ ] Gallery works
- [ ] Contact form works (if backend added)
- [ ] Email forwarding tested
- [ ] Mobile responsive (test on phone)

---

## 🤝 Client Handoff

**What to give Chance:**

1. **Live site URL:** https://portergeist.art
2. **Email access:** Login credentials (Cloudflare or Porkbun)
3. **GitHub access:** Repo URL + how to request changes
4. **Contact form:** Which email receives submissions (if applicable)
5. **Support:** How to reach us for updates

**Template email in SOP:** `~/clawd/wiki/docs/processes/client-site-deployment.md`

---

## 🔧 Making Updates

**To update the site:**

1. Edit files locally in `~/clawd/portergeist-art/`
2. Test locally: `open index.html` in browser
3. Commit changes:
   ```bash
   cd ~/clawd/portergeist-art
   git add .
   git commit -m "Update: [description]"
   git push
   ```
4. Wait 1-5 minutes → changes live

**No server, no deploy process — just git push!**

---

## 📚 Reference

- **SOP:** `~/clawd/wiki/docs/processes/client-site-deployment.md`
- **GitHub Repo:** https://github.com/mdisturbed/portergeist-art
- **GitHub Pages Docs:** https://docs.github.com/pages
- **DNS Checker:** https://dnschecker.org
- **Contact Form Options:** Formspree (50/mo free) or Formsubmit (unlimited free)

---

**Next Action:** Jay adds DNS records on Porkbun → wait for propagation → enable HTTPS → choose email option → go live!
