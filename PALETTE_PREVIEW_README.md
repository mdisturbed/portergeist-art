# Color Palette Preview Tool

## What Was Added
A temporary theme switcher that allows Chance to preview and choose between three color palettes for portergeist.art.

## How to Use
1. Visit https://mdisturbed.github.io/portergeist-art/
2. Look for the floating button in the **bottom-right corner** labeled "Preview: Current"
3. **Click the button** to cycle through three theme options:
   - **Current** - The original dark theme with dark red (#8B0000) accent
   - **Bold Ink** - Modern electric theme with teal (#00d4aa) and magenta (#ff2e63)
   - **Traditional Flash** - Classic tattoo theme with burnt orange (#e85d04) and gold (#ffd000)
4. The selection **persists** across page refreshes (saved to localStorage)

## Theme Details

### Theme 1: Current (Default)
- **Background:** Pure black (#0a0a0a)
- **Accent:** Dark red (#8B0000)
- **Vibe:** Original, gothic, mysterious
- **Best for:** Keeping existing brand recognition

### Theme 2: Bold Ink
- **Background:** Dark charcoal (#1a1a2e), NOT pure black
- **Primary Accent:** Teal (#00d4aa)
- **Secondary Accent:** Magenta/hot pink (#ff2e63)
- **Text:** Light gray (#e0e0e0)
- **Vibe:** Modern, electric, high-contrast, energetic
- **Best for:** Standing out, modern tattoo culture, Gen Z appeal

### Theme 3: Traditional Flash
- **Background:** Dark warm brown (#1c1a17)
- **Primary Accent:** Burnt orange (#e85d04)
- **Secondary Accent:** Gold (#ffd000)
- **Text:** Warm white (#f5f0e8)
- **Vibe:** Classic tattoo culture, bold but timeless, warm
- **Best for:** Traditional tattoo heritage, classic americana feel

## Mobile Testing
✅ The switcher is responsive and works on mobile devices (where Chance will likely view it)

## What Doesn't Change
- Layout, structure, navigation
- Content, copy, images
- Portfolio and flash galleries
- Forms and functionality
- **Only the color palette changes**

## After Chance Chooses
Once the final palette is selected, we will:

1. **Keep** the chosen theme's CSS variables as the new default
2. **Remove** the theme switcher button from the UI
3. **Delete** the unused theme CSS variants
4. **Clean up** the localStorage code

This is a **temporary preview tool** - designed to be easily removed once a decision is made.

## Technical Details
- **Implementation:** CSS custom properties (CSS variables)
- **Persistence:** localStorage (survives page refresh)
- **Files Modified:**
  - `styles.css` - Added theme variants + switcher styles
  - `script.js` - Added theme toggle logic + localStorage
  - `index.html` - Added switcher button

## GitHub
- **PR:** https://github.com/mdisturbed/portergeist-art/pull/2
- **Status:** ✅ MERGED (March 13, 2026)
- **Branch:** feature/palette-preview (deleted after merge)

## Deployment
GitHub Pages auto-deploys from main branch. Changes are live at:
**https://mdisturbed.github.io/portergeist-art/**

---

**Built for:** Chance Porter (Portergeist Art)  
**Purpose:** Client preview for final palette selection  
**Status:** Live and ready for review
