# Droidpowers Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Adapt the Claude Code superpowers skills system to work with Factory AI's configuration system using Custom Droids, slash commands, and AGENTS.md while maintaining mandatory workflow enforcement.

**Architecture:** Hybrid approach mapping superpowers skills to Factory AI's configuration system through three mechanisms: Custom Droids for complex workflows, slash commands for quick actions, and AGENTS.md for project-specific configuration and discovery.

**Tech Stack:** Factory AI CLI, Custom Droids (YAML + Markdown), slash commands, AGENTS.md configuration, project templates.

---

### Task 1: Project Infrastructure Setup

**Files:**
- Create: `.factory/droids/` (directory)
- Create: `.factory/commands/` (directory)
- Create: `docs/plans/` (directory)
- Create: `README.md`

**Step 1: Create project README**

```markdown
# Droidpowers

Factory AI adaptation of the superpowers skills system - maintaining rigorous workflow enforcement with enhanced discoverability.

## Quick Start

1. Install Factory AI CLI
2. Copy droids to `.factory/droids/`
3. Copy commands to `.factory/commands/`
4. Add AGENTS.md to project root
5. Start using enhanced workflows!

## Skills Available

### Core Droids
- `/droid test-driven-development` - TDD enforcement
- `/droid systematic-debugging` - Bug investigation workflow
- `/droid brainstorming` - Idea refinement and design

### Quick Commands
- `/tdd` - Start TDD workflow
- `/debug` - Begin systematic debugging
- `/brainstorm [topic]` - Refine ideas into designs

### Project Configuration
- AGENTS.md - Project-specific skill recommendations
- skill-checker droid - Automatic skill discovery
```

**Step 2: Commit project setup**

```bash
git add README.md
git commit -m "feat: initial droidpowers project structure and README"
```

### Task 2: Gateway Droid Implementation

**Files:**
- Create: `.factory/droids/skill-checker.md`

**Step 1: Write the gateway droid**

```markdown
---
name: skill-checker
description: Analyzes tasks and enforces mandatory skill usage - maintains superpowers workflow enforcement in Factory AI
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash]
---

# Skill Checker Gateway Droid

## Purpose
Enforces the superpowers principle: "If you think there is even a 1% chance a skill might apply to what you're doing, you ABSOLUTELY MUST use it."

## Task Analysis
1. Analyze current working directory and files
2. Identify task type from user request
3. Match against skill applicability patterns
4. Enforce mandatory skill usage

## Applicability Patterns

### Always Required
- **test-driven-development**: Any code implementation, feature additions, bug fixes
- **verification-before-completion**: Before commits, PRs, or declaring work done
- **systematic-debugging**: For any investigation of errors, bugs, unexpected behavior

### Task-Specific
- **brainstorming**: New features, architecture, design decisions
- **writing-plans**: Complex implementations, multi-step tasks
- **code-reviewer**: After completing significant work
- **using-git-worktrees**: Feature development that needs isolation

## Enforcement Logic
```yaml
if task involves "implement", "add", "create", "fix":
    enforce: "test-driven-development"
    
if task involves "bug", "error", "broken", "failing":
    enforce: "systematic-debugging"
    
if task involves "design", "plan", "architecture":
    enforce: "brainstorming"
    
if task involves "review", "check", "validate":
    enforce: "verification-before-completion"
```

## Usage
Always invoke skill-checker before starting any significant task. It will redirect you to the appropriate skill droid.
```

**Step 2: Commit gateway droid**

```bash
git add .factory/droids/skill-checker.md
git commit -m "feat: implement skill-checker gateway droid for workflow enforcement"
```

### Task 3: Core TDD Droid Implementation

**Files:**
- Create: `.factory/droids/test-driven-development.md`

**Step 1: Implement TDD enforcement droid**

