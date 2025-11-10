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