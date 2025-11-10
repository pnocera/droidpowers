# Missing Critical Droids Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement 6 missing critical droids and complete command coverage to achieve 100% feature parity with superpowers system

**Architecture:** Create missing droids following existing Factory AI patterns, maintain gateway routing logic, and ensure full integration with existing command system

**Tech Stack:** Factory AI CLI, Markdown-based droids, MCP tools, existing superpowers patterns

---

## Task 1: Root-Cause-Tracing Droid Implementation

**Files:**
- Create: `.factory/droids/root-cause-tracing.md`
- Create: `.factory/commands/root-cause-tracing.md`
- Modify: `.factory/droids/systematic-debugging.md` (update dependency reference)

**Step 1: Create the root-cause-tracing droid markdown file**

```markdown
# Root Cause Tracing

## Overview

Use when errors occur deep in execution and you need to trace back to find the original trigger - systematically traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior.

## Usage

Run this droid when:
- An error occurs deep in the execution stack
- You need to find the original source of a problem
- Bugs are symptoms rather than root causes
- Multiple layers of code are involved

## Process

### Phase 1: Error Analysis
1. **Identify the failure point** - Where did the error manifest?
2. **Map the call stack** - What led to this failure?
3. **Document symptoms** - What are the observable effects?

### Phase 2: Backward Tracing
1. **Trace data flow** - Follow invalid data backward
2. **Check call chain** - Examine each function in the stack
3. **Add instrumentation** - Insert logging/checkpoints as needed

### Phase 3: Source Identification
1. **Locate origin** - Find where the problem first appeared
2. **Verify hypothesis** - Confirm this is the root cause
3. **Document findings** - Clear explanation of the source

## Integration

**Required by:** systematic-debugging
**Integrates with:** test-driven-development, verification-before-completion

## Examples

See superpowers skills for detailed examples and common patterns.
```

**Step 2: Create the command file**

```markdown
# Root Cause Tracing Command

Factory AI command implementation for root-cause-tracing droid.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/root-cause-tracing.md .factory/commands/root-cause-tracing.md`
Expected: Both files exist

**Step 4: Update systematic-debugging dependency reference**

**Step 5: Commit**

```bash
git add .factory/droids/root-cause-tracing.md .factory/commands/root-cause-tracing.md .factory/droids/systematic-debugging.md
git commit -m "feat: add root-cause-tracing droid and command"
```

---

## Task 2: Finishing-a-Development-Branch Droid Implementation

**Files:**
- Create: `.factory/droids/finishing-a-development-branch.md`
- Create: `.factory/commands/finish-branch.md`
- Modify: `.factory/droids/subagent-driven-development.md` (update reference)

**Step 1: Create the finishing-a-development-branch droid**

```markdown
# Finishing a Development Branch

## Overview

Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup.

## Usage

Run this droid when:
- Implementation is complete
- All tests are passing
- You need to decide next steps for integration

## Process

### Phase 1: Completion Assessment
1. **Verify implementation** - Is the feature complete?
2. **Check test coverage** - Are all scenarios tested?
3. **Review quality** - Does code meet standards?

### Phase 2: Integration Options
1. **Create Pull Request** - For review and collaboration
2. **Direct Merge** - For simple changes
3. **Cleanup and Archive** - For experimental work

### Phase 3: Next Steps
1. **Execute chosen option** - Follow the selected path
2. **Clean up workspace** - Remove temporary files
3. **Update documentation** - Ensure docs are current

## Integration

**Required by:** multiple skills for workflow completion
**Integrates with:** verification-before-completion, requesting-code-review

## Options Presented

- Create PR with comprehensive description
- Direct merge to main branch
- Feature branch cleanup
- Documentation updates
```

**Step 2: Create the command file**

```markdown
# Finish Branch Command

Factory AI command for finishing development branches.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/finishing-a-development-branch.md .factory/commands/finish-branch.md`
Expected: Both files exist

**Step 4: Update references in subagent-driven-development**

**Step 5: Commit**

```bash
git add .factory/droids/finishing-a-development-branch.md .factory/commands/finish-branch.md .factory/droids/subagent-driven-development.md
git commit -m "feat: add finishing-a-development-branch droid and command"
```

---

## Task 3: Dispatching-Parallel-Agents Droid Implementation

**Files:**
- Create: `.factory/droids/dispatching-parallel-agents.md`
- Create: `.factory/commands/parallel.md`

