# Droidpowers Usage Guide

## Quick Start

1. **Copy** `.factory/` directory to your project
2. **Configure** by copying `AGENTS.md.template` to `AGENTS.md`
3. **Start** with `/droid using-droids` before any task
4. **Follow** automatic skill routing recommendations

## Complete Droid Reference (15 Droids)

### Gateway Droids (Always use first)
- `/droid using-droids` - Mandatory task analysis and droid discovery
- `/droid skill-checker` - Automatic routing to applicable droids

### Core Skills (Essential workflows)
- `/droid test-driven-development` - Strict TDD with RED-GREEN-REFACTOR
- `/droid systematic-debugging` - Four-phase bug investigation framework  
- `/droid brainstorming` - Collaborative design through questioning
- `/droid verification-before-completion` - Pre-commit validation and quality gates
- `/droid writing-skills` - TDD approach to droid creation

### Advanced Skills (Specialized workflows)
- `/droid condition-based-waiting` - Eliminate flaky tests with condition polling
- `/droid defense-in-depth` - Multi-layer validation for robust systems
- `/droid writing-plans` - Comprehensive implementation planning
- `/droid executing-plans` - Batch execution with review checkpoints
- `/droid requesting-code-review` - Code review dispatch and coordination
- `/droid receiving-code-review` - Technical evaluation of feedback
- `/droid using-git-worktrees` - Isolated development environments
- `/droid subagent-driven-development` - Parallel task execution

## Complete Command Reference (14 Commands)

All commands are accessible via Factory AI CLI:

### Core Commands
- `/tdd` - Start TDD workflow
- `/debug` - Begin systematic debugging
- `/brainstorm` - Design refinement through questioning
- `/verify` - Pre-commit validation
- `/plan` - Create detailed implementation plan
- `/execute` - Execute planned tasks in batches

### Code Review Commands
- `/review` - Request code review
- `/handle-review` - Evaluate and apply feedback

### Advanced Commands
- `/worktree` - Git worktree management
- `/subdev` - Parallel development with subagents
- `/condition-wait` - Fix flaky tests and race conditions
- `/defense-in-depth` - Implement robust validation
- `/write-droid` - Create new droids following TDD
- `/droids` - Learn proper droid usage and discovery

## Example Workflows

### Creating a New Feature
```bash
# 1. Start with mandatory analysis
/droid using-droids
# Follow skill-checker recommendations

# 2. If recommended, design first
/droid brainstorming "user authentication system"

# 3. Implement with TDD (always required for code)
/droid test-driven-development

# 4. Verify before completion
/droid verification-before-completion

# 5. Request review for significant changes
/droid requesting-code-review
```

### Debugging a Problem
```bash
# 1. Start with task analysis
/droid using-droids
# skill-checker will route to systematic-debugging

# 2. Follow four-phase debugging process
/droid systematic-debugging

# 3. Verify fix is complete
/droid verification-before-completion
```

### Fixing Flaky Tests
```bash
# 1. Run task analysis
/droid using-droids
# skill-checker will route to condition-based-waiting

# 2. Apply condition-based patterns
/droid condition-based-waiting

# 3. Verify tests are stable
/droid verification-before-completion
```

### Creating Robust Validation
```bash
# 1. Start task analysis
/droid using-droids
# May route to defense-in-depth for critical systems

# 2. Apply four-layer validation
/droid defense-in-depth

# 3. Verify robustness
/droid verification-before-completion
```

## Project Configuration

Each project should have an `AGENTS.md` file that specifies:
- Project type, language, and build system
- Mandatory vs recommended droids for your stack
- Build, test, lint, and verification commands
- Directory structure and key components
- Team conventions and workflow rules

## Mandatory Workflow Enforcement

The system maintains superpowers' rigorous enforcement through:

1. **Gateway Analysis**: `using-droids` must run first for task analysis
2. **Automatic Routing**: `skill-checker` identifies applicable droids
3. **Embedded Validation**: Each droid includes self-checking logic
4. **Project Configuration**: AGENTS.md defines mandatory workflows
5. **Compliance Prompts**: Interactive warnings when applicable droids are skipped

## Simple Usage Checklist

Before any task:
- [ ] Run `/droid using-droids` for task analysis
- [ ] Follow `skill-checker` routing recommendations
- [ ] Create TodoWrite todos for all checklist items
- [ ] Complete all required checkpoints
- [ ] Run `/droid verification-before-completion` before declaring done

## Quality Benefits

Projects using droidpowers typically see:
- 100% test coverage compliance through TDD enforcement
- Elimination of flaky tests via condition-based waiting
- Robust validation systems through defense-in-depth patterns
- Systematic debugging with four-phase investigation
- Consistent code quality through verification gates
- Reduced bugs and improved development velocity