# Subagent-Driven Development Command
Execute implementation plans with fresh subagents and code review checkpoints

## Usage
`/subdev [plan-file]` or `/subdev`

## Process
1. Load and analyze implementation plan
2. Create TodoWrite task tracking
3. Dispatch optimized subagents per task
4. Automated code review between tasks
5. Continuous progress reporting

$ARGUMENTS

**Features:**
- Fresh subagent per task (no context pollution)
- Automatic code review checkpoints
- Issue fixing before proceeding
- Task completion tracking

**Workflow:**
- Load plan → Create tasks → Dispatch subagents → Review → Fix → Complete
- Fresh subagent per task with specialized prompts
- Code review automation between tasks
- Continuous progress tracking with TodoWrite

**Integration:**
- writing-plans (plan creation)
- requesting-code-review (automated reviews)
- finishing-a-development-branch (completion workflow)
- test-driven-development (subagent TDD)