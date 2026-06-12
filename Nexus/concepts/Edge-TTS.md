# Edge TTS

## Definition
Free Microsoft neural text-to-speech synthesis via the edge-tts Python library, requiring no API key or account. Provides access to Microsoft's neural voices with tunable rate and pitch parameters for voice customization.

## Why It Matters
Edge-tts eliminates the cost barrier for voice output in AI assistants. Combined with local wake word detection and transcription, it enables a fully functional voice interface where the only cloud dependency is the LLM reasoning step.

## Key Ideas
- No API key, no account, no cost — installs via pip
- Access to Microsoft's full neural voice catalog (e.g., en-GB-ThomasNeural for calm British operator)
- Voice tuning: `rate="-8%"` (slower) and `pitch="-6Hz"` (lower) transform standard TTS into character voices
- Async API: `edge_tts.Communicate(text, voice, rate, pitch).save("output.mp3")`
- Output is standard MP3 — plays back with any audio library (pygame, etc.)

## Tradeoffs
- Requires internet connection to Microsoft's edge TTS service — not truly local
- Rate limits may apply under heavy usage
- Voice quality depends on Microsoft's infrastructure — no control over service availability

## Related
- [[concepts/Voice-Activation-Assistant]]
- [[concepts/Local-LLM]]

## Source
[[summaries/0xChaseTM-How-to-Build-Your-Own-JARVIS]]
