# Design System Reference

This document provides a design system reference for creating prototypes and mockups that match your product's visual design. Fill it in once you have access to the company's design system.

> **Setup required:** Replace all `[FILL IN: ...]` placeholders with your company's design system details.
> Run `/setup` for guided onboarding.

---

## Component Library

**[FILL IN: component library name, e.g. "MUI", "Ant Design", "PrimeVue", "Custom"]**

- **Documentation**: [FILL IN: link to component library docs]
- **Framework**: [FILL IN: e.g. "React 18 + MUI v5", "Vue 3 + PrimeVue"]
- **Styling**: [FILL IN: e.g. "Custom theme built on top of MUI defaults", "Tailwind CSS"]

When building prototypes:
1. Use [FILL IN: component library] components where applicable
2. Apply the custom color palette (documented below)
3. Match the spacing, typography, and styling patterns shown in this guide
4. Reference the component library API for proper implementation

---

## Table of Contents

1. [Color Palette](#color-palette)
2. [Typography](#typography)
3. [Components](#components)
4. [Spacing & Layout](#spacing--layout)
5. [Shadows & Borders](#shadows--borders)
6. [Forms & Inputs](#forms--inputs)
7. [Buttons](#buttons)
8. [Navigation](#navigation)

---

## Color Palette

> **Setup:** Extract these values from your company's Figma file or design system documentation.

### Primary Colors
- `primary`: [FILL IN: hex, main brand color]
- `primary-dark`: [FILL IN: hex, hover/pressed state]
- `primary-light`: [FILL IN: hex, backgrounds, highlights]

### Secondary/Accent Colors
- `accent`: [FILL IN: hex]
- `success`: [FILL IN: hex]
- `warning`: [FILL IN: hex]
- `error`: [FILL IN: hex]

### Neutral Colors
- `text-primary`: [FILL IN: hex]
- `text-secondary`: [FILL IN: hex]
- `text-disabled`: [FILL IN: hex]
- `bg-primary`: [FILL IN: hex, main background]
- `bg-secondary`: [FILL IN: hex, cards, panels]
- `border`: [FILL IN: hex]

### Dark Mode (if applicable)
- `bg-primary-dark`: [FILL IN: hex]
- `bg-secondary-dark`: [FILL IN: hex]
- `text-primary-dark`: [FILL IN: hex]
- `text-secondary-dark`: [FILL IN: hex]

---

## Typography

**Font Family:**
- Primary: [FILL IN: e.g. "Inter, -apple-system, sans-serif"]
- Monospace: [FILL IN: e.g. "SF Mono, Monaco, monospace"]

**Font Sizes:**
```
xs:   [FILL IN]px   /* Small labels, captions */
sm:   [FILL IN]px   /* Secondary text */
base: [FILL IN]px   /* Body text */
lg:   [FILL IN]px   /* Section headers */
xl:   [FILL IN]px   /* Modal titles */
2xl:  [FILL IN]px   /* Page headers */
```

**Font Weights:**
- Regular: 400 (body text)
- Medium: 500 (labels)
- Semibold: 600 (buttons, headers)
- Bold: 700 (emphasis)

---

## Components

### Avatars
- Small: [FILL IN]px × [FILL IN]px
- Medium: [FILL IN]px × [FILL IN]px
- Large: [FILL IN]px × [FILL IN]px
- Style: [FILL IN: rounded / square / circle]

### Status Indicators
- [FILL IN: status color 1 and meaning, e.g. "Green = Online/Active"]
- [FILL IN: status color 2 and meaning, e.g. "Red = Error/Offline"]
- [FILL IN: status color 3 and meaning, e.g. "Orange = Warning/Pending"]

---

## Spacing & Layout

**Base unit:** [FILL IN: e.g. "4px (Tailwind scale)"]

**Layout Structure:**
```
[FILL IN: describe your app's main layout, e.g. sidebar + main content, header + body]
```

**Common Patterns:**
- Component padding: [FILL IN]px
- Section spacing: [FILL IN]px
- Card padding: [FILL IN]px
- Modal padding: [FILL IN]px

---

## Shadows & Borders

**Border Widths:**
- Default: [FILL IN]px
- Thick: [FILL IN]px

**Border Colors:**
- Light mode: [FILL IN: hex]
- Dark mode: [FILL IN: hex]

**Border Radius:**
- Small (buttons, pills): [FILL IN]px
- Medium (inputs, cards): [FILL IN]px
- Large (modals): [FILL IN]px
- Full (circles, badges): 9999px

**Card Shadow:**
```css
box-shadow: [FILL IN];
```

**Modal Shadow:**
```css
box-shadow: [FILL IN];
```

---

## Forms & Inputs

**Text Input:**
```css
/* Light mode */
background: [FILL IN]
border: 1px solid [FILL IN]
border-radius: [FILL IN]px
padding: [FILL IN]px
color: [FILL IN]
font-size: [FILL IN]px

/* Focus State */
border-color: [FILL IN, primary color]
box-shadow: [FILL IN]
```

---

## Buttons

### Primary Button
```css
background: [FILL IN, primary color]
color: [FILL IN, usually white]
padding: [FILL IN]px [FILL IN]px
border-radius: [FILL IN]px
font-size: [FILL IN]px
font-weight: [FILL IN]

/* Hover */
background: [FILL IN, slightly darker]

/* Disabled */
background: [FILL IN, muted]
opacity: 0.5
```

### Secondary Button
```css
background: transparent
color: [FILL IN]
border: 1px solid [FILL IN]
/* ... */
```

### Destructive Button
```css
background: [FILL IN, error/red color]
color: white
/* ... */
```

---

## Navigation

**Sidebar/Nav Width:** [FILL IN]px

**Nav Item States:**
```css
/* Default */
color: [FILL IN]

/* Hover */
background: [FILL IN]
color: [FILL IN]

/* Active/Selected */
background: [FILL IN, primary]
color: white
```

---

## Implementation Notes

### Framework & Library Setup
[FILL IN: notes on how to set up the component library in a new project, npm install commands, provider setup, theme configuration]

### Prototype Structure
```
components/
├── ui/          [FILL IN: base UI components]
├── features/    [FILL IN: feature-specific components]
└── layout/      [FILL IN: layout components]
```

### Accessibility
- Ensure all components have proper ARIA labels
- Support keyboard navigation
- Meet WCAG 2.1 AA contrast ratios
- Include focus indicators

---

## Resources

**Design Files:**
- Figma: [FILL IN: link to main Figma file]
- Storybook: [FILL IN: link to Storybook, if available]

**Component Library:**
- [FILL IN: component library name]: [FILL IN: link to docs]

**Icon Library:**
- [FILL IN: icon library name]: [FILL IN: link]

**Framework:**
- [FILL IN: framework]: [FILL IN: link to docs]

---

## Version History

- **[FILL IN: date]**: Initial design system documentation created

---

*Fill in this document by referencing your company's Figma design files and component library documentation.*