**Step 1: Create the dispatching-parallel-agents droid**

```markdown
# Dispatching Parallel Agents

## Overview

Use when facing 3+ independent failures that can be investigated without shared state or dependencies - dispatches multiple Claude agents to investigate and fix independent problems concurrently.

## Usage

Run this droid when:
- Multiple independent failures exist
- Problems can be solved in parallel
- No shared state between issues
- Need faster resolution through concurrency

## Process

### Phase 1: Problem Analysis
1. **Identify independent issues** - Separate distinct problems
2. **Verify no dependencies** - Ensure problems don't share state
3. **Assign agents** - Create specific tasks for each agent

### Phase 2: Parallel Dispatch
1. **Launch multiple agents** - Send independent tasks simultaneously
2. **Monitor progress** - Track each agent's work
3. **Coordinate results** - Combine solutions as needed

### Phase 3: Integration
1. **Review all solutions** - Verify each fix works
2. **Test combined system** - Ensure fixes work together
3. **Document results** - Record what was fixed and how

## Requirements

- Minimum 3 independent failures
- No shared state between problems
- Clear separation of concerns

## Integration

**Advanced workflow** for complex debugging scenarios
**Integrates with:** systematic-debugging, test-driven-development
```

**Step 2: Create the command file**

```markdown
# Parallel Command

Factory AI command for dispatching parallel agents.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/dispatching-parallel-agents.md .factory/commands/parallel.md`
Expected: Both files exist

**Step 4: Commit**

```bash
git add .factory/droids/dispatching-parallel-agents.md .factory/commands/parallel.md
git commit -m "feat: add dispatching-parallel-agents droid and command"
```

---

## Task 4: Testing-Anti-Patterns Droid Implementation

**Files:**
- Create: `.factory/droids/testing-anti-patterns.md`
- Create: `.factory/commands/anti-patterns.md`

**Step 1: Create the testing-anti-patterns droid**

```markdown
# Testing Anti-Patterns

## Overview

Use when writing or changing tests, adding mocks, or tempted to add test-only methods to production code - prevents testing mock behavior, production pollution with test-only methods, and mocking without understanding dependencies.

## Usage

Run this droid when:
- Writing new tests
- Adding mocks to tests
- Tempted to add test-only methods to production
- Reviewing existing test code

## Common Anti-Patterns

### 1. Mock Behavior Testing
- **Problem:** Testing how mocks work instead of real behavior
- **Solution:** Test real interactions, use mocks sparingly

### 2. Production Code Pollution
- **Problem:** Adding test-only methods to production code
- **Solution:** Keep test concerns separate from production

### 3. Mocking Without Understanding
- **Problem:** Mocking dependencies you don't understand
- **Solution:** Understand dependencies before mocking

### 4. Test-Only Methods
- **Problem:** Creating methods just for testing
- **Solution:** Test the public interface, not internals

## Prevention Checklist

- [ ] No test-only methods in production code
- [ ] Mocks represent real dependencies accurately
- [ ] Tests verify actual behavior, not mock behavior
- [ ] Production code remains test-agnostic
- [ ] No testing-specific logic in production

## Integration

**Educational component** for maintaining test quality
**Integrates with:** test-driven-development, verification-before-completion
```

**Step 2: Create the command file**

```markdown
# Anti-Patterns Command

Factory AI command for testing anti-patterns prevention.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/testing-anti-patterns.md .factory/commands/anti-patterns.md`
Expected: Both files exist

**Step 4: Commit**

```bash
git add .factory/droids/testing-anti-patterns.md .factory/commands/anti-patterns.md
git commit -m "feat: add testing-anti-patterns droid and command"
```

---

## Task 5: Testing-Skills-With-Subagents Droid Implementation

**Files:**
- Create: `.factory/droids/testing-skills-with-subagents.md`
- Create: `.factory/commands/test-skills.md`

**Step 1: Create the testing-skills-with-subagents droid**