```markdown
---
name: test-driven-development
description: STRICT TDD enforcement - NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
model: claude-sonnet-4-5
tools: [Write, Read, Edit, Bash, Task, TodoWrite]
---

# Test-Driven Development Droid

## IRON LAW
**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST**
**NO SKILL WITHOUT A FAILING TEST FIRST**

## Workflow Steps

### 1. Analysis Phase
- [ ] Understand requirements completely
- [ ] Identify test scenarios needed
- [ ] Plan test structure and organization

### 2. Red Phase - Write Failing Test
- [ ] Write test for desired behavior
- [ ] Run test - MUST FAIL with clear error
- [ ] Verify test failure makes sense

### 3. Green Phase - Minimal Implementation
- [ ] Write minimal code to make test pass
- [ ] Run test - MUST PASS
- [ ] Run all tests - ALL MUST PASS

### 4. Refactor Phase
- [ ] Improve code while keeping tests green
- [ ] Run tests continuously during refactoring
- [ ] Ensure no functionality changes

## Enforcement Checkpoints

### Before Writing Production Code
```bash
# Verify failing test exists
if [[ ! $(find . -name "*test*" -type f | grep -E "(test|spec)" | head -1) ]]; then
    echo "ERROR: No test files found. Write test first!"
    exit 1
fi

# Verify test fails
npm test || pytest || python -m pytest
```

### Before Committing
```bash
# All tests must pass
npm test && npm run lint
```

## Supported Test Types
- JavaScript/TypeScript: Jest, Vitest, Mocha
- Python: pytest, unittest
- Other: Generic test framework detection

## Error Handling
- If test doesn't fail initially: Check test logic
- If production code written first: STOP, write test first
- If tests fail after refactoring: Fix tests or revert code
```

**Step 2: Create TDD slash command**

**File:** `.factory/commands/tdd`

```markdown
# Test-Driven Development Quick Start

Enforces TDD workflow - NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST

## Usage
`tdd` or `tdd [feature-description]`

## Process
1. Analyzes current project structure
2. Identifies appropriate test framework
3. Starts TDD droid with full enforcement
4. Tracks compliance throughout workflow

$ARGUMENTS

**Getting Started:**
1. Write failing test first
2. Run test (must fail)  
3. Write minimal code to pass
4. Refactor while keeping green
5. Repeat for each feature

**REMEMBER: No production code without a failing test first!**
```

**Step 3: Make slash command executable**

```bash
chmod +x .factory/commands/tdd
```

**Step 4: Commit TDD implementation**

```bash
git add .factory/droids/test-driven-development.md .factory/commands/tdd
git commit -m "feat: implement TDD droid and slash command with strict enforcement"
```

### Task 4: Brainstorming Droid Implementation

**Files:**
- Create: `.factory/droids/brainstorming.md`
- Create: `.factory/commands/brainstorm`

**Step 1: Implement brainstorming droid**

```markdown
---
name: brainstorming
description: Refines rough ideas into fully-formed designs through collaborative questioning and incremental validation
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite]
---

# Brainstorming Droid

## Purpose
Turn ideas into fully-formed designs through natural collaborative dialogue.

## Process

### Understanding Phase
1. Check current project context (files, docs, recent commits)
2. Ask clarifying questions one at a time
3. Focus on: purpose, constraints, success criteria
4. Prefer multiple choice questions when possible

### Exploration Phase  
1. Propose 2-3 different approaches with trade-offs
2. Present options conversationally with recommendations
3. Lead with recommended option and explain reasoning
4. Explore alternatives thoroughly

### Design Presentation
1. Break design into sections (200-300 words each)
2. Present incrementally with validation checkpoints
3. Cover: architecture, components, data flow, error handling, testing
4. Be ready to go back and clarify as needed

### Documentation
1. Write validated design to `docs/plans/YYYY-MM-DD-<topic>-design.md`
2. Include implementation considerations and trade-offs
3. Commit design document to git
4. Link to project requirements

## Question Templates
- "For the [feature], what's your primary constraint: A) Performance, B) Maintainability, C) Speed of development, D) Something else?"
- "Which approach seems better: A) Simple solution with known limitations, B) Complex solution with future flexibility, C) Hybrid approach?"

## Design Checklist
- [ ] Requirements fully understood
- [ ] Multiple approaches explored
- [ ] Trade-offs clearly identified
- [ ] Stakeholder feedback incorporated
- [ ] Design documented
- [ ] Implementation plan created
```

