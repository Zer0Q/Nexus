# Voice Activation Assistant

## Definition
Always-on voice interface combining local wake word detection, local speech-to-text transcription, LLM reasoning with persona, and neural text-to-speech output. The entire pipeline runs on a single machine except for the LLM reasoning step, which can be local or cloud-based.

## Why It Matters
Voice interfaces remove the friction of typing and enable hands-free interaction with AI. When combined with a persistent persona and conversation history, the assistant becomes an always-available operator rather than a chat window you open and close.

## Key Ideas
- Five-component pipeline: wake word detection (openWakeWord) → transcription (faster-whisper) → reasoning (Claude/local LLM) → TTS (edge-tts) → audio playback (pygame)
- openWakeWord ships with pre-trained "hey jarvis" model — no training needed
- faster-whisper base model runs on CPU with int8 quantization (~150 MB download)
- Voice tuning: `en-GB-ThomasNeural` with `rate="-8%"` and `pitch="-6Hz"` for calm British operator voice
- Costs ~$4/month on Anthropic API (max_tokens=300 keeps exchanges cheap)
- Conversation history carried in a Python list — remembers context within the session
- Edge case: the real value is integrating with calendars, codebases, and inboxes — voice is just the interface

## Tradeoffs
- Cloud-based reasoning (Anthropic API) means voice transcripts leave the machine
- No persistent memory across sessions — restart the script and history is lost
- Noise sensitivity: wake word detection degrades in noisy environments
- Single-file implementation lacks error recovery, logging, and production-grade reliability

## Related
- [[concepts/Persona-Prompting]]
- [[concepts/Local-LLM]]
- [[concepts/Edge-TTS]]

## Source
[[summaries/0xChaseTM-How-to-Build-Your-Own-JARVIS]]