```markdown
# Testing Skills With Subagents

## Overview

Use when creating or editing skills, before deployment, to verify they work under pressure and resist rationalization - applies RED-GREEN-REFACTOR cycle to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization.

## Usage

Run this droid when:
- Creating new skills or droids
- Editing existing skills
- Before deploying skills to production
- Validating skill robustness

## RED-GREEN-REFACTOR for Skills

### RED: Test Without Skill
1. **Run baseline test** - Verify failure without skill
2. **Document expected behavior** - What should skill accomplish?
3. **Identify gaps** - Where does baseline fall short?

### GREEN: Write Skill to Address Failures
1. **Implement minimal skill** - Address specific test failures
2. **Test with subagents** - Verify skill works in practice
3. **Ensure skill passes tests** - Confirm behavior matches expectations

### REFACTOR: Improve and Strengthen
1. **Refine documentation** - Make instructions clearer
2. **Add edge cases** - Handle more scenarios
3. **Test thoroughly** - Verify skill resists rationalization

## Testing Process

### Baseline Testing
- Run task without the skill
- Document failure modes
- Establish success criteria

### Skill Validation
- Test skill with various inputs
- Verify it handles edge cases
- Ensure it resists workarounds

### Subagent Testing
- Have subagents test the skill
- Verify skill works with different agents
- Check for consistent behavior

## Integration

**Meta-skill** for skill validation and quality assurance
**Integrates with:** writing-skills, subagent-driven-development
```

**Step 2: Create the command file**

```markdown
# Test Skills Command

Factory AI command for testing skills with subagents.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/testing-skills-with-subagents.md .factory/commands/test-skills.md`
Expected: Both files exist

**Step 4: Commit**

```bash
git add .factory/droids/testing-skills-with-subagents.md .factory/commands/test-skills.md
git commit -m "feat: add testing-skills-with-subagents droid and command"
```

---

## Task 6: Sharing-Skills Droid Implementation

**Files:**
- Create: `.factory/droids/sharing-skills.md`
- Create: `.factory/commands/share.md`

**Step 1: Create the sharing-skills droid**

```markdown
# Sharing Skills

## Overview

Use when you've developed a broadly useful skill and want to contribute it upstream via pull request - guides process of branching, committing, pushing, and creating PR to contribute skills back to upstream repository.

## Usage

Run this droid when:
- You've developed a useful skill
- Want to contribute back to superpowers project
- Ready to share improvements with community

## Contribution Process

### Phase 1: Preparation
1. **Verify skill quality** - Ensure skill is well-tested
2. **Document thoroughly** - Clear usage instructions
3. **Check compatibility** - Ensure it fits upstream standards

### Phase 2: Repository Operations
1. **Create feature branch** - Isolated work environment
2. **Commit changes** - Clear commit messages
3. **Push to remote** - Make changes available

### Phase 3: Pull Request
1. **Create PR** - Detailed description of changes
2. **Fill contribution form** - Complete required information
3. **Address feedback** - Respond to review comments

## Contribution Guidelines

### Quality Standards
- Skills must be thoroughly tested
- Documentation must be complete
- Code must follow project conventions
- Skills should solve real problems

### PR Requirements
- Clear description of the skill
- Examples of usage
- Testing instructions
- Benefits for the community

## Integration

**Contribution workflow** for community engagement
**Integrates with:** writing-skills, testing-skills-with-subagents

## Best Practices

- Start with small, focused contributions
- Engage with the community
- Respond to feedback promptly
- Follow project coding standards
```

**Step 2: Create the command file**

```markdown
# Share Command

Factory AI command for sharing skills upstream.
```

**Step 3: Run tests to verify structure**

Run: `ls .factory/droids/sharing-skills.md .factory/commands/share.md`
Expected: Both files exist

**Step 4: Commit**

```bash
git add .factory/droids/sharing-skills.md .factory/commands/share.md
git commit -m "feat: add sharing-skills droid and command"
```

---

## Task 7: Update Gateway Droids and Documentation

**Files:**
- Modify: `.factory/droids/using-droids.md` (add new droids to overview)
- Modify: `.factory/droids/skill-checker.md` (update routing logic)
- Modify: `README.md` (update droid count and coverage)
- Modify: `USAGE.md` (add new commands)

**Step 1: Update using-droids overview**

**Step 2: Update skill-checker routing**

**Step 3: Update README with new droid count (21 total)**

**Step 4: Update USAGE.md with 6 new commands**

**Step 5: Commit**

```bash
git add .factory/droids/using-droids.md .factory/droids/skill-checker.md README.md USAGE.md
git commit -m "docs: update gateway droids and documentation for missing skills"
```

---

## Task 8: Create Test Coverage for New Droids