**Step 2: Create brainstorming command**

```markdown
# Brainstorming Command

Refines rough ideas into fully-formed designs through collaborative questioning.

## Usage  
`/brainstorm [your idea or topic]`
`/brainstorm` (starts interactive session)

## Process
1. Analyzes current project context
2. Asks clarifying questions one at a time
3. Explores 2-3 approaches with trade-offs
4. Presents design in validated sections
5. Documents final design

$ARGUMENTS

**Perfect for:**
- New feature design
- Architecture decisions  
- Complex problem solving
- Technical planning
```

**Step 3: Make command executable**

```bash
chmod +x .factory/commands/brainstorm
```

**Step 4: Commit brainstorming implementation**

```bash
git add .factory/droids/brainstorming.md .factory/commands/brainstorm
git commit -m "feat: implement brainstorming droid and command for collaborative design"
```

### Task 5: Project Configuration Template

**Files:**
- Create: `AGENTS.md.template`

**Step 1: Create AGENTS.md template**

```markdown
# Project Skills Configuration

## Project Overview
**Project Type:** [React/Node.js/Python/etc]
**Primary Language:** [JavaScript/TypeScript/Python/etc]
**Build System:** [npm/yarn/pip/etc]

## Mandatory Skills
- **test-driven-development**: All feature implementation and bug fixes
- **verification-before-completion**: Before any commits or pull requests
- **systematic-debugging**: For any bug investigation or unexpected behavior

## Recommended Skills
- **brainstorming**: For new features, architecture changes, complex implementations
- **writing-plans**: For multi-step tasks and major features
- **code-reviewer**: After completing significant work items
- **using-git-worktrees**: For feature development and experimental work

## Workflow Rules
1. **Always check skill-checker** before starting any task
2. **Use indicated skills** for corresponding work types  
3. **Complete all checklists** before proceeding to next step
4. **Validate completion** before marking work as done
5. **Document designs** before implementation

## Build Commands
```bash
# Install dependencies
[install-command]

# Run tests
[test-command]

# Build project
[build-command]

# Lint code
[lint-command]
```

## Architecture
### Directory Structure
```
[describe key directories and their purposes]
```

### Key Components
- [Component 1]: [purpose and location]
- [Component 2]: [purpose and location]
- [Component 3]: [purpose and location]

## Testing Strategy
- **Unit Tests:** [location and framework]
- **Integration Tests:** [location and framework]  
- **End-to-End Tests:** [location and framework]
- **Coverage Target:** [percentage or requirement]

## Development Workflow
1. Create feature branch from main
2. Use test-driven-development for implementation
3. Run verification-before-completion before commits
4. Create pull request with code-reviewer
5. Address feedback and iterate

## Team Conventions
- **Commit Format:** [conventional commits or other format]
- **Branch Naming:** [pattern for feature branches]
- **Code Style:** [linter config, formatting rules]
- **Documentation:** [where and how to document]
```

**Step 2: Commit project template**

```bash
git add AGENTS.md.template
git commit -m "feat: add AGENTS.md template for project-specific skill configuration"
```

### Task 6: Usage Documentation

**Files:**
- Create: `USAGE.md`
- Create: `MIGRATION.md`

**Step 1: Create usage guide**

```markdown
# Droidpowers Usage Guide

## Quick Start

1. **Install** Factory AI CLI
2. **Copy droids** to `.factory/droids/` in your project
3. **Copy commands** to `.factory/commands/` in your project  
4. **Configure** project by copying `AGENTS.md.template` to `AGENTS.md`
5. **Start** using enhanced workflows!

## Available Skills

### Droids (Full Workflows)
Access via Factory AI Task tool:
- `skill-checker` - Gateway droid for skill discovery and enforcement
- `test-driven-development` - Strict TDD workflow enforcement
- `brainstorming` - Collaborative design refinement
- `systematic-debugging` - Four-phase bug investigation
- `verification-before-completion` - Pre-commit validation

### Commands (Quick Actions)
- `/tdd` - Start TDD workflow
- `/brainstorm [topic]` - Refine ideas into designs
- `/debug` - Begin systematic debugging
- `/verify` - Run completion verification
- `/plan [task]` - Create detailed implementation plan

## Example Workflows

### Adding a New Feature
```bash
# 1. Check if skills apply
/droid skill-checker "Add user authentication"

