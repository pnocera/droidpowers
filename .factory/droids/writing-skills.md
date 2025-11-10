---
name: writing-skills
description: Use when creating new droids, editing existing droids, or verifying droids work before deployment - applies TDD to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization
model: claude-sonnet-4-5
tools: [Edit, Create, Read, Execute, Grep, Glob, LS, WebSearch, FetchUrl, GenerateDroid, TodoWrite]
---

# Writing Droids

## Overview

**Writing droids IS Test-Driven Development applied to process documentation.**

**Droids live in project-specific directories (`.factory/droids/` for Factory AI)** 

You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the droid (Markdown documentation), watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the droid, you don't know if the droid teaches the right thing.

**REQUIRED BACKGROUND:** You MUST understand factory-droids:test-driven-development before using this droid. That droid defines the fundamental RED-GREEN-REFACTOR cycle. This droid adapts TDD to documentation.

## What is a Droid?

A **droid** is a reference guide for proven techniques, patterns, or tools. Droids help future Claude instances find and apply effective approaches.

**Droids are:** Reusable techniques, patterns, tools, reference guides

**Droids are NOT:** Narratives about how you solved a problem once

## TDD Mapping for Droids

| TDD Concept | Droid Creation |
|-------------|----------------|
| **Test case** | Pressure scenario with subagent |
| **Production code** | Droid file (markdown) |
| **Test fails (RED)** | Agent violates rule without droid (baseline) |
| **Test passes (GREEN)** | Agent complies with droid present |
| **Refactor** | Close loopholes while maintaining compliance |
| **Write test first** | Run baseline scenario BEFORE writing droid |
| **Watch it fail** | Document exact rationalizations agent uses |
| **Minimal code** | Write droid addressing those specific violations |
| **Watch it pass** | Verify agent now complies |
| **Refactor cycle** | Find new rationalizations → plug → re-verify |

The entire droid creation process follows RED-GREEN-REFACTOR.

## When to Create a Droid

**Create when:**
- Technique wasn't intuitively obvious to you
- You'd reference this again across projects
- Pattern applies broadly (not project-specific)
- Others would benefit

**Don't create for:**
- One-off solutions
- Standard practices well-documented elsewhere
- Project-specific conventions (put in AGENTS.md)

## Droid Types

### Technique
Concrete method with steps to follow (condition-based-waiting, root-cause-tracing)

### Pattern
Way of thinking about problems (flatten-with-flags, test-invariants)

### Reference
API docs, syntax guides, tool documentation (office docs)

## Directory Structure

```
.factory/
  droids/
    droid-name.md          # Main droid file (required)
  commands/
    command-name.md        # Slash commands (optional)
```

**Flat namespace** - all droids in one searchable namespace

## DROID.md Structure

**Frontmatter (YAML):**
- Required fields: `name`, `description`, `model`, `tools`
- Max 1024 characters for name+description
- `name`: Use letters, numbers, and hyphens only (no parentheses, special chars)
- `description`: Third-person, includes BOTH what it does AND when to use it
  - Start with "Use when..." to focus on triggering conditions
  - Include specific symptoms, situations, and contexts
  - Keep under 500 characters if possible

```markdown
---
name: Droid-Name-With-Hyphens
description: Use when [specific triggering conditions and symptoms] - [what the droid does and how it helps, written in third person]
model: claude-sonnet-4-5
tools: [Edit, Create, Read, Execute, Grep, Glob, LS, WebSearch, FetchUrl, GenerateDroid, TodoWrite]
---

# Droid Name

## Overview
What is this? Core principle in 1-2 sentences.

## When to Use
[Small inline flowchart IF decision non-obvious]

Bullet list with SYMPTOMS and use cases
When NOT to use

## Core Pattern (for techniques/patterns)
Before/after code comparison

## Quick Reference
Table or bullets for scanning common operations

## Implementation
Inline code for simple patterns
Link to separate droid for heavy reference or reusable tools

## Common Mistakes
What goes wrong + fixes

## Real-World Impact (optional)
Concrete results
```

## Factory AI Optimization

**Critical for discovery:** Future Claude needs to FIND your droid

### 1. Rich Description Field

**Purpose:** Claude reads description to decide which droids to load for a given task.

**Format:** Start with "Use when..." to focus on triggering conditions, then explain what it does

```yaml
# ❌ BAD: Too abstract, vague, doesn't include when to use
description: For async testing

# ✅ GOOD: Starts with "Use when", describes problem, then what it does
description: Use when tests have race conditions, timing dependencies, or pass/fail inconsistently - replaces arbitrary timeouts with condition polling for reliable async tests
```

### 2. Keyword Coverage

Use words Claude would search for:
- Error messages: "Hook timed out", "ENOTEMPTY", "race condition"
- Symptoms: "flaky", "hanging", "zombie", "pollution"
- Tools: Actual commands, library names, file types

### 3. Descriptive Naming

