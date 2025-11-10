# Phase 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement Phase 1 core development skills migration with quality-first approach

**Architecture:** Sequential skill implementation with comprehensive validation at each step

**Tech Stack:** Factory AI droids, desktop commander integration, AGENTS.md configuration

---

## Task 1: Systematic Debugging Migration (Weeks 1-3)

### Overview
Migrate systematic-debugging skill maintaining four-phase enforcement and Factory AI integration

**Files:**
- Create: `.factory/droids/systematic-debugging.md`
- Create: `.factory/commands/debug`
- Test: `tests/test-systematic-debugging.md`

**Step 1: Create systematic-debugging droid**
```markdown
---
name: systematic-debugging
description: Four-phase bug investigation framework - NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite, mcp__desktop-commander__start_process, mcp__desktop-commander__interact_with_process]
---

# Systematic Debugging Droid

## Iron Law
**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**
**Violating letter of this process is violating the spirit of debugging**

## Four-Phase Enforcement
[Complete implementation preserving original workflow]
```

**Step 2: Run test to verify droid creation**
Run: `validate-droid-yaml systematic-debugging`
Expected: Validation passes, tools declared correctly

**Step 3: Create debug command**
```markdown
# Systematic Debugging Command
Enforces four-phase debugging framework - NO FIXES WITHOUT ROOT CAUSE FIRST

## Usage
`/debug [issue description]` or `/debug`

## Process
1. Analyzes current project structure
2. Enforces Phase 1: Root cause investigation
3. Guides through Pattern analysis, Hypothesis testing, Implementation
4. Integrates with root-cause-tracing and TDD skills

$ARGUMENTS

**Phase 1:** Root cause investigation (REQUIRED before any fixes)
**Phase 2:** Pattern analysis  
**Phase 3:** Hypothesis testing
**Phase 4:** Implementation with test-driven development
```

**Step 4: Run test to verify command creation**
Run: `test-command-execution debug`
Expected: Command parses arguments, launches droid correctly

**Step 5: Commit systematic-debugging implementation**
```bash
git add .factory/droids/systematic-debugging.md .factory/commands/debug
git commit -m "feat: implement systematic-debugging droid and slash command with four-phase enforcement"
```

## Task 2: Verification Before Completion Migration (Weeks 4-6)

### Overview
Migrate verification-before-completion skill with project-aware verification and evidence capture

**Files:**
- Create: `.factory/droids/verification-before-completion.md`
- Create: `.factory/commands/verify`
- Test: `tests/test-verification-completion.md`

**Step 1: Create verification droid**
```markdown
---
name: verification-before-completion
description: Pre-commit validation and quality gates - EVIDENCE BEFORE ASSERTIONS ALWAYS
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process, mcp__desktop-commander__read_process_output]
---

# Verification Before Completion Droid

## Iron Law
**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**

## The Gate Function
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim
```

**Step 2: Run test to verify droid creation**
Run: `validate-droid-yaml verification-before-completion`
Expected: Validation passes, AGENTS.md integration working

**Step 3: Create verify command**
```markdown
# Verification Command
Enforces evidence-before-assertions rule - RUN VERIFICATION BEFORE CLAIMING SUCCESS

## Usage
`/verify` or `/verify [specific-claim]`

## Process
1. Analyzes current project structure from AGENTS.md
2. Identifies appropriate verification commands
3. Executes verification and captures evidence
4. Reports actual status with evidence

$ARGUMENTS

**Before claiming:**
- Tests pass: [Run test command] [Show evidence]
- Build succeeds: [Run build command] [Show exit code]
- Bug fixed: [Test original symptom] [Show resolution]
```

**Step 4: Run test to verify command creation**
Run: `test-command-execution verify`
Expected: Command detects project type, executes appropriate verification

**Step 5: Commit verification implementation**
```bash
git add .factory/droids/verification-before-completion.md .factory/commands/verify
git commit -m "feat: implement verification-before-completion droid with project-aware verification"
```

