---
name: subagent-driven-development
description: Execute plans with independent tasks and fresh subagents - HIGH QUALITY, FAST ITERATION
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite, mcp__desktop-commander__start_process]
---

# Subagent-Driven Development Droid

## Overview

Execute plan by dispatching fresh subagent per task, with code review after each.

**Core principle:** Fresh subagent per task + review between tasks = high quality, fast iteration

## vs. Executing Plans (parallel session):
- Same session (no context switch)
- Fresh subagent per task (no context pollution)
- Code review after each task (catch issues early)
- Faster iteration (no human-in-loop between tasks)

## When to Use

**Use when:**
- Staying in this session
- Tasks are mostly independent
- Want continuous progress with quality gates

**When NOT to use:**
- Need to review plan first (use executing-plans)
- Tasks are tightly coupled (manual execution better)
- Plan needs revision (brainstorm first)

## The Process

### 1. Load Plan

Read plan file, create TodoWrite with all tasks.

### 2. Execute Task with Subagent

For each task:

**Dispatch fresh subagent:**
```
Task tool (general-purpose):
  description: "Implement Task N: [task name]"
  prompt: |
    You are implementing Task N from [plan-file].

    Read that task carefully. Your job is to:
    1. Implement exactly what the task specifies
    2. Write tests (following TDD if task says to)
    3. Verify implementation works
    4. Commit your work
    5. Report back

    Work from: [directory]

    Report: What you implemented, what you tested, test results, files changed, any issues
```

**Subagent reports back** with summary of work.

### 3. Review Subagent's Work

**Dispatch code-reviewer subagent:**
```
Task tool (superpowers:code-reviewer):
  Use template at requesting-code-review/code-reviewer.md

  WHAT_WAS_IMPLEMENTED: [from subagent's report]
  PLAN_OR_REQUIREMENTS: Task N from [plan-file]
  BASE_SHA: [commit before task]
  HEAD_SHA: [current commit]
  DESCRIPTION: [task summary]
```

**Code reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment

### 4. Apply Review Feedback

**If issues found:**
- Fix Critical issues immediately
- Fix Important issues before next task
- Note Minor issues

**Dispatch follow-up subagent if needed:**
```
"Fix issues from code review: [list issues]"
```

### 5. Mark Complete, Next Task

- Mark task as completed in TodoWrite
- Move to next task
- Repeat steps 2-5

### 6. Final Review

After all tasks complete, dispatch final code-reviewer:
- Reviews entire implementation
- Checks all plan requirements met
- Validates overall architecture

### 7. Complete Development

After final review passes:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## Example Workflow

```
You: I'm using Subagent-Driven Development to execute this plan.

[Load plan, create TodoWrite]

Task 1: Hook installation script

[Dispatch implementation subagent]
Subagent: Implemented install-hook with tests, 5/5 passing

[Get git SHAs, dispatch code-reviewer]
Reviewer: Strengths: Good test coverage. Issues: None. Ready.

[Mark Task 1 complete]

Task 2: Recovery modes

[Dispatch implementation subagent]
Subagent: Added verify/repair, 8/8 tests passing

[Dispatch code-reviewer]
Reviewer: Strengths: Solid. Issues (Important): Missing progress reporting

[Dispatch fix subagent]
Fix subagent: Added progress every 100 conversations

[Verify fix, mark Task 2 complete]

...

[After all tasks]
[Dispatch final code-reviewer]
Final reviewer: All requirements met, ready to merge

Done!
```

## Advantages

**vs. Manual execution:**
- Subagents follow TDD naturally
- Fresh context per task (no confusion)
- Parallel-safe (subagents don't interfere)

**vs. Executing Plans:**
- Same session (no handoff)
- Continuous progress (no waiting)
- Review checkpoints automatic

## Cost:
- More subagent invocations
- But catches issues early (cheaper than debugging later)

## Red Flags

**Never:**
- Skip code review between tasks
- Proceed with unfixed Critical issues
- Dispatch multiple implementation subagents in parallel (conflicts)
- Implement without reading plan task

**If subagent fails task:**
- Dispatch fix subagent with specific instructions
- Don't try to fix manually (context pollution)

## Integration

**Required workflow skills:**
- **writing-plans** - REQUIRED: Creates the plan that this skill executes
- **requesting-code-review** - REQUIRED: Review after each task (see Step 3)
- **finishing-a-development-branch** - REQUIRED: Complete development after all tasks (see Step 7)

**Subagents must use:**
- **test-driven-development** - Subagents follow TDD for each task

**Alternative workflow:**
- **executing-plans** - Use for parallel session instead of same-session execution

## Smart Subagent Configuration

### Simple Implementation Subagent
You are implementing a straightforward development task.

Requirements:
- Follow TDD: test → implement → verify
- Keep changes minimal and focused
- Write clear, maintainable code
- Test all scenarios mentioned in task

### Complex Integration Subagent
You are implementing a complex integration task.

Requirements:
- Break down into smaller steps
- Consider all integration points
- Handle error scenarios thoroughly
- Write comprehensive tests
- Document integration approach

### Critical Security Subagent
You are implementing a security-critical task.

Requirements:
- Security-first approach
- Comprehensive threat modeling
- Multiple review checkpoints
- Extensive testing including edge cases
- Security validation before completion

## Task Complexity Analysis

### Simple Tasks
- **Description:** Single component, straightforward logic
- **Subagent Type:** general-purpose
- **Time Estimate:** 5-15 minutes
- **Review Level:** Basic code review

### Complex Tasks
- **Description:** Multiple components, complex integration
- **Subagent Type:** specialized (backend, frontend, testing)
- **Time Estimate:** 30-60 minutes
- **Review Level:** Comprehensive code review

### Critical Tasks
- **Description:** Security, performance, breaking changes
- **Subagent Type:** senior-developer
- **Time Estimate:** 60+ minutes
- **Review Level:** Senior code review + security analysis

## Intelligent Error Recovery

### handle-subagent-failure
```bash
# Advanced error handling and recovery
handle-subagent-failure() {
    local task_id=$1
    local error_type=$2
    local error_details=$3
    
    case $error_type in
        "implementation_failure")
            # Try simpler subagent or break down task
            break-down-task "$task_id"
            ;;
        "review_failure")
            # Try different reviewer or manual review
            fallback-to-manual-review "$task_id"
            ;;
        "test_failure")
            # Dispatch debugging subagent
            dispatch-debug-subagent "$task_id"
            ;;
    esac
}
```

## Advanced Task Analytics

- **Task Performance:** Track completion times and quality metrics
- **Subagent Performance:** Monitor subagent effectiveness and accuracy
- **Review Quality:** Analyze code review thoroughness and accuracy
- **Development Velocity:** Measure overall development speed and quality

## Team Collaboration Features

- **Task Assignment:** Automatic assignment based on developer expertise
- **Progress Visibility:** Real-time progress tracking for team leads
- **Quality Gates:** Automatic quality gates before proceeding
- **Knowledge Sharing:** Task completion notes and learning