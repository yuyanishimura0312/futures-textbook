# Design Consistency Report: 未来を読む力 Textbook (20 Chapters)

**Report Date:** 2026-04-26  
**Audited:** All 20 chapters (ch01.html through ch20.html)

---

## Executive Summary

**Critical Issue Found:** Chapters 1-7 use a **fundamentally different architecture** from chapters 8-20.

- **Chapters 1-7:** Mixed CSS approaches with inline styles in some chapters
- **Chapters 8-20:** Consistent external CSS with centralized styling

This creates two distinct design systems within the same textbook, compromising visual and functional consistency.

---

## 1. Navigation Elements (Dark Mode Toggle & Print Button)

### Status: ✓ CONSISTENT across all chapters
All 20 chapters have:
- Dark mode toggle button (`theme-toggle-btn`)
- Print / PDF button (`btn-print`)
- Properly implemented in navigation bar

**Navigation Structure Inconsistency:**
- **Ch 1:** Basic navigation (목차へ戻る + ch02へ link)
- **Ch 2-7:** Styled `.chapter-nav` with `.nav-link` class and detailed labels (前章/次章)
- **Ch 8-20:** Simplified `.chapter-nav` with plain text links (← 第Xチャプター)

→ **Fix needed:** Normalize navigation styling and structure across all chapters.

---

## 2. CSS Architecture

### CRITICAL INCONSISTENCY

**Chapters 1 & 8-20:**
```html
<link rel="stylesheet" href="../assets/css/textbook.css">
<link rel="stylesheet" href="../assets/css/print.css" media="print">
```
✓ External CSS files (scalable, maintainable)

**Chapters 2-7:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP...">
<style>
  [root CSS variables and extensive inline styles]
</style>
```
✗ Inline `<style>` tags (harder to maintain, redundant code across 6 files)

→ **Requires consolidation:** Chapters 2-7 should use external CSS files like the rest.

---

## 3. Google Fonts

### Status: INCONSISTENT

**Chapters 2-7:** Explicitly import Google Fonts
- `Noto Serif JP` (weights: 400, 700)
- `Noto Sans JP` (weights: 300, 400, 500, 700)

**Chapters 1 & 8-20:** No explicit Google Fonts import in HTML
- Presumed to be loaded via `../assets/css/textbook.css`

→ **Issue:** Chapter 1 and 8-20 may not display fonts if external CSS fails to load Google Fonts reference.

---

## 4. Color Scheme

### Status: PARTIALLY CONSISTENT

**Primary Colors Used:**
- `#7A4033` (darker brown) - SVGs in chapters 1, 8-20
- `#8B6914` (warm brown) - CSS variable `--primary` in chapters 2-7
- `#D4A84B` (gold/warm accent) - CSS variable `--secondary` in chapters 2-7

**Color Usage:**
- Chapters 1-20 all use the same color palette (brown + gold)
- Colors are correctly applied to SVG diagrams and text elements
- Dark mode color shifts implemented consistently