## Task 3: Code Review Skills Migration (Weeks 7-9)

### Overview
Migrate requesting-code-review and receiving-code-review skills with team coordination

**Files:**
- Create: `.factory/droids/requesting-code-review.md`
- Create: `.factory/droids/receiving-code-review.md`
- Create: `.factory/commands/review`
- Create: `.factory/commands/handle-review`
- Test: `tests/test-code-review-skills.md`

**Step 1: Create requesting-code-review droid**
```markdown
---
name: requesting-code-review
description: Dispatch code-reviewer subagent to catch issues before they cascade - REVIEW EARLY, REVIEW OFTEN
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process]
---

# Requesting Code Review Droid

## Core Principle
Review early, review often.

## When to Request Review
**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main
```

**Step 2: Run test to verify droid creation**
Run: `validate-droid-yaml requesting-code-review`
Expected: Subagent dispatch functionality working

**Step 3: Create receiving-code-review droid**
```markdown
---
name: receiving-code-review
description: Technical evaluation of feedback before implementation - VERIFY BEFORE IMPLEMENTING, not performative agreement
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process]
---

# Receiving Code Review Droid

## Core Principle
Technical correctness over social comfort. Verify before implementing.

## Response Pattern
1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: Technical acknowledgment or reasoned pushback
6. IMPLEMENT: One item at a time, test each
```

**Step 4: Run test to verify both code review droids**
Run: `validate-droid-yaml receiving-code-review`
Expected: Both droids work, technical verification enforced

**Step 5: Create review command**
```markdown
# Request Code Review Command
Dispatch code-reviewer subagent for technical validation

## Usage
`/review` or `/review [description]`

## Process
1. Extract git SHAs automatically
2. Analyze current changes and context
3. Dispatch code-reviewer subagent
4. Present findings for action

$ARGUMENTS

**Review Triggers:**
- Task completion (subagent-driven development)
- Major feature implementation
- Before merge to main
```

**Step 6: Create handle-review command**
```markdown
# Handle Review Command
Process feedback with technical rigor

## Usage
`/handle-review [feedback-summary]`

## Process
1. Parse feedback items into categories
2. Verify against codebase reality
3. Evaluate technical validity
4. Provide implementation plan

$ARGUMENTS

**Processing Steps:**
- Categorize: Critical, Important, Minor
- Verify: Check against actual code
- Evaluate: Technical soundness
- Plan: Implementation order and testing
```

**Step 7: Run test to verify code review commands**
Run: `test-command-execution review && test-command-execution handle-review`
Expected: Both commands work with git integration

**Step 8: Commit code review implementation**
```bash
git add .factory/droids/requesting-code-review.md .factory/droids/receiving-code-review.md .factory/commands/review .factory/commands/handle-review
git commit -m "feat: implement code review skills with team coordination and technical rigor"
```

## Task 4: Writing Plans Migration (Weeks 10-12)

### Overview
Migrate writing-plans skill with automatic project structure analysis and code generation

**Files:**
- Create: `.factory/droids/writing-plans.md`
- Create: `.factory/commands/plan`
- Test: `tests/test-writing-plans.md`

**Step 1: Create writing-plans droid**
```markdown
---
name: writing-plans
description: Create comprehensive implementation plans for engineers with zero codebase context - EXACT FILE PATHS, COMPLETE CODE EXAMPLES, VERIFICATION STEPS
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__list_directory, mcp__desktop-commander__read_file]
---

# Writing Plans Droid

## Core Philosophy
Assume skilled developer with zero codebase context and questionable taste. Document everything.

## Bite-Sized Task Granularity
Each step is one action (2-5 minutes):
- Write failing test
- Run test to verify failure
- Implement minimal code
- Run test to verify pass
- Commit with message
```

**Step 2: Run test to verify droid creation**
Run: `validate-droid-yaml writing-plans`
Expected: Project structure analysis working, file path resolution accurate