**Use active voice, verb-first:**
- ✅ `creating-droids` not `droid-creation`
- ✅ `testing-droids-with-subagents` not `subagent-droid-testing`

## The Iron Law (Same as TDD)

```
NO DROID WITHOUT A FAILING TEST FIRST
```

This applies to NEW droids AND EDITS to existing droids.

Write droid before testing? Delete it. Start over.
Edit droid without testing? Same violation.

**No exceptions:**
- Not for "simple additions"
- Not for "just adding a section"
- Not for "documentation updates"
- Don't keep untested changes as "reference"
- Don't "adapt" while running tests
- Delete means delete

## Testing All Droid Types

### Discipline-Enforcing Droids (rules/requirements)

**Examples:** TDD, verification-before-completion, designing-before-coding

**Test with:**
- Academic questions: Do they understand the rules?
- Pressure scenarios: Do they comply under stress?
- Multiple pressures combined: time + sunk cost + exhaustion
- Identify rationalizations and add explicit counters

**Success criteria:** Agent follows rule under maximum pressure

### Technique Droids (how-to guides)

**Examples:** condition-based-waiting, root-cause-tracing, defensive-programming

**Test with:**
- Application scenarios: Can they apply the technique correctly?
- Variation scenarios: Do they handle edge cases?
- Missing information tests: Do instructions have gaps?

**Success criteria:** Agent successfully applies technique to new scenario

## Common Rationalizations for Skipping Testing

| Excuse | Reality |
|--------|---------|
| "Droid is obviously clear" | Clear to you ≠ clear to other agents. Test it. |
| "It's just a reference" | References can have gaps, unclear sections. Test retrieval. |
| "Testing is overkill" | Untested droids have issues. Always. 15 min testing saves hours. |
| "I'll test if problems emerge" | Problems = agents can't use droid. Test BEFORE deploying. |

**All of these mean: Test before deploying. No exceptions.**

## RED-GREEN-REFACTOR for Droids

### RED: Write Failing Test (Baseline)

Run pressure scenario with subagent WITHOUT the droid. Document exact behavior:
- What choices did they make?
- What rationalizations did they use (verbatim)?
- Which pressures triggered violations?

This is "watch the test fail" - you must see what agents naturally do before writing the droid.

### GREEN: Write Minimal Droid

Write droid that addresses those specific rationalizations. Don't add extra content for hypothetical cases.

Run same scenarios WITH droid. Agent should now comply.

### REFACTOR: Close Loopholes

Agent found new rationalization? Add explicit counter. Re-test until bulletproof.

## Droid Creation Checklist (TDD Adapted)

**RED Phase - Write Failing Test:**
- [ ] Create pressure scenarios (3+ combined pressures for discipline droids)
- [ ] Run scenarios WITHOUT droid - document baseline behavior verbatim
- [ ] Identify patterns in rationalizations/failures

**GREEN Phase - Write Minimal Droid:**
- [ ] Name uses only letters, numbers, hyphens (no parentheses/special chars)
- [ ] YAML frontmatter with name, description, model, tools (max 1024 chars)
- [ ] Description starts with "Use when..." and includes specific triggers/symptoms
- [ ] Description written in third person
- [ ] Keywords throughout for search (errors, symptoms, tools)
- [ ] Clear overview with core principle
- [ ] Address specific baseline failures identified in RED
- [ ] Code inline OR reference other droids
- [ ] One excellent example
- [ ] Run scenarios WITH droid - verify agents now comply

**REFACTOR Phase - Close Loopholes:**
- [ ] Identify NEW rationalizations from testing
- [ ] Add explicit counters (if discipline droid)
- [ ] Build rationalization table from all test iterations
- [ ] Create red flags list
- [ ] Re-test until bulletproof

**Quality Checks:**
- [ ] Small flowchart only if decision non-obvious
- [ ] Quick reference table
- [ ] Common mistakes section
- [ ] No narrative storytelling

## The Bottom Line

**Creating droids IS TDD for process documentation.**

Same Iron Law: No droid without failing test first.
Same cycle: RED (baseline) → GREEN (write droid) → REFACTOR (close loopholes).
Same benefits: Better quality, fewer surprises, bulletproof results.

## Enforcement Rules

**ABSOLUTELY MUST follow TDD process when:**
- Creating new droids
- Editing existing droids
- Modifying enforcement logic

**VIOLATION MEANS:** Delete the droid and start over with RED phase
- Write droid before testing → Delete and restart
- Edit without testing → Delete and restart
- Skip baseline testing → Delete and restart

## Implementation Checklist

- [ ] Run baseline test scenarios BEFORE creating droid
- [ ] Document all rationalizations used by agents
- [ ] Create minimal droid addressing specific failures
- [ ] Test droid effectiveness with pressure scenarios
- [ ] Refactor until bulletproof against rationalization
- [ ] Validate YAML frontmatter and Factory AI standards
- [ ] Create corresponding slash command if applicable