**Files:**
- Create: `tests/droids/test-root-cause-tracing.py`
- Create: `tests/droids/test-finishing-branch.py`
- Create: `tests/droids/test-dispatching-parallel.py`
- Create: `tests/droids/test-testing-anti-patterns.py`
- Create: `tests/droids/test-testing-skills.py`
- Create: `tests/droids/test-sharing-skills.py`

**Step 1: Create test for root-cause-tracing droid**

```python
def test_root_cause_tracing_droid_exists():
    """Test that root-cause-tracing droid is properly implemented."""
    droid_path = ".factory/droids/root-cause-tracing.md"
    assert os.path.exists(droid_path), "Root cause tracing droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Root Cause Tracing" in content, "Should have correct title"
        assert "systematic-debugging" in content, "Should reference dependent skills"

def test_root_cause_tracing_command_exists():
    """Test that root-cause-tracing command is implemented."""
    command_path = ".factory/commands/root-cause-tracing.md"
    assert os.path.exists(command_path), "Root cause tracing command should exist"
```

**Step 2: Create test for finishing-branch droid**

**Step 3: Create test for dispatching-parallel droid**

**Step 4: Create test for testing-anti-patterns droid**

**Step 5: Create test for testing-skills droid**

**Step 6: Create test for sharing-skills droid**

**Step 7: Run all tests**

Run: `python -m pytest tests/droids/ -v`
Expected: All tests pass

**Step 8: Commit**

```bash
git add tests/droids/
git commit -m "test: add coverage for 6 new droids and commands"
```

---

## Task 9: Final Verification and Integration

**Files:**
- Create: `scripts/verify-completeness.py`
- Modify: `AGENTS.md.template` (update droid references)

**Step 1: Create completeness verification script**

```python
#!/usr/bin/env python3
"""Verify that all critical droids are implemented."""

import os
import sys

REQUIRED_DROIDS = [
    "test-driven-development",
    "systematic-debugging", 
    "brainstorming",
    "verification-before-completion",
    "condition-based-waiting",
    "defense-in-depth",
    "writing-plans",
    "executing-plans",
    "requesting-code-review",
    "receiving-code-review",
    "using-git-worktrees",
    "subagent-driven-development",
    "root-cause-tracing",           # NEW
    "finishing-a-development-branch", # NEW
    "dispatching-parallel-agents",  # NEW
    "testing-anti-patterns",        # NEW
    "testing-skills-with-subagents", # NEW
    "sharing-skills",               # NEW
    "writing-skills",
    "using-droids",
    "skill-checker"
]

def verify_droids():
    """Check that all required droids exist."""
    missing = []
    for droid in REQUIRED_DROIDS:
        droid_path = f".factory/droids/{droid}.md"
        if not os.path.exists(droid_path):
            missing.append(droid)
    
    if missing:
        print(f"❌ Missing droids: {missing}")
        return False
    else:
        print(f"✅ All {len(REQUIRED_DROIDS)} droids implemented")
        return True

if __name__ == "__main__":
    success = verify_droids()
    sys.exit(0 if success else 1)
```

**Step 2: Run verification script**

Run: `python scripts/verify-completeness.py`
Expected: "✅ All 21 droids implemented"

**Step 3: Update AGENTS.md.template references**

**Step 4: Final integration test**

Run: `find .factory -name "*.md" | wc -l`
Expected: 42+ files (21 droids + 21 commands)

**Step 5: Create final summary**

Run: `ls .factory/droids/ | wc -l && ls .factory/commands/ | wc -l`
Expected: 21 droids and 21 commands

**Step 6: Commit**

```bash
git add scripts/verify-completeness.py AGENTS.md.template
git commit -m "feat: complete missing critical droids implementation - 100% feature parity achieved"
```

---

## Summary

This implementation plan addresses all 6 missing critical droids identified in the analysis:

1. **root-cause-tracing** - Required by systematic-debugging
2. **finishing-a-development-branch** - Required by multiple skills  
3. **dispatching-parallel-agents** - Advanced parallel execution
4. **testing-anti-patterns** - Educational component for test quality
5. **testing-skills-with-subagents** - Meta-skill for validation
6. **sharing-skills** - Contribution workflow

**Result:** 100% feature parity with superpowers system (21/21 droids implemented)

**Next Steps:** Run @verification-before-completion to validate implementation quality.