→ **Minor issue:** Two different primary brown values (#7A4033 vs #8B6914) are used. Should unify to one canonical value.

---

## 5. SVG Diagrams

### Status: ✓ ALL CHAPTERS HAVE SVGS

| Chapter | SVG Count | Content |
|---------|-----------|---------|
| Ch 01   | 3         | Forecasting vs Foresight diagram |
| Ch 02   | 2         | Futures matrix diagrams |
| Ch 03   | 2         | Scenario planning structure |
| Ch 04   | 2         | Environmental scanning framework |
| Ch 05   | 3         | Scenario planning process steps |
| Ch 06   | 1         | Delphi method flow |
| Ch 07   | 3         | Systems thinking visualization |
| Ch 08-20| 1 each    | Chapter-specific thematic diagrams |

**Observation:** Chapters 1-7 have more SVGs (average 2.4 per chapter) vs chapters 8-20 (1 per chapter). This may reflect different design priorities.

→ **Consistency note:** SVG presence is universal, but density varies. Intentional or needs standardization?

---

## 6. Print CSS (@media print)

### Status: MIXED

**Chapters 1 & 8-20:**
- External file: `../assets/css/print.css` with `media="print"` attribute
- ✓ Recommended approach

**Chapters 2-7:**
- Inline print styles within `<style>` tag
- `@media print { ... }` rules embedded
- ✗ Harder to audit and maintain

→ **All print styles should be consolidated in `../assets/css/print.css`.**

---

## 7. Header Structure

### Status: ✓ CONSISTENT

All chapters follow the same header pattern:
```html
<header class="chapter-header">
  <span class="chapter-number">Chapter XX</span>
  <h1 class="chapter-title">タイトル</h1>
  <p class="chapter-subtitle">サブタイトル</p>
</header>
```

Variations by chapter group:
- **Ch 1 & 8-20:** Use `.chapter-header` class
- **Ch 2-7:** Use `.chapter-hero` class (different styling, more elaborate)

→ **Minor fix:** Class naming inconsistency (`chapter-header` vs `chapter-hero`). Consider standardizing.

---

## 8. Dark Mode Implementation

### Status: ✓ CONSISTENT across all chapters

All 20 chapters implement dark mode identically:
- HTML tag: `<html lang="ja" data-theme="light">`
- Toggle function: `toggleTheme()` reads/writes to `data-theme` attribute
- localStorage support: Theme preference persists across sessions
- CSS variables: Both chapter groups use `[data-theme="dark"]` selectors

→ ✓ No issues here. Dark mode is well-implemented.

---

## Summary of Issues by Severity

### CRITICAL (Visual/Functional Impact)
1. **Ch 1-7 vs 8-20 CSS Architecture Split**
   - Chapters 2-7 have inline styles; rest use external CSS
   - Creates maintenance burden and potential CSS conflicts
   - **Fix:** Move all inline styles from ch02-07 into `../assets/css/textbook.css`

2. **Google Fonts Import Inconsistency**
   - Chapters 2-7 explicitly import; chapters 1, 8-20 do not
   - **Fix:** Ensure all chapters load fonts via centralized CSS file

### MAJOR (Consistency/Maintenance)
3. **Navigation Styling Inconsistency**
   - Ch 2-7 have styled nav elements with labels; ch 8-20 have plain text
   - **Fix:** Standardize navigation structure and CSS across all chapters

4. **Color Value Duplication**
   - `#7A4033` (ch 1, 8-20 SVGs) vs `#8B6914` (ch 2-7 CSS)
   - **Fix:** Define canonical brown color and use globally

### MINOR (Non-critical)
5. **Header Class Naming**
   - Ch 2-7 use `.chapter-hero`; ch 1, 8-20 use `.chapter-header`
   - **Fix:** Unify to single class name

---

## Recommended Action Plan

### Phase 1: Audit External CSS Files (Prerequisite)
- [ ] Review `/assets/css/textbook.css` structure
- [ ] Review `/assets/css/print.css` coverage
- [ ] Check Google Fonts reference in external CSS

### Phase 2: Consolidate Inline Styles
- [ ] Extract all `<style>` blocks from ch02-07.html
- [ ] Merge with `textbook.css`, using CSS variables for chapter-specific overrides if needed
- [ ] Remove inline `<style>` tags from chapters 2-7
- [ ] Verify layout/appearance unchanged

### Phase 3: Standardize Navigation
- [ ] Decide on final navigation structure (simple or detailed labels)
- [ ] Update all chapters to use consistent `.chapter-nav` styling
- [ ] Test prev/next links on all 20 chapters

### Phase 4: Unify Color System
- [ ] Define canonical color palette (choose between #7A4033 and #8B6914)
- [ ] Update all SVG diagrams and CSS variables
- [ ] Add color token documentation to external CSS

### Phase 5: Normalize Header Markup
- [ ] Rename all `.chapter-hero` to `.chapter-header` (or vice versa)
- [ ] Ensure consistent class names across all 20 chapters

### Phase 6: Validation
- [ ] Test dark mode toggle on all 20 chapters
- [ ] Test print functionality on all 20 chapters
- [ ] Verify responsive design (mobile/tablet/desktop)
- [ ] Cross-browser testing (Safari, Chrome, Firefox)

---

## Files That Will Require Changes

**HTML files (ch02-07):**
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch02.html`
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch03.html`
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch04.html`
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch05.html`
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch06.html`
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch07.html`

**HTML files (ALL, for navigation/header standardization):**
- `/Users/nishimura+/projects/apps/futures-textbook/chapters/ch01-20.html` (all)

**CSS files to be created/updated:**
- `/Users/nishimura+/projects/apps/futures-textbook/assets/css/textbook.css`
- `/Users/nishimura+/projects/apps/futures-textbook/assets/css/print.css`

---

## Conclusion

The textbook has **solid dark mode and print functionality**, but suffers from a **two-tier CSS architecture** that splits maintenance effort between inline styles (ch 2-7) and external CSS (ch 1, 8-20). This is the highest priority issue to resolve.

Once consolidated, the textbook will have a clean, maintainable design system that is easy to update globally and scale to future chapters.
