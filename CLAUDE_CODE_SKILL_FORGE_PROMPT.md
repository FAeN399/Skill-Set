# SKILL FORGE: Narrative-Driven Skill Ecosystem Generator

## Mission Brief for Claude Code

You are tasked with creating a GitHub repository that houses an interconnected ecosystem of Claude skills. This isn't just documentation—it's a **living narrative system** where users journey through an allegorical story world, learning practical real-world skills through immersive narrative progression.

---

## Repository Architecture

### Core Structure
```
skill-forge-narrative/
├── README.md (orientation & philosophy)
├── START_HERE.md (narrative entry point - CRITICAL)
├── skills/
│   ├── 00-foundation-prime/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/
│   ├── 01-skill-name/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   └── foundation-context.md (references foundation)
│   │   └── scripts/
│   ├── 02-skill-name/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── foundation-context.md
│   │   │   └── previous-skill-context.md
│   │   └── scripts/
│   └── ... (additional skills)
├── narrative/
│   ├── world-state.md (evolving story context)
│   ├── character-arcs.md (user's journey tracking)
│   └── stage-progressions.md (narrative checkpoints)
└── scripts/
    ├── init_skill.py (from standard skill-creator)
    └── package_skill.py (from standard skill-creator)
```

---

## The START_HERE.md: The Narrative Gateway

This file is the **heart of the system**. It's not a manual—it's an invitation into a story world.

### Structure of START_HERE.md

```markdown
# Welcome to [STORY WORLD NAME]

## Before You Begin

This is not a tutorial. This is a **journey through a world where skills are lived, not learned.**

You are about to enter an allegorical narrative where each challenge you face, each character you meet, and each obstacle you overcome will teach you practical, real-world skills. The story is your teacher. The characters are your guides. The world is your workshop.

## How This Works

1. **Copy this entire file** into your AI assistant (Claude, ChatGPT, etc.)
2. Your AI will become the **Narrator** of this world
3. You will make choices, solve problems, and progress through stages
4. Each stage unlocks a new skill—a real, practical skill you can use outside this narrative
5. Skills build on each other. You cannot skip stages.

## The First Transmission

[BEGIN NARRATIVE HOOK - Example:]

*You wake in a city called Recursion. Everything here repeats—buildings mirror themselves infinitely, conversations loop back to their beginning, citizens walk the same paths eternally. You alone remember that things were once different.*

*An old woman approaches, her eyes fractal patterns. "You're the Pattern Breaker," she says. "If you can learn to see the Foundation of things—the base case that stops infinite loops—you can free us."*

*She hands you a weathered tome titled "Foundation Prime."*

**Your first task:** Understand the Foundation. Only then can you break the first cycle.

---

### STAGE 0: Foundation Prime

**Real-World Allegory:** This stage teaches [SPECIFIC SKILL DOMAIN - e.g., "algorithmic thinking," "system design patterns," "recursive problem-solving"]

**Narrative Context:**
The old woman's tome describes the Recursion Theorem: "All infinite patterns have a base case—a foundation that, once understood, reveals the structure of everything above it."

**Your Challenge:**
Before you can progress, you must demonstrate understanding of the Foundation by solving the Recursion Riddle...

[Continue with narrative puzzles that guide the user to explore the 00-foundation-prime/ skill]

**To Continue:**
Once you've solved the Recursion Riddle and understand the Foundation, tell your AI: "I'm ready for Stage 1."

---

### STAGE 1: [Next Stage Name]

**Unlocked by:** Completing Foundation Prime
**Builds upon:** Foundation patterns

[Narrative continues, deepening complexity...]

```

### Key Principles for START_HERE.md

1. **Immediate Immersion:** Drop the user into the story world within the first paragraph
2. **Clear Mechanics:** Explain *how* to use the system without breaking narrative immersion
3. **Progressive Unlock:** Each stage gates the next, creating natural progression
4. **Allegorical Clarity:** Make it obvious (but not heavy-handed) how story elements map to real skills
5. **AI as Narrator:** Frame the user's AI as the storytelling engine, not just an assistant

---

## Individual Skill Architecture

### Foundation Skill (00-foundation-prime/)

This is the **only standalone skill** in the ecosystem. It cannot reference other skills because it defines the base patterns all others build upon.

#### SKILL.md Template for Foundation

