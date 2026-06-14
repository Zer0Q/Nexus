---
title: "How to Build Your Own J.A.R.V.I.S (Full Guide)"
source: "https://x.com/0xChaseTM/status/2065047339929047357"
author:
  - "[[@0xChaseTM]]"
published: 2026-06-11
created: 2026-06-14
description: "Tony Stark spent billions on JARVIS. You'll spend $4 a monthYou've been carrying Claude in your pocket for months - asking it the same obvio..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HKiFPXjXYAEErFp?format=jpg&name=large)

**Tony Stark spent billions on JARVIS. You'll spend $4 a month**

You've been carrying Claude in your pocket for months - asking it the same obvious questions as everyone else. Today you build the one you always wanted

Say "Hey Jarvis" from across the room and it answers. Ask it to push your code, clean up your downloads folder, or read you the one message that actually matters - it does it, then tells you when it's done.Always on. Always one word away

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2064760010702274561/img/YARxTWKPYMQcbcYg?format=jpg&name=large)

0:06

**Five steps. 30 minutes. Full script down below - copy, paste, run**

# Step 1 - Get The Keys

## The whole build is one file: jarvis.py

Three parts go into it - a brain, ears, and a voice - one per step, until Step 5 wires them together and runs it. Only the brain needs a key. The other two are free.

