# DESIGN.md: HealthyBite AI Direction

## Design Read
Reading this as: Educational Knowledge Representation web application for students, educators, and health-conscious eaters, in an editorial botanical and transparent scientific style, dial ENERGY 2 / RHYTHM 2 / MOTION 1.

## Dials
- **ENERGY: 2 (Balanced)**. Focused, warm, and credible. Not flat or sterile, but free of noisy neon gimmicks and gradient orbs.
- **RHYTHM: 2 (Structured with Intentional Breaks)**. Sidebar input controls flow into clear focal summary metrics, structured meal recommendation cards, and expandable rule explanations.
- **MOTION: 1 (Calm)**. Subtle interactive state feedback on buttons, cards, and tabs. No auto-looping pulses, no floating elements, no distracting entrance animations.

## Identity & Voice
- **Identity**: HealthyBite AI is a deterministic, explainable nutritional recommendation system driven by Knowledge Representation (Rule-Based Reasoning + Semantic Network).
- **Personality**: Transparent, informative, grounded, and medically humble (always clear that data is illustrative, not clinical advice).
- **Tone**: Human, natural, concise Indonesian language without AI marketing buzzwords (no "revolusioner", "seamless", "next-generation") and strictly avoiding em dashes (U+2014).

## Color Palette (WCAG AA Compliant)
- **Primary Brand**: Deep Forest Green (`#124838`)
  - Light mode: Used for hero titles, badges, and primary actions. Contrast ratio on white: 9.8:1 (Pass AAA).
  - Dark mode complement: Sage Tint (`#6ee7b7`) for text on dark backgrounds.
- **Surface / Background**:
  - Light Mode: Warm Crisp Ivory (`#fafbf9`) with card backgrounds (`#ffffff`), subtle borders (`#d1d5db`).
  - Dark Mode: Deep Moss Slate (`#111815`) with card backgrounds (`#1a2420`), subtle borders (`#2d3a33`).
- **Accent**: Warm Terracotta / Amber (`#b45309`)
  - Used strictly at key moments: allergen tags, dietary warnings, and rule constraint triggers. Contrast on white: 5.1:1 (Pass AA).
- **Neutrals**:
  - Primary text: `#111827` (light) / `#f3f4f6` (dark).
  - Secondary text: `#374151` (light) / `#9ca3af` (dark), verified >= 4.5:1.

## Typography
- System font stack prioritizing native readability: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
- Scale: Hero H1 (2.2rem), Section H2 (1.5rem), Card H3 (1.15rem), Body (0.95rem), Metadata (0.85rem).
- No uppercase labels with wide tracking; no artificial monospace headers.

## Responsive & Accessible Layout
- Fluid multi-state reflow: Single column on mobile (< 640px), two columns on tablet (640px - 1024px), wide view on desktop (> 1024px).
- Minimum tap target: 44px for buttons, select controls, and interactive elements.
- Clear `:focus-visible` styling with 3:1 contrast against adjacent background.
- Real states: Always provide rich empty state, loading indicator, and explicit allergen conflict explanations.
