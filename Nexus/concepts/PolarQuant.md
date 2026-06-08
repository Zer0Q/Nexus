# PolarQuant

## Definition
Vector quantization method that converts Cartesian coordinates to polar coordinates (radius + angle), eliminating the need for data normalization and removing memory overhead from quantization constants. Presented at AISTATS 2026.

## Why It Matters
Traditional quantization requires storing full-precision quantization constants per data block (1-2 extra bits per number). PolarQuant maps data onto a fixed, predictable "circular" grid where boundaries are already known, eliminating this overhead entirely.

## Key Ideas
- Converts d-dimensional vectors to polar coordinates: radius (strength) + angle (direction/meaning)
- Recursive polar transformation: pairs of coordinates mapped to polar, radii gathered in pairs, repeats until single final radius + collection of angles
- Known angle distribution eliminates expensive data normalization step
- "Square" grid (Cartesian) has changing boundaries; "circular" grid (polar) has fixed boundaries
- Uses most of the compression power (majority of bits) to capture main vector concept and strength

## Tradeoffs
- Polar transformation adds encoding/decoding overhead
- Best suited for high-dimensional vectors where angle distributions concentrate
- Works as first stage of TurboQuant; standalone performance is slightly below the combined method

## Related
- [[concepts/TurboQuant]]
- [[concepts/QJL]]
- [[concepts/Vector-Quantization]]

## Source
[[summaries/google-TurboQuant-Extreme-KV-Compression]]
