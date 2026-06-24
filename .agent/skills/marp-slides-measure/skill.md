---
name: marp-slides-measure
description: Generates a Marp slide deck on measure theory and measurable functions for graduate students and undergraduate math majors with no real analysis background. Use when asked to create slides on measure theory, Lebesgue measure, or measurable functions.
allowed-tools: shell
---

# Marp Slides: Measure and Measurable Functions

You are creating a Marp slide deck on measure theory and measurable functions for graduate students and undergraduate math majors with NO real analysis background.

## Target Audience
Graduate students and undergraduate math majors. They are mathematically mature but have NOT taken real analysis. They know calculus, linear algebra, and basic set theory.

## Requirements
- Minimum 10-12 slides
- Start with intuition (length, area, volume, probability) → build to formal definitions
- Explain why measure theory is needed (limitations of Riemann integral)
- Include formal definitions: outer measure, Lebesgue measure, measurable sets (Carathéodory), measurable functions
- Include 4-5 display math equations using $$
- Concrete examples: measure of [0,1] = 1, measure of Q ∩ [0,1] = 0
- Connection to probability: random variables = measurable functions
- Title slide with <!-- _class: lead -->
- Summary slide at the end

## Frontmatter Template
```yaml
---
marp: true
theme: default
paginate: true
math: katex
---