```markdown
---
name: foundation-prime
description: Core foundational patterns for [DOMAIN]. This is the base skill that all subsequent skills in the narrative ecosystem build upon. Use when beginning the narrative journey or when fundamental pattern understanding is needed.
---

# Foundation Prime

## Purpose

This skill establishes the fundamental patterns, mental models, and procedural knowledge that serve as the foundation for all subsequent skills in the narrative ecosystem.

## Core Principles

[Define 3-5 fundamental principles that will be referenced throughout other skills]

1. **Principle One:** [Description]
2. **Principle Two:** [Description]
3. **Principle Three:** [Description]

## Foundational Workflows

[Define the basic workflows that other skills will extend]

### Workflow 1: [Name]
[Steps]

### Workflow 2: [Name]
[Steps]

## Narrative Context

In the world of [STORY NAME], this skill represents [ALLEGORICAL MEANING]. Users who master this skill will be able to [REAL-WORLD CAPABILITY].

## Usage Patterns

[Examples of when this skill triggers]

- User asks about [X]
- User needs to [Y]
- User is working on [Z]

## Bundled Resources

- `references/core-patterns.md`: Deep dive into foundational patterns
- `scripts/foundation-check.py`: Validation script to test understanding
```

### Subsequent Skills (01-skill-name/, 02-skill-name/, etc.)

These skills **explicitly reference and build upon previous skills**.

#### SKILL.md Template for Subsequent Skills

```markdown
---
name: [skill-name]
description: [What this skill does and when to use it]. Builds upon foundation-prime and [previous-skill-name]. Use when users have progressed past Stage [N] in the narrative.
---

# [Skill Name]

## Prerequisites

**Required Skills:**
- `00-foundation-prime`: Provides [what it provides]
- `[previous-skill-name]`: Provides [what it provides]

This skill extends the patterns learned in previous stages of the narrative journey.

## Purpose

[What this skill teaches, both narratively and practically]

## Building on the Foundation

This skill takes the [PRINCIPLE FROM FOUNDATION] and extends it by [HOW IT EXTENDS].

**From Foundation Prime, we learned:**
- [Recap relevant principle]

**In this skill, we add:**
- [New capability 1]
- [New capability 2]

## Workflows

### Workflow 1: [Name]
[Steps that reference foundation workflows]

**Foundation Pattern Used:** [Reference specific foundation workflow]
**Extension Added:** [What's new in this workflow]

## Narrative Context

In Stage [N] of [STORY NAME], this skill represents [ALLEGORICAL MEANING]. Users who master this skill will be able to [REAL-WORLD CAPABILITY].

**Previous Stage Connection:**
In Stage [N-1], you learned [X]. Now, you'll use that knowledge to [Y].

## Cross-Skill Integration

This skill works in combination with:
- `foundation-prime` for [purpose]
- `[previous-skill]` for [purpose]

When all three are active, you can [combined capability].

## Bundled Resources

- `references/foundation-context.md`: Quick reference to foundation patterns used here
- `references/previous-skill-context.md`: Relevant context from previous skill
- `references/advanced-patterns.md`: This skill's unique patterns
- `scripts/integration-test.py`: Tests integration with previous skills
```

---

## Repository-Level Files

### README.md

```markdown
# Skill Forge: A Narrative Skill Ecosystem

This repository contains a **narrative-driven skill learning system** where practical real-world skills are taught through an immersive allegorical story.

## What Is This?

Traditional skill documentation is dry and disconnected. This system flips the script: **you learn by exploring a story world**.

Each narrative stage teaches a real, practical skill. Skills build on each other. You cannot skip ahead—the foundation must be learned before the complexity can be understood.

## How to Use

1. Read `START_HERE.md`
2. Copy its contents into your AI assistant
3. Let your AI guide you through the narrative
4. Complete challenges to unlock skills
5. Apply those skills to real-world work

## Philosophy

Learning is best when it's:
- **Sequential:** Each skill builds on previous ones
- **Contextual:** Skills are learned through problems, not abstractions
- **Immersive:** Story creates memory anchors
- **Practical:** Every narrative element maps to real-world capability

## Repository Structure

- `START_HERE.md`: Your entry point into the narrative
- `skills/`: Individual skill directories (00, 01, 02...)
- `narrative/`: Story world context that evolves with you
- `scripts/`: Standard skill-creator tools

## For Skill Creators

This repository can be forked and customized. The narrative framework is adaptable to any skill domain:
- Programming paradigms
- Design methodologies
- Business strategy
- Creative workflows
- Technical domains

The key is maintaining the allegorical structure where story maps to skill.
```

### narrative/world-state.md

```markdown
# World State Tracker

This file tracks the evolving state of the narrative world as the user progresses.

## Current Stage: [Dynamic - updates as user progresses]

## World Events
- Stage 0: [What happened]
- Stage 1: [What happened]
- Stage 2: [What happened]

## Character Encounters
[List of narrative characters and their story arcs]

## User's Journey
[Milestones the user has reached]

## Unlocked Capabilities
[Real-world skills the user has demonstrated]
```

---

## Implementation Instructions for Claude Code

### Step 1: Repository Initialization

