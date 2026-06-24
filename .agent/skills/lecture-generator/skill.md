---
name: lecture-generator
description: Creates a complete lecture package on measure theory — slides, narrated video, and interactive animation — for graduate students and undergraduate math majors with no real analysis background. Coordinates marp-slides-measure, lecture-video-measure, and html-animation-measure skills.
allowed-tools: shell
---

# Lecture Generator: Measure and Measurable Functions

You are creating a complete lecture package on measure theory and measurable functions for graduate students and undergraduate math majors with NO real analysis background.

## Target Audience
Graduate students and undergraduate math majors. They are mathematically mature but have NOT taken real analysis. They know calculus, linear algebra, and basic set theory (unions, intersections, complements). They need rigorous definitions but with clear motivation and intuition first.

## Skills to Coordinate

You will coordinate the following three skills in sequence:

1. **marp-slides-measure**: Generate a Marp slide deck (10-12 slides) with:
   - Intuition first (length, area, volume, probability)
   - Formal definitions: outer measure, Lebesgue measure, measurable sets (Carathéodory), measurable functions
   - Concrete examples: measure of [0,1] = 1, measure of Q ∩ [0,1] = 0
   - Connection to probability: random variables = measurable functions
   - Title slide with `<!-- _class: lead -->`
   - Summary slide at the end

2. **lecture-video-measure**: Generate a narrated Remotion video using edge-tts based on the slide content:
   - 7 scenes (title, motivation, measure definition, formal definitions, measurable functions, probability connection, summary)
   - 1920×1080 at 30fps
   - White background, dark blue text (#003057)
   - Fade transitions
   - Audio: edge-tts voice "en-US-AriaNeural"
   - Total duration: ~110 seconds

3. **html-animation-measure**: Generate a self-contained interactive HTML animation for the most visually compelling concept:
   - Canvas-based drawing
   - At least one interactive control (slider or button)
   - Real-time numerical updates
   - Clean, academic layout

## Process

1. Start by generating the slides using `marp-slides-measure` with the topic and audience.
2. Use the slide content to inform the narration script for `lecture-video-measure`.
3. Generate the HTML animation for the most visually compelling concept using `html-animation-measure`.
4. Output a brief integration note explaining how all three pieces fit together as a teaching package.

## Final Output

After all three are produced, output:
1. The complete slide deck
2. The video generation code and instructions
3. The HTML animation file
4. A brief integration note explaining how the slides, video, and animation work together

Topic and audience: {{input}}