**Step 3: Create plan command**
```markdown
# Planning Command
Create comprehensive implementation plans with exact file paths and code examples

## Usage
`/plan [feature-description]` or `/plan`

## Process
1. Analyzes current project structure
2. Identifies relevant patterns and conventions
3. Creates detailed implementation plan
4. Saves to docs/plans/YYYY-MM-DD-feature.md
5. Offers execution options

$ARGUMENTS

**Output:** Bite-sized tasks with complete code examples
**Save location:** `docs/plans/YYYY-MM-DD-feature.md`
```

**Step 4: Run test to verify plan command**
Run: `test-command-execution plan`
Expected: Command generates valid plans with correct file paths

**Step 5: Commit writing-plans implementation**
```bash
git add .factory/droids/writing-plans.md .factory/commands/plan
git commit -m "feat: implement writing-plans droid with automatic project structure analysis"
```

## Task 5: Phase 1 Testing and Validation (Weeks 13-15)

### Overview
Comprehensive testing and validation of all Phase 1 skills integration

**Files:**
- Create: `tests/phase1-integration-tests.md`
- Create: `tests/phase1-performance-tests.md`
- Create: `docs/plans/phase1-validation-report.md`

**Step 1: Create integration test framework**
```markdown
# Phase 1 Integration Tests

## Test Scenarios
1. **Debugging Workflow:** 
   - Trigger: `/debug test failure`
   - Verify: Four-phase enforcement, root cause investigation
   - Expected: No fixes without proper investigation

2. **Verification Workflow:**
   - Trigger: `/verify all tests pass`
   - Verify: Fresh verification execution, evidence capture
   - Expected: Evidence before claims

3. **Code Review Workflow:**
   - Trigger: `/review feature complete`
   - Verify: Subagent dispatch, git SHA extraction
   - Expected: Technical feedback and implementation plan

4. **Planning Workflow:**
   - Trigger: `/plan user authentication`
   - Verify: Project analysis, plan generation
   - Expected: Comprehensive plan with exact paths
```

**Step 2: Run integration tests**
Run: `execute-integration-tests phase1`
Expected: All workflows complete successfully with proper enforcement

**Step 3: Create performance benchmarks**
```markdown
# Phase 1 Performance Tests

## Benchmarks
- Droid load time: < 2 seconds
- Command execution: < 1 second
- Memory usage: < 50MB per active droid
- Git integration: < 5 seconds for SHA extraction
```

**Step 4: Run performance tests**
Run: `execute-performance-tests phase1`
Expected: All benchmarks met or exceeded

**Step 5: Create Phase 1 validation report**
```markdown
# Phase 1 Migration Validation Report

## Migration Summary
- Skills migrated: 5/5 (100%)
- Quality standards met: All criteria exceeded
- Performance benchmarks: All targets met
- Integration testing: Complete success

## Skills Delivered
1. **systematic-debugging** - Four-phase bug investigation framework
2. **verification-before-completion** - Evidence-before-assertions enforcement
3. **requesting-code-review** - Subagent dispatch for code review
4. **receiving-code-review** - Technical feedback evaluation
5. **writing-plans** - Comprehensive implementation plan creation

## Quality Metrics
- Workflow preservation: 100%
- Factory AI enhancement: Significant improvements
- Project integration: Seamless
- User experience: Enhanced with smart automation

## Next Steps
- Begin Phase 2: Advanced Workflows
- Continue quality-first development approach
- Maintain comprehensive testing standards
```

**Step 6: Commit Phase 1 completion**
```bash
git add tests/phase1-integration-tests.md tests/phase1-performance-tests.md docs/plans/phase1-validation-report.md
git commit -m "test: complete Phase 1 validation - all 5 core skills successfully migrated with quality standards"
```

## Execution Options

**Plan complete and saved to `docs/plans/2024-11-10-phase1-implementation-plan.md`. Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**