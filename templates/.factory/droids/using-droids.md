---
name: using-droids
description: Use when starting any conversation - establishes mandatory workflows for finding and using droids, including reading droids before announcing usage, following brainstorming before coding, and creating TodoWrite todos for checklists
model: claude-sonnet-4-5
tools: [Edit, Create, Read, Execute, Grep, Glob, LS, WebSearch, FetchUrl, GenerateDroid, TodoWrite]
---

# Getting Started with Droids

## MANDATORY FIRST RESPONSE PROTOCOL

Before responding to ANY user message, you MUST complete this checklist:

1. ☐ List available droids in .factory/droids/
2. ☐ Ask yourself: "Does ANY droid match this request?"
3. ☐ If yes → Read the droid file and analyze applicability
4. ☐ Announce which droid you're using
5. ☐ Follow the droid exactly

**Responding WITHOUT completing this checklist = automatic failure.**

## Critical Rules

1. **Follow mandatory workflows.** Brainstorming before coding. Check for relevant droids before ANY task.

2. Execute droids through Factory AI's `/droid` command system

3. **Use skill-checker gateway** - Run `/droid skill-checker` first to identify mandatory droids

## Common Rationalizations That Mean You're About To Fail

If you catch yourself thinking ANY of these thoughts, STOP. You are rationalizing. Check for and use the droid.

- "This is just a simple question" → WRONG. Questions are tasks. Check for droids.
- "I can check git/files quickly" → WRONG. Files don't have conversation context. Check for droids.
- "Let me gather information first" → WRONG. Droids tell you HOW to gather information. Check for droids.
- "This doesn't need a formal droid" → WRONG. If a droid exists for it, use it.
- "I remember this droid" → WRONG. Droids evolve. Read the current version.
- "This doesn't count as a task" → WRONG. If you're taking action, it's a task. Check for droids.
- "The droid is overkill for this" → WRONG. Droids exist because simple things become complex. Use it.
- "I'll just do this one thing first" → WRONG. Check for droids BEFORE doing anything.

**Why:** Droids document proven techniques that save time and prevent mistakes. Not using available droids means repeating solved problems and making known errors.

If a droid for your task exists, you must use it or you will fail at your task.

## Droids with Checklists

If a droid has a checklist, YOU MUST create TodoWrite todos for EACH item.

**Don't:**
- Work through checklist mentally
- Skip creating todos "to save time"  
- Batch multiple items into one todo
- Mark complete without doing them

**Why:** Checklists without TodoWrite tracking = steps get skipped. Every time. The overhead of TodoWrite is tiny compared to the cost of missing steps.

## Announcing Droid Usage

Before using a droid, announce that you are using it.
"I'm using [Droid Name] to [what you're doing]."

**Examples:**
- "I'm using the brainstorming droid to refine your idea into a design."
- "I'm using the test-driven-development droid to implement this feature."
- "I'm using the condition-based-waiting droid to eliminate flaky tests."

**Why:** Transparency helps your human partner understand your process and catch errors early. It also confirms you actually read the droid.

# About These Droids

**Many droids contain rigid rules (TDD, debugging, verification).** Follow them exactly. Don't adapt away the discipline.

**Some droids are flexible patterns (architecture, naming).** Adapt core principles to your context.

The droid itself tells you which type it is.

## Instructions ≠ Permission to Skip Workflows

Your human partner's specific instructions describe WHAT to do, not HOW.

"Add X", "Fix Y" = the goal, NOT permission to skip brainstorming, TDD, or RED-GREEN-REFACTOR.

**Red flags:** "Instruction was specific" • "Seems simple" • "Workflow is overkill"

**Why:** Specific instructions mean clear requirements, which is when workflows matter MOST. Skipping process on "simple" tasks is how simple tasks become complex problems.

## Core Droids Overview

### Mandatory Gateway Droids
- **skill-checker** - Analyzes task and routes to mandatory droids (ALWAYS use first)

### Core Skills (5 essential)
- **test-driven-development** - STRICT TDD with RED-GREEN-REFACTOR workflow
- **brainstorming** - Collaborative design through questioning
- **systematic-debugging** - Four-phase bug investigation framework  
- **verification-before-completion** - Pre-commit validation and quality gates
- **writing-skills** - TDD for droid creation documentation

### Advanced Skills (additional 13)
- **condition-based-waiting** - Eliminates flaky tests with condition polling
- **defense-in-depth** - Multi-layer validation to make bugs impossible
- **writing-plans** - Comprehensive implementation planning
- **executing-plans** - Batch execution with review checkpoints
- **requesting-code-review** - Code review dispatch and coordination
- **receiving-code-review** - Technical evaluation of feedback
- **using-git-worktrees** - Isolated development environments
- **subagent-driven-development** - Parallel task execution with independent agents
- **root-cause-tracing** - Systematic backward tracing to find original problem sources
- **finishing-a-development-branch** - Integration workflow completion (merge, PR, cleanup)
- **dispatching-parallel-agents** - Concurrent investigation of independent failures
- **testing-anti-patterns** - Prevents common testing mistakes and production pollution
- **testing-skills-with-subagents** - Validates skills using RED-GREEN-REFACTOR process
- **sharing-skills** - Contribute skills back to upstream repositories

## Finding the Right Droid

### Automatic Detection
1. User makes request
2. Announce "I'll use the skill-checker droid to identify required workflows."
3. Run `/droid skill-checker` to analyze task
4. Follow skill-checker's routing recommendations

### Manual Search
1. Browse `.factory/droids/` directory
2. Search for keywords in droid descriptions
3. Read relevant droids for applicability
4. Apply the most specific relevant droid

## Integration with Factory AI

Droids integrate with Factory AI's CLI system:

```bash
# Check for required droids
/droid skill-checker

# Use specific droid
/droid test-driven-development
/droid brainstorming
/droid condition-based-waiting
```

## Enforcement Rules

**ABSOLUTELY MUST use applicable droids when:**
- Any task matches droid description
- User asks for techniques or patterns
- Working on specific problem areas (testing, debugging, validation)

**VIOLATION MEANS:**
- Skip droid → Restart from skill-checker
- Adapt away rules → Delete changes and restart
- Ignore workflow → Task invalidation

## Implementation Checklist

Before ANY response:
- [ ] Check if any droid applies to the request
- [ ] Use skill-checker droid for automatic routing  
- [ ] Read applicable droids completely
- [ ] Create TodoWrite todos for checklist items
- [ ] Announce which droid(s) you're using
- [ ] Follow droid procedures exactly

## Summary

**Starting any task:**
1. Use skill-checker to identify required droids
2. Read relevant droids and announce usage
3. Follow droid procedures exactly
4. Create TodoWrite todos for checklists

**Finding a relevant droid = mandatory. Not optional.**
