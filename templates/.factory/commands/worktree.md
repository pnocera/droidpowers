# Git Worktree Command
Create isolated development workspaces with safety verification

## Usage
`/worktree [branch-name]` or `/worktree`

## Process
1. Detect existing worktree locations
2. Verify .gitignore safety requirements
3. Create isolated workspace with smart directory selection
4. Auto-detect and run project setup
5. Verify clean test baseline

$ARGUMENTS

**Safety Features:**
- Automatic .gitignore verification and fixing
- Project-specific setup (npm, poetry, cargo, etc.)
- Clean baseline verification
- Permission and disk space checking

**Supported Project Types:**
- React/Vue/Angular: npm install, npm run dev-setup
- Python (Poetry): poetry install, pre-commit setup
- Python (Pip): pip install, test setup
- Rust: cargo build, cargo fetch
- Go: go mod download, go mod tidy
- TypeScript/Node: npm install, npm run build

**Integration:**
- brainstorming (automatic worktree creation)
- finishing-a-development-branch (automatic cleanup)
- subagent-driven-development (isolated task execution)
- executing-plans (worktree-based implementation)