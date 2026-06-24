---
name: lecture-video-measure
description: Generates a narrated Remotion video for a measure theory lecture using edge-tts. Use when asked to create a narrated video, lecture video, or animated math video on measure theory.
allowed-tools: shell
---

# Lecture Video: Measure and Measurable Functions

Using Remotion and edge-tts, generate a complete narrated math lecture video on measure theory for graduate students and undergraduate math majors with NO real analysis background.

## Target Audience
Graduate students and undergraduate math majors. They know calculus, linear algebra, and basic set theory but have NOT taken real analysis.

## Video Structure
- Scene 1 (0-8s): Title card
- Scene 2 (8-25s): Motivation (Riemann integral limitations, Dirichlet function)
- Scene 3 (25-45s): What is measure? (length, area, volume, probability)
- Scene 4 (45-65s): Formal definitions (outer measure, Lebesgue measure)
- Scene 5 (65-80s): Measurable functions
- Scene 6 (80-95s): Connection to probability (random variables)
- Scene 7 (95-110s): Summary

## Technical Requirements
- 1920×1080 at 30fps
- White background, dark blue text (#003057)
- Fade transitions
- Audio: edge-tts voice "en-US-AriaNeural"
- Total duration: ~110 seconds
- Single React component using Remotion

Topic: {{input}}