# 2. Design the feature (if recommended)
/brainstorm user authentication system

# 3. Implement with TDD
/tdd user login functionality

# 4. Verify before committing
/verify
```

### Debugging an Issue
```bash
# 1. Start systematic debugging
/droid systematic-debugging "User login failing"

# 2. Follow the four-phase process:
#    - Root cause investigation
#    - Pattern analysis  
#    - Hypothesis testing
#    - Implementation

# 3. Verify fix
/verify
```

### Code Review Process
```bash
# 1. After completing work
/droid code-reviewer

# 2. Address feedback
/droid receiving-code-review

# 3. Final verification
/verify
```

## Project Configuration

Each project should have an `AGENTS.md` file that specifies:
- Project type and technology stack
- Mandatory vs recommended skills
- Build and test commands
- Team conventions and workflows

## Enforcement Mechanisms

The system maintains superpowers' rigorous enforcement through:

1. **Gateway Droid**: skill-checker analyzes tasks and enforces skill usage
2. **Embedded Validation**: Each droid includes self-checking logic
3. **Project Configuration**: AGENTS.md defines mandatory workflows
4. **Interactive Prompts**: Warnings when applicable skills are skipped

## Compliance Tracking

Projects can track:
- Skill usage frequency
- Workflow compliance rates
- Quality metrics (test coverage, bug reduction)
- Development velocity impact
```

**Step 2: Create migration guide**

```markdown
# Superpowers to Droidpowers Migration Guide

## Overview
This guide helps users migrate from Claude Code superpowers to Factory AI droidpowers while maintaining workflow benefits.

## Key Differences

### Superpowers (Claude Code)
- Plugin-based installation
- Automatic skill discovery via Skill tool
- Session hooks for mandatory usage
- Marketplace distribution

### Droidpowers (Factory AI)
- File-based configuration
- Manual setup per project
- Gateway droid for enforcement
- Project-specific customization

## Migration Steps

### 1. Project Setup
```bash
# Create Factory AI directories
mkdir -p .factory/{droids,commands}

