# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Droidpowers** is a complete Factory AI adaptation of the superpowers skills system with 100% feature parity and enhanced discoverability. It provides 15 specialized "droids" (skills) that enforce proven development workflows through Factory AI's CLI system.

**Project Type:** Skills/Droids system for Factory AI  
**Primary Components:** Markdown-based droids and commands  
**Architecture:** Gateway pattern with mandatory routing  

## Core Architecture

### Directory Structure
```
├─ .factory/               # Complete Factory AI integration
│  ├─ commands/           # 14 slash commands (tdd, debug, brainstorm, etc.)
│  └─ droids/             # 15 specialized droids with workflows
├─ superpowers/          # Original superpowers system (reference/backup)
│  ├─ agents/            # Subagent implementations
│  ├─ commands/          # Command wrappers for skills
│  ├─ hooks/             # Session initialization
│  ├─ lib/               # Utilities and initialization
│  └─ skills/            # Core skills (20+ specialized workflows)
├─ assets/               # Project images and documentation
└─ docs/                 # Additional documentation
```

### Key Components

- **Gateway Droids**: `using-droids` and `skill-checker` provide mandatory task analysis and routing
- **Core Skills**: Essential workflows like TDD, debugging, brainstorming, verification
- **Advanced Skills**: Specialized workflows for complex scenarios
- **Command System**: 14 slash commands provide quick access to droids
- **Factory Integration**: Full integration with Factory AI's `/droid` and `/command` systems

## Core Commands (Factory AI CLI)

### Essential Workflow Commands
- `/droid using-droids` - **MANDATORY** first step for all task analysis
- `/droid skill-checker` - Automatic routing to applicable droids
- `/droid test-driven-development` or `/tdd` - Strict TDD workflow
- `/droid verification-before-completion` or `/verify` - Pre-commit validation

### Development Commands
- `/droid brainstorming` or `/brainstorm` - Design refinement through questioning
- `/droid systematic-debugging` or `/debug` - Four-phase bug investigation
- `/droid writing-plans` or `/plan` - Comprehensive implementation planning
- `/droid executing-plans` or `/execute` - Batch execution with checkpoints

### Code Review Commands
- `/droid requesting-code-review` or `/review` - Code review dispatch
- `/droid receiving-code-review` or `/handle-review` - Technical feedback evaluation

### Advanced Commands
- `/droid condition-based-waiting` or `/condition-wait` - Fix flaky tests
- `/droid defense-in-depth` or `/defense-in-depth` - Multi-layer validation
- `/droid using-git-worktrees` or `/worktree` - Isolated development
- `/droid subagent-driven-development` or `/subdev` - Parallel task execution
- `/droid writing-skills` or `/write-droid` - Create new droids via TDD
- `/droid droids` or `/droids` - Learn droid usage and discovery

## Mandatory Workflows

### Non-Negotiable Rules
1. **Always** start with `/droid using-droids` for task analysis
2. **Always** follow `skill-checker` routing recommendations
3. **Always** use TodoWrite for checklist items
4. **Never** skip applicable droids - system enforces compliance
5. **Always** complete verification checkpoints before declaring done

### Core Skill Enforcement
- **test-driven-development**: Required for ANY code implementation
- **systematic-debugging**: Required for ANY bug investigation
- **verification-before-completion**: Required before commits/PRs
- **brainstorming**: Required for new features/architecture
- **writing-plans**: Required for complex implementations

## Development Workflow

### Standard Feature Development
```bash
# 1. Mandatory task analysis
/droid using-droids

# 2. Follow skill-checker routing (will direct to appropriate droids)
/droid skill-checker

# 3. Likely workflow for new features:
/droid brainstorming "feature description"
/droid writing-plans
/droid test-driven-development
/droid verification-before-completion

# 4. For significant changes:
/droid requesting-code-review
```

### Bug Fixing Workflow
```bash
# 1. Start with task analysis
/droid using-droids

# 2. Skill-checker will route to systematic-debugging
/droid systematic-debugging

# 3. Implement fix with TDD
/droid test-driven-development

# 4. Verify resolution
/droid verification-before-completion
```

## Droid System Architecture

### Gateway Pattern
- **using-droids**: Mandatory entry point that establishes workflow requirements
- **skill-checker**: Analyzes tasks and enforces mandatory skill usage
- **Automatic Routing**: Prevents workflow skipping through intelligent task analysis

### Skill Categories
- **Core Skills** (5): TDD, debugging, brainstorming, verification, writing-skills
- **Advanced Skills** (7): condition-waiting, defense-in-depth, planning, execution, review, git-worktrees, subagent-development
- **Gateway Skills** (2): using-droids, skill-checker

### Enforcement Mechanisms
- **Checklist Integration**: All droids with checklists require TodoWrite todos
- **Workflow Compliance**: System prevents skipping applicable droids
- **Quality Gates**: Verification droids ensure completion standards

## Project Configuration

### AGENTS.md Configuration
Projects should copy `AGENTS.md.template` to `AGENTS.md` and configure:
- Project type and language specifics
- Build/test/lint commands
- Directory structure
- Team conventions
- Mandatory vs recommended droids

### Factory Integration
- `.factory/` directory contains complete Factory AI setup
- Commands and droids are automatically available via Factory CLI
- Slash commands provide quick access to workflows
- Integration maintains superpowers' rigorous enforcement

## Key Principles

1. **Mandatory Compliance**: If a droid exists for a task, using it is required
2. **Evidence Over Claims**: Verification before declaring success
3. **Systematic Over Ad-hoc**: Proven workflows over guessing
4. **Quality First**: TDD and verification are non-negotiable
5. **Continuous Improvement**: All workflows include refinement mechanisms

## Common Gotchas

- **Skip Analysis**: Never skip `/droid using-droids` - it's mandatory
- **Ignore Routing**: Always follow `skill-checker` recommendations
- **Forget Todos**: Use TodoWrite for ALL checklist items
- **Adapt Rules**: Follow droid procedures exactly, don't adapt away discipline
- **Skip Verification**: Always run verification before declaring work complete

## Testing and Quality

- **TDD Enforcement**: All code implementation requires test-driven development
- **Verification Gates**: Pre-commit validation ensures quality standards
- **Systematic Debugging**: Four-phase process for thorough bug investigation
- **Anti-Pattern Prevention**: Skills include protection against common mistakes
- **Continuous Validation**: Workflow checkpoints maintain quality throughout development