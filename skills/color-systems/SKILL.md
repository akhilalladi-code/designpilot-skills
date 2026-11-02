---
name: color-systems
description: Create practical, accessible color palettes and semantic color roles for brands and interfaces.
---

# Color Systems Skill

## Objective
Build a coherent palette that supports meaning, hierarchy, accessibility, and consistent application.

## Workflow
1. Gather brand context, audience, medium, existing colors, cultural considerations, and accessibility needs.
2. Define palette roles: primary, secondary, accent, background, surface, text, muted text, border, and status colors where needed.
3. Explain the purpose of each color; avoid palettes made only of attractive swatches.
4. Define usable combinations for text, icons, controls, and large areas.
5. Check contrast using a recognised contrast-ratio method. For WCAG 2.2 AA, target at least 4.5:1 for normal text and 3:1 for large text; check non-text UI contrast where applicable.
6. Test the palette in grayscale, low-quality displays, dark/light contexts, and common color-vision simulations when relevant.
7. Document tokens and usage rules.

## Token example
```css
:root {
  --color-brand-primary: #174B3A;
  --color-brand-accent: #E58A24;
  --color-surface: #FFFFFF;
  --color-text: #171717;
  --color-text-muted: #595959;
  --color-border: #D8D8D8;
}
```

Treat these values as illustrative only; calculate and validate combinations for the actual project.

## Quality checklist
- Each color has a defined role.
- Text combinations meet the chosen contrast target.
- Meaning is not communicated by color alone.
- Palette works across required media and backgrounds.
- Tokens are named by role rather than appearance.
- Brand constraints and cultural context are respected.

## Output format
Return palette swatches as HEX values, semantic roles, pairing guidance, contrast results (including tested foreground/background pairs), token names, and usage examples.

## Guardrails
Do not invent contrast scores. If no calculator or code execution is available, say that contrast still needs verification. Do not alter supplied brand colors without permission.