---
title: "How to Create Custom Hermes Skins That Actually Look Good"
source: "https://x.com/NeoAIForecast/status/2041818820810351092"
author:
  - "[[@NeoAIForecast]]"
published: 2026-04-08
created: 2026-05-31
description: "Most people treat Hermes skins like a color swap. That is the fastest way to make a mediocre theme.A good Hermes skin is not just a palette...."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HFX5y8Ya8AELHNc?format=jpg&name=large)

Most people treat Hermes skins like a color swap. That is the fastest way to make a mediocre theme.

A good Hermes skin is not just a palette. It is a visual system: colors, spinner behavior, branding, tool output, and banner art all working together.

If you want to make custom Hermes skins well, here is the technical and practical guide.

Hermes has one of the cleaner CLI skin systems in open agent tooling right now.

That matters because most terminal theming systems fall into one of two traps: either they are too rigid to be fun, or so loose that every custom theme turns into visual chaos.

Hermes sits in a useful middle. It gives you a YAML-driven skin layer that can control:

- colors
- spinner faces
- spinner verbs
- branding text
- tool activity prefix
- per-tool emojis
- custom ASCII logo art
- custom hero art

And the key design choice is this: missing values inherit from the built-in default skin.

That one decision makes Hermes skins much easier to build and much harder to break.