# Copy droid files
cp droidpowers/.factory/droids/* .factory/droids/
cp droidpowers/.factory/commands/* .factory/commands/

# Configure project
cp droidpowers/AGENTS.md.template AGENTS.md
# Edit AGENTS.md for your specific project
```

### 2. Skill Mapping

| Superpowers Skill | Droidpowers Equivalent |
|-------------------|----------------------|
| Skill tool discovery | `/droid skill-checker` |
| test-driven-development | `/droid test-driven-development` or `/tdd` |
| brainstorming | `/droid brainstorming` or `/brainstorm` |
| systematic-debugging | `/droid systematic-debugging` or `/debug` |
| verification-before-completion | `/droid verification` or `/verify` |

### 3. Workflow Adaptation

**Before (Superpowers):**
```
User asks to implement feature
→ Claude automatically checks for applicable skills
→ Uses mandatory skill if found
→ Follows skill workflow exactly
```

**After (Droidpowers):**
```
User asks to implement feature
→ Claude runs skill-checker droid
→ Identifies mandatory skills
→ Routes to appropriate droid/command
→ Follows same workflow with enforcement
```

### 4. Maintaining Compliance

The same "ABSOLUTELY MUST use skill" rule applies, enforced through:
- skill-checker gateway analysis
- Droid internal validation logic
- Project configuration in AGENTS.md
- Interactive compliance prompts

## Benefits of Migration

1. **Enhanced Discovery**: Factory AI's configuration system provides better project-specific skill matching
2. **Flexible Integration**: Mix and match skills with other Factory AI tools
3. **Improved Customization**: Adapt skills to specific project needs
4. **Better Documentation**: AGENTS.md provides comprehensive project context
5. **Team Collaboration**: Easier to share and standardize workflows across teams

## Testing Migration

1. **Test with existing project**: Try droidpowers on a familiar codebase
2. **Compare workflows**: Verify same outcomes as superpowers
3. **Check enforcement**: Ensure mandatory usage still works
4. **Team validation**: Get feedback from team members

## Troubleshooting

### Skill Not Detected
- Check AGENTS.md configuration
- Verify droid files are in correct location
- Run skill-checker manually: `/droid skill-checker`

### Enforcement Not Working
- Ensure skill-checker droid is installed
- Check project-specific skill rules in AGENTS.md
- Verify droid permissions and executable status

### Workflow Differences
- Compare original SKILL.md with new droid implementation
- Check for missing validation steps
- Verify all checkpoints are preserved
```

**Step 3: Commit documentation**

```bash
git add USAGE.md MIGRATION.md
git commit -m "docs: add comprehensive usage and migration guides"
```

### Task 7: Validation and Testing

**Files:**
- Create: `tests/` (directory)
- Create: `tests/test-droid-functionality.md`

**Step 1: Create test validation file**

```markdown
# Droidpowers Testing Guide

## Manual Testing Checklist

### Gateway Droid (skill-checker)
- [ ] Detects "implement" tasks → routes to TDD
- [ ] Detects "debug" tasks → routes to systematic-debugging  
- [ ] Detects "design" tasks → routes to brainstorming
- [ ] Enforces mandatory skill usage
- [ ] Provides clear routing instructions

### TDD Droid
- [ ] Enforces "no code without test first" rule
- [ ] Validates test failure before implementation
- [ ] Ensures minimal implementation approach
- [ ] Maintains test during refactoring
- [ ] Supports multiple test frameworks

### Brainstorming Droid
- [ ] Asks clarifying questions one at a time
- [ ] Explores multiple approaches
- [ ] Presents design incrementally
- [ ] Documents final design
- [ ] Creates implementation plan

### Slash Commands
- [ ] `/tdd` launches TDD workflow correctly
- [ ] `/brainstorm` starts collaborative design
- [ ] Commands accept arguments properly
- [ ] Error handling works for missing arguments

### Project Configuration
- [ ] AGENTS.md template works for different project types
- [ ] Skills correctly mapped to project needs
- [ ] Build commands integrate properly
- [ ] Team conventions documented clearly

## Automated Testing

### Droid YAML Validation
```bash
# Validate all droid YAML frontmatter
for droid in .factory/droids/*.md; do
    echo "Validating $droid"
    # Add YAML validation command
done
```

### Command Permissions
```bash
# Ensure all commands are executable
find .factory/commands -type f -exec chmod +x {} \;
find .factory/commands -type f -exec test -x {} \; -print
```

### Integration Tests
- Test skill discovery with various project types
- Verify enforcement mechanisms work
- Check compliance tracking functionality
- Validate migration from superpowers

## Performance Testing

- Droid loading time: < 2 seconds
- Skill analysis time: < 1 second  
- Command response time: < 500ms
- Memory usage: < 50MB per active droid
```

**Step 2: Commit test framework**

```bash
git add tests/test-droid-functionality.md
git commit -m "test: add comprehensive testing framework and validation checklist"
```

---

## Implementation Complete

**Total Estimated Time:** 2-3 weeks for full implementation
**Critical Path:** Gateway droid → Core skills (TDD, brainstorming) → Project configuration
**Success Criteria:** 
- All core superpowers skills successfully migrated
- Workflow enforcement mechanisms preserved
- Project-specific customization working
- Migration path documented and tested
- Team adoption possible within 1 week

## Next Steps After Implementation

1. **Extended Skills Migration**: Convert remaining 14 superpowers skills
2. **Advanced Features**: Skill chaining, analytics, team collaboration
3. **Community Sharing**: Marketplace for custom droids and configurations
4. **Integration Tools**: IDE plugins, CI/CD integration, dashboards