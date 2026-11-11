---
name: Coastory
description: Visual system for the Coastory website
colors:
  coral: "#ff5436"
  coral-ink: "#c0351c"
  coral-hover: "#ff6d53"
  on-coral: "#241c16"
  cream: "#fff7f0"
  white: "#ffffff"
  plum-ink: "#2a2233"
  plum-soft: "#625669"
  teal-link: "#077483"
  tinted-band: "#fff1e6"
  night-ground: "#100b25"
  night-surface: "#1a1433"
typography:
  display:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontWeight: 600
    lineHeight: 1.04
  body:
    fontFamily: "Nunito, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Nunito, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 700
    lineHeight: 1.3
rounded:
  thumbnail: "6px"
  control: "8px"
  panel: "12px"
  device: "22px"
  pill: "999px"
components:
  button-primary:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.on-coral}"
    rounded: "{rounded.pill}"
    padding: "0.6rem 1.35rem"
  button-primary-hover:
    backgroundColor: "{colors.coral-hover}"
    textColor: "{colors.on-coral}"
  button-secondary:
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.pill}"
    padding: "0.6rem 1.35rem"
---

# Design System: Coastory

## Overview

The website uses the app's own cream, plum, coral, and teal palette and its two typefaces. Warm surfaces and a restrained editorial serif give the rider's history space; clear Nunito text keeps actions and details easy to scan. Real app captures carry the product imagery.

## Colors

- **Coral** is the action fill and selected-state accent. Its darker ink variant is used for text and focus outlines on light surfaces; dark ink sits on coral fills because white text does not meet the site's contrast target.
- **Cream and plum** form the light page and text. White panels and a tinted band separate content without heavy decoration. Dark mode changes the ground, surfaces, text, and link contrast through the existing CSS tokens.
- **Teal** is the app's factual accent; the darker link variant is used for readable links on cream.

## Typography

- **Fraunces** is the display face for page titles, section starts, feature headings, and large figures. The shared title scale runs from `clamp(2.5rem, 5.2vw, 3.75rem)`; `/get` uses a slightly larger local headline.
- **Nunito** carries body copy, labels, navigation, actions, and list names. The shared body role is `1rem/1.65`; metadata is smaller at `0.875rem/1.45`.

## Layout

The shared header and footer use a `1248px` maximum frame and a `1.25rem` gutter, rising to `1.5rem` at `41rem`. Landing content is narrower. The `/get` page keeps downloads before the real app preview in reading order, then places them in two columns from `48rem`.

## Elevation & Depth

Panels use tonal contrast and fine rules rather than shadows. The shared invitation is one raised surface with a border and panel radius.

## Shapes

Panels have a `12px` radius; controls use `8px`, thumbnails `6px`, and action buttons are pills. The `22px` device corner belongs to phone captures, not general cards.

## Components

- **Action buttons:** Coral fill with dark ink for the primary action; transparent outlined secondary action. Both have a `48px` minimum height, pill shape, and a short color transition.
- **Navigation:** Nunito links have a `44px` minimum height. The current item has a coral underline; the filled navigation action uses dark ink on coral.
- **Store choices:** Preserve the official badge artwork. The `/get` page places each badge in a large link target; the inferred matching platform receives a tinted background and coral border. Both choices remain available and equal when no platform is inferred.
- **Focus:** Keyboard focus uses a `3px` coral-ink outline with a `3px` offset. Store-link focus follows the panel radius.

## Do's and Don'ts

- **Do** use the existing CSS custom properties and self-hosted Nunito/Fraunces faces when extending the website.
- **Do** preserve real app captures and legible light and dark states.
- **Don't** put white text on the coral action fill or use the raw teal accent as small text on cream; the existing ink and link variants address contrast.