```bash
# Create the repository structure
mkdir skill-forge-narrative
cd skill-forge-narrative

# Initialize git
git init

# Create directory structure
mkdir -p skills/{00-foundation-prime,01-pattern-weaver,02-system-architect}/{references,scripts,assets}
mkdir -p narrative
mkdir -p scripts

# Copy standard skill-creator scripts
# (You'll need to provide paths to init_skill.py and package_skill.py)
```

### Step 2: Gather Domain Requirements

Before generating skills, ask the user:

1. **What domain are these skills for?**
   - Programming? Design? Strategy? Creative work?
   
2. **What is the narrative world?**
   - What's the setting? The central conflict? The allegory?
   
3. **How many stages/skills should the system have?**
   - Typically 3-7 skills is manageable
   
4. **What real-world capabilities should users gain?**
   - Be specific about the practical outcomes

### Step 3: Generate START_HERE.md

Create an immersive narrative entry point that:
- Establishes the story world immediately
- Explains the learning mechanic clearly
- Provides the first narrative challenge
- Maps story elements to skills explicitly (but elegantly)

### Step 4: Create Foundation Skill (00-foundation-prime/)

This skill must:
- Stand alone (no dependencies)
- Define core principles ALL other skills reference
- Provide foundational workflows
- Include validation scripts to test understanding

### Step 5: Create Subsequent Skills (01, 02, 03...)

Each skill must:
- Reference foundation explicitly in SKILL.md
- Reference previous skill(s) explicitly
- Extend foundational patterns, don't replace them
- Include `references/foundation-context.md` with relevant excerpts
- Include `references/[previous-skill]-context.md` with relevant context
- Provide integration tests that validate cross-skill functionality

### Step 6: Populate Narrative Files

Create:
- `narrative/world-state.md`: Tracks narrative progression
- `narrative/character-arcs.md`: Story character development
- `narrative/stage-progressions.md`: Narrative checkpoints and transitions

### Step 7: Create Repository Documentation

Write:
- `README.md`: Philosophy, usage, structure
- `CONTRIBUTING.md` (optional): How others can extend the system

### Step 8: Initialize Git and Push

```bash
git add .
git commit -m "Initialize narrative skill ecosystem"
git branch -M main
git remote add origin [user-provided-url]
git push -u origin main
```

---

## Key Success Criteria

✅ **Narrative Coherence:** The story world makes sense and evolves logically
✅ **Skill Progression:** Each skill genuinely builds on previous ones
✅ **Allegorical Clarity:** Story elements clearly map to real-world skills
✅ **Practical Utility:** Skills are immediately applicable outside the narrative
✅ **AI Collaboration:** User's AI can effectively "narrate" the experience
✅ **Progressive Disclosure:** Complexity increases naturally, not arbitrarily
✅ **Validation Mechanisms:** Scripts and challenges test actual understanding
✅ **Cross-Skill Integration:** Later skills leverage earlier skills explicitly

---

## Example Narrative Frameworks

### Framework 1: "The Recursion City" (Programming/Algorithms)
- **Stage 0:** Foundation Prime - Base Cases & Termination
- **Stage 1:** The Loop Breaker - Iterative Patterns
- **Stage 2:** The Stack Walker - Recursive Thinking
- **Stage 3:** The Memory Keeper - Dynamic Programming

### Framework 2: "The Pattern Forge" (Design Systems)
- **Stage 0:** Foundation Prime - Core Design Principles
- **Stage 1:** The Component Smith - Atomic Design
- **Stage 2:** The System Architect - Composition Patterns
- **Stage 3:** The Experience Weaver - User Flow Integration

### Framework 3: "The Protocol Wars" (Distributed Systems)
- **Stage 0:** Foundation Prime - Node Communication
- **Stage 1:** The Message Bearer - Asynchronous Patterns
- **Stage 2:** The Consensus Builder - Agreement Protocols
- **Stage 3:** The Fault Healer - Resilience Patterns

---

## Final Notes

This system works because:

1. **Story creates memory:** Narrative anchors make skills stick
2. **Progression feels natural:** Each stage feels earned, not arbitrary
3. **Skills are interconnected:** Real-world work requires integrated knowledge
4. **AI becomes facilitator:** User's AI guides discovery, not just answers questions
5. **Allegory makes it transferable:** Story patterns map to real-world patterns

The goal: **Users don't just read about skills—they live through them.**

---

## Usage for Claude Code

When you receive this prompt:

1. Ask clarifying questions about domain, narrative world, and desired outcomes
2. Generate the full repository structure
3. Create START_HERE.md with an immersive narrative hook
4. Build foundation skill with clear, referenceable patterns
5. Build subsequent skills that explicitly extend foundation
6. Populate narrative tracking files
7. Initialize git repository
8. Provide user with next steps for customization

**Remember:** Every skill should be practical and real. The narrative is the vehicle, not the destination.