Joey’s [@aijoey](https://x.com/@aijoey) Hermes skins repo is a very good reference for how to do this in practice: [https://github.com/joeynyc/hermes-skins](https://github.com/joeynyc/hermes-skins)

It complements the official Hermes skin docs really well because it shows not just the schema, but what polished skins actually look like.

## First, understand what a Hermes skin is

A Hermes skin only changes visual presentation. It does not change:

- personality
- system behavior
- tool logic
- prompting style

Official Hermes docs are explicit about this distinction: personality affects how Hermes speaks, skin affects how Hermes looks in the terminal.

That matters because a lot of people mix branding and behavior together.

A skin is UI. Not cognition.

That means your goal is not “make Hermes act cyberpunk.” It is “make the terminal experience feel visually coherent.”

**Takeaway:** Treat skins like interface design, not persona design.

## Where custom skins live

Hermes loads skins from two places:

1. Built-in skins inside Hermes
2. User skins in ~/.hermes/skins/<name>.yaml

User skins take priority over built-ins.

That means the basic workflow is simple:

- create a YAML file
- save it to ~/.hermes/skins/
- switch to it with /skin <name>

Example: /skin mytheme

Or make it permanent in ~/.hermes/config.yaml:

```yaml
display:
  skin: mytheme
```

This is one of the nicest parts of the system. The activation path is lightweight enough that you can iterate fast.

**Takeaway:** The fastest workflow is edit YAML > /skin name > inspect > adjust.

## The core architecture is inheritance

This is the most important thing to understand technically. Hermes skins inherit missing values from the built-in default skin.

In practice, this means you do not need to write a full theme unless you want full control.

**You can make:**

- a minimal skin with only a few color overrides
- a medium skin with custom branding and spinner verbs
- a full skin with custom Rich-markup ASCII banner art and per-tool emoji mapping

This inheritance model gives you three good design strategies.

**Strategy 1: Palette-only skin**

Change only colors. Keep default behavior, layout, and branding feel. Best for subtle personalization and matching a desktop color scheme.

**Strategy 2: Identity skin**

Change colors, spinner, and branding. Best for role-based themes or aesthetic skins like Joey’s Netrunner, Nous, or Skynet examples.

**Strategy 3: Full art-directed skin**

Change colors, spinner, branding, tool emojis, banner\_logo, and banner\_hero. Best for showcase skins, themed distributions, and repo-worthy skins you want to share publicly.

**Takeaway:** Do not start full-width unless you already know the visual identity you want.

## What you can actually customize

From the official schema and Joey’s template, the customization surface is broader than most people realize.

The main groups are:

1. **Colors** These control banner, prompt, labels, warnings, response borders, session labels, and more. Important keys: banner\_border, banner\_title, banner\_accent, ui\_accent, prompt, response\_border, etc.
2. **Spinner** This controls the animation personality of the CLI while Hermes is thinking. Keys: waiting\_faces, thinking\_faces, thinking\_verbs, wings. This is where a skin starts feeling alive.
3. **Branding** This controls text identity: agent\_name, welcome, goodbye, response\_label, prompt\_symbol, help\_header.
4. **Tool presentation** You can override: tool\_prefix, tool\_emojis. Per-tool emoji mapping helps the whole CLI feel more cohesive.
5. **Banner art**Y ou can replace: banner\_logo, banner\_hero. These support Rich console markup, colored ASCII art is possible directly in the YAML.

**Takeaway:** If your skin still feels generic after a color pass, branding, spinner and tool\_emojis are usually the missing layer.

## The biggest beginner mistake is overdesign

This is where most custom skins go wrong.

People discover the full schema and immediately try to customize everything: every color, every verb, every emoji, huge banners, complex gradients, novelty symbols everywhere.

The result is usually impressive for 15 seconds and tiring after 15 minutes.

Good skins are restrained. The official Hermes inheritance model is basically encouraging restraint.

Joey’s [repo](https://github.com/joeynyc/hermes-skins) shows this well too: the strongest skins are not random, they are tightly themed.

For example:

- Netrunner is coherent because the palette, verbs, symbols, and art all support one cyberpunk direction

![Imatge](https://pbs.twimg.com/media/HFX9I8Ya8AMpac_?format=jpg&name=large)

- Nous is coherent because it aligns palette and branding around a single Nous identity

![Imatge](https://pbs.twimg.com/media/HFX9DDLa8AA8kJt?format=png&name=large)

- Skynet works because the red/black palette, directive language, and machine branding all point the same way

![Imatge](https://pbs.twimg.com/media/HFX88-La8AIdP6Y?format=jpg&name=large)

The lesson is simple: pick one visual story and keep every layer aligned to it.

**Takeaway:** A skin should feel consistent before it feels clever.

## How to design a good skin, step by step

If I were making a custom Hermes skin from scratch, I would do it in this order:

1. **Define the identity** Answer: What is this skin supposed to feel like? (clean and serious, cyberpunk and sharp, mythic and ornate, etc.) If you cannot describe the identity in one sentence, the skin is not ready to design.
2. **Build the palette first** Start with banner\_border, banner\_title, banner\_accent, banner\_text, prompt, response\_border. Do not start with ASCII art. Start with readability.
3. **Add spinner language** Then choose faces, verbs, wings. Best practice: make spinner verbs match the world of the skin (e.g., cyberpunk: “breaching ICE”, research: “running inference”, mythic: “divining patterns”).
4. **Add branding carefully** Customize agent\_name, response\_label, prompt\_symbol, welcome/help text if needed. Do not make these too long or too gimmicky. You still need to live with the interface.
5. **Add tool emojis if the skin deserves them** Use them when they reinforce meaning. Not just because you can.
6. **Add banner\_logo and banner\_hero last** Only once the skin works as a UI should you add large art. Art is the easiest thing to overfit and the hardest thing to maintain.

**Takeaway:** The right order is identity > palette > spinner > branding > tool details > art.

## Joey’s repo is useful because it gives you examples, not just rules

[https://github.com/joeynyc/hermes-skins](https://github.com/joeynyc/hermes-skins)

The repo gives you:

- a README with install/activation workflow
- SCHEMA.md with the complete key reference
- template.yaml as a copy-paste starter
- multiple finished skins showing different aesthetic approaches

Three especially useful references:

- template.yaml for structure
- SCHEMA.md for what each field actually does
- polished skins like netrunner.yaml, nous.yaml, and skynet.yaml for theme logic

The important point is not to copy them blindly. It is to study how each one keeps visual language aligned.

**Takeaway:** Use Joey’s repo as a design reference set, not just a file library.

## Rich markup and ASCII art are powerful, but easy to abuse

Hermes supports Rich markup in banner\_logo, banner\_hero, welcome, and goodbye.

That means you can do colored text, bold sections, gradients, custom ASCII logos, and large hero illustrations.

This is one of the coolest parts of the skin system. It is also the part most likely to go wrong.

Best practices:

- keep banner art readable at terminal width
- make the color palette of the art match the rest of the skin
- avoid giant art blocks that dominate startup
- use gradients sparingly
- test on your actual terminal theme, not just in theory

Joey’s repo shows a useful pattern here: the best art is not “bigger,” it is better integrated into the theme identity.

**Takeaway:** Banner art should support the skin, not hijack it.

## Minimal skins are underrated

This is maybe the most important practical advice in the whole guide.

Because Hermes inherits from default, minimal skins are often better than full skins.

A minimal skin might only change:

- a few core colors
- one response label
- one prompt symbol
- maybe one or two spinner verbs

That can be enough.

Why minimal works: lower maintenance, less visual noise, fewer opportunities for awkward contrast, default Hermes layout remains familiar, easier to iterate.

**Takeaway:** A clean partial skin usually ages better than an overloaded full skin.

## Best resources

**Official Hermes references**

- Official skins docs: [https://hermes-agent.nousresearch.com/docs/user-guide/features/skins](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins)
- Hermes config docs ([display.skin](https://display.skin/))
- Hermes built-in skin definitions live in the source (skin\_engine.py)

**Joey’s repo**

- [https://github.com/joeynyc/hermes-skins](https://github.com/joeynyc/hermes-skins)
- README: great quickstart and examples
- SCHEMA.md: complete field reference
- template.yaml: best starting point
- skins/ folder: polished examples like netrunner, nous, skynet, sakura, pirate, and neonwave

**Suggested workflow**

1. Read official skins docs
2. Read Joey’s SCHEMA.md
3. Start from template.yaml
4. Build a minimal version first
5. Expand only if the identity still needs more

## Conclusion

Hermes skins are good because they are composable.

You can make a tiny skin that just improves your palette. Or a full art-directed theme with custom tool emojis, spinner language, and branded startup art.

But the best skins all follow the same rule: they feel designed, not merely decorated.

If you want your custom Hermes skin to look good in daily use: start small, stay coherent, and let inheritance do more work than your ego wants it to.