**The brain - Anthropic.** Go to [console.anthropic.com](https://console.anthropic.com/) → sign up → load ~$10 of credit → copy an API key. This is Claude, the part that thinks. That $10 is about two months of JARVIS - more on why it's this cheap below

![Imatge](https://pbs.twimg.com/media/HKdKWUJWQAAPAqR?format=jpg&name=large)

![Imatge](https://pbs.twimg.com/media/HKdKaVNW8AAsVDU?format=jpg&name=large)

**The ears - free.** Go to openWakeWord listens for "Hey Jarvis" on your machine - no account, no key, and the model ships inside the library. Nothing about your room leaves the laptop until you've spoken

**The voice - free.** No account, no key. A library called edge-tts gives you Microsoft's neural voices - including a calm British one that sounds like the operator from the film. It installs in Step 4

## The math:

**You pay for one thing:** the thinking. The ears run on your machine, the voice is free, and Claude charges pennies per exchange because JARVIS keeps its answers short. A few dozen commands a day comes to about $4 a month - so $10 of prepaid credit lasts two. On pay-as-you-go that balance is a hard ceiling: it can't cost you a cent more than you load

# Step 2 - Give It Ears

Two pieces make the ear. openWakeWord listens for the phrase "Hey Jarvis." Whisper turns the next five seconds into text. Both run on your machine - nothing leaves the room until you've actually spoken

## Install the tools:

```bash
pip install "openwakeword==0.4.0" pvrecorder faster-whisper anthropic edge-tts numpy pygame onnxruntime
```

Now the ear. The "hey jarvis" model ships inside openWakeWord - no training, no download, it just works:

```python
import numpy as np, openwakeword
from openwakeword.model import Model
from pvrecorder import PvRecorder
from faster_whisper import WhisperModel

JARVIS   = [p for p in openwakeword.get_pretrained_model_paths() if "hey_jarvis" in p][0]
oww      = Model(wakeword_model_paths=[JARVIS])
recorder = PvRecorder(frame_length=1280)      # 80 ms @ 16 kHz
whisper  = WhisperModel("base", device="cpu", compute_type="int8")
recorder.start()

def hear():
    oww.reset()
    while max(oww.predict(np.array(recorder.read(), dtype=np.int16)).values()) < 0.5:
        pass                                  # idle until "Hey Jarvis"
    frames = []
    for _ in range(62):                       # ~5 seconds
        frames.extend(recorder.read())
    audio = np.array(frames, dtype=np.float32) / 32768.0
    segments, _ = whisper.transcribe(audio, language="en")
    return " ".join(s.text for s in segments).strip()
```

First run downloads the Whisper model once (~150 MB) - that's the extra ten minutes. After that it loads in seconds. Keep it on base: bigger models are slower, and you're transcribing one sentence, not a podcast.

It can hear you now. It just has nothing to say back yet

# Step 3 - Give It a Brain

This is the part everyone thinks is hard. **It isn't**

You hand Claude the transcribed text and one thing that matters more than which model you pick: a persona. The persona turns a helpful assistant into JARVIS - terse, certain, allergic to filler

```python
from anthropic import Anthropic
claude = Anthropic(api_key=ANTHROPIC_API_KEY)

PERSONA = """You are JARVIS. You run my day. You are not a chatbot.
- Talk like a calm operator. One breath. No filler.
- Never open with "Certainly" or "Great question."
- Default to action. Report results, not intentions.
- When I'm wrong, say so in one line."""

def think(history):
    reply = claude.messages.create(
        model="claude-sonnet-4-6",     # fast + smart; the sweet spot for voice
        max_tokens=300,
        system=PERSONA,
        messages=history,
    )
    return reply.content[0].text
```

Swap claude-sonnet-4-6 for claude-haiku-4-5 (cheaper, faster) or claude-opus-4-8 (smarter). The history list carries the conversation - so it remembers what you said thirty seconds ago, not just the last line

A generic assistant answers your question. A persona answers like someone who works for you

# Step 4 - Give It a Voice

Text is where most assistants stop. JARVIS speaks.

You send Claude's reply to edge-tts and it comes back as speech in one of Microsoft's neural voices - free, no key. The voice that sells it isn't the loudest, it's the calmest: en-GB-ThomasNeural, slowed a little and pitched down, lands right next to the operator from the film

```python
import asyncio, edge_tts, pygame

pygame.mixer.init()
VOICE = "en-GB-ThomasNeural"   # calm British; swap for en-GB-RyanNeural if you like

async def _render(text):
    tts = edge_tts.Communicate(text, VOICE, rate="-8%", pitch="-6Hz")
    await tts.save("reply.mp3")

def speak(text):
    asyncio.run(_render(text))
    pygame.mixer.music.load("reply.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
```

The trick is two settings - rate="-8%" and pitch="-6Hz". Without them you have British text-to-speech. With them you have JARVIS. Push them further if you want it slower and graver

# Step 5 - Wire It Together And Run

Ears, brain, voice. Now you close the loop. This is the whole thing - the entire JARVIS fits on one screen:

```python
import os, asyncio, numpy as np
import openwakeword, edge_tts, pygame
from openwakeword.model import Model
from pvrecorder import PvRecorder
from faster_whisper import WhisperModel
from anthropic import Anthropic

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
VOICE             = "en-GB-ThomasNeural"

PERSONA = """You are JARVIS. You run my day. You are not a chatbot.
- Talk like a calm operator. One breath. No filler.
- Never open with "Certainly" or "Great question."
- Default to action. Report results, not intentions.
- When I'm wrong, say so in one line."""

JARVIS   = [p for p in openwakeword.get_pretrained_model_paths() if "hey_jarvis" in p][0]
oww      = Model(wakeword_model_paths=[JARVIS])
recorder = PvRecorder(frame_length=1280)
whisper  = WhisperModel("base", device="cpu", compute_type="int8")
claude   = Anthropic(api_key=ANTHROPIC_API_KEY)
pygame.mixer.init()
history  = []

def hear():
    oww.reset()
    while max(oww.predict(np.array(recorder.read(), dtype=np.int16)).values()) < 0.5:
        pass
    frames = []
    for _ in range(62):
        frames.extend(recorder.read())
    audio = np.array(frames, dtype=np.float32) / 32768.0
    segments, _ = whisper.transcribe(audio, language="en")
    return " ".join(s.text for s in segments).strip()

def think(history):
    return claude.messages.create(
        model="claude-sonnet-4-6", max_tokens=300,
        system=PERSONA, messages=history,
    ).content[0].text

def speak(text):
    asyncio.run(edge_tts.Communicate(text, VOICE, rate="-8%", pitch="-6Hz").save("reply.mp3"))
    pygame.mixer.music.load("reply.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

print('JARVIS online. Say "Hey Jarvis".')
recorder.start()
try:
    while True:
        command = hear()
        if not command:
            continue
        print("You:", command)
        history.append({"role": "user", "content": command})
        reply = think(history)
        history.append({"role": "assistant", "content": reply})
        print("JARVIS:", reply)
        speak(reply)
except KeyboardInterrupt:
    print("Shutting down.")
finally:
    recorder.delete()
```

## Set your two keys and run it:

```bash
export ANTHROPIC_API_KEY="..."
python jarvis.py
```

Then say **"Hey Jarvis."** Wait for the beat. Talk. It hears you, thinks, and answers in the voice you gave it

Built-in mic and speakers both work. To keep it always-on, leave the script running or add it to your login items. The most expensive assistant in fiction now runs in a terminal window you never close

# Building it is the trivial part

**The value is in what comes next:**

Connected to your calendar, your codebase, your inbox, a voice assistant becomes an interface to your entire workflow. Most people will stop at conversation. The edge belongs to whoever integrates it first