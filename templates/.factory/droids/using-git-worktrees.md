---
name: using-git-worktrees
description: Creates isolated git worktrees with smart directory selection and safety verification
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__list_directory, mcp__desktop-commander__create_directory, mcp__desktop-commander__start_process]
---

# Using Git Worktrees Droid

## Overview

Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

## Directory Selection Process

Follow this priority order:

### 1. Check Existing Directories

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**If found:** Use that directory. If both exist, `.worktrees` wins.

### 2. Check AGENTS.md

```bash
grep -i "worktree.*director" AGENTS.md 2>/dev/null
```

**If preference specified:** Use it without asking.

### 3. Ask User

If no directory exists and no AGENTS.md preference:

```
No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. ~/.config/droidpowers/worktrees/<project-name>/ (global location)

Which would you prefer?
```

## Safety Verification

### For Project-Local Directories (.worktrees or worktrees)

**MUST verify .gitignore before creating worktree:**

```bash
# Check if directory pattern in .gitignore
grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore
```

**If NOT in .gitignore:**

Fix broken things immediately:
1. Add appropriate line to .gitignore
2. Commit the change
3. Proceed with worktree creation

**Why critical:** Prevents accidentally committing worktree contents to repository.

### For Global Directory (~/.config/droidpowers/worktrees)

No .gitignore verification needed - outside project entirely.

## Enhanced Project Type Detection

### Project Types and Setup Commands

#### React/Vue/Angular
```yaml
Detection Files:
  - package.json
  - vite.config.ts
  - webpack.config.js
  - angular.json

Setup Commands:
  - npm install
  - npm run dev-setup
  - npm test
  - npm run type-check
```

#### Python (Poetry)
```yaml
Detection Files:
  - pyproject.toml
  - poetry.lock

Setup Commands:
  - poetry install
  - poetry run pre-commit install
  - poetry run pytest
  - poetry run mypy
```

#### Python (Pip)
```yaml
Detection Files:
  - requirements.txt
  - setup.py

Setup Commands:
  - pip install -r requirements.txt
  - pip install -e .
  - pytest
  - python -m mypy
```

#### Rust
```yaml
Detection Files:
  - Cargo.toml
  - Cargo.lock

Setup Commands:
  - cargo build
  - cargo fetch
  - cargo test
  - cargo clippy
```

#### Go
```yaml
Detection Files:
  - go.mod
  - go.sum

Setup Commands:
  - go mod download
  - go mod tidy
  - go test ./...
  - go vet ./...
```

#### TypeScript/Node
```yaml
Detection Files:
  - tsconfig.json
  - package.json

Setup Commands:
  - npm install
  - npm run build
  - npm test
  - npm run type-check
```

## Enhanced Creation Steps

### 1. Detect Project Name
```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2. Safety Verification
```bash
# Pre-creation safety checks
verify-disk-space "$path"
verify-permissions "$path"
verify-git-health
fix-gitignore-if-needed "$location"
```

### 3. Create Worktree
```bash
# Determine full path
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/droidpowers/worktrees/*)
    path="~/.config/droidpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with enhanced error handling
git worktree add "$path" -b "$BRANCH_NAME" || {
    cleanup-on-failure "$path"
    return 1
}
```

### 4. Enhanced Project Setup
```bash
setup-project-environment() {
    local project_path=$1
    local project_type=$2
    
    case $project_type in
        "react"|"vue"|"angular")
            npm install
            npm run dev-setup
            ;;
        "python-poetry")
            poetry install
            poetry run pre-commit install
            ;;
        "python-pip")
            pip install -r requirements.txt
            pip install -e .
            ;;
        "rust")
            cargo build
            cargo fetch
            ;;
        "go")
            go mod download
            go mod tidy
            ;;
        "typescript"|"node")
            npm install
            npm run build
            ;;
    esac
}
```

### 5. Verify Clean Baseline
```bash
verify-clean-baseline() {
    local project_path=$1
    local project_type=$2
    
    case $project_type in
        "react"|"vue"|"angular")
            npm test
            ;;
        "python-poetry")
            poetry run pytest
            ;;
        "python-pip")
            pytest
            ;;
        "rust")
            cargo test
            ;;
        "go")
            go test ./...
            ;;
        "typescript"|"node")
            npm test
            npm run type-check
            ;;
    esac
}
```

### 6. Report Location
```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
Project type: <detected-type>
```

## Worktree Management Features

### Workspace Tracking
- Maintain registry of active worktrees
- Monitor disk usage and performance
- Track project types and setup history
- Report worktree health status

### Automatic Cleanup Integration
- Integration with finishing-a-development-branch
- Automatic removal of worktrees for deleted branches
- Clean up stale directories
- Verify git consistency

### Team Coordination
- Worktree sharing capabilities
- Handoff procedures between developers
- Conflict resolution for shared worktrees
- Collaboration analytics and reporting

## Integration with Other Droids

- **brainstorming:** Automatic worktree creation for implementation (REQUIRED)
- **finishing-a-development-branch:** Seamless cleanup and integration (REQUIRED)
- **subagent-driven-development:** Worktree isolation for task execution
- **executing-plans:** Worktree-based plan implementation

## Red Flags

**Never:**
- Create worktree without .gitignore verification (project-local)
- Skip baseline test verification
- Proceed with failing tests without asking
- Assume directory location when ambiguous
- Skip AGENTS.md check

**Always:**
- Follow directory priority: existing > AGENTS.md > ask
- Verify .gitignore for project-local
- Auto-detect and run project setup
- Verify clean test baseline

## Quick Reference

| Situation | Action |
|-----------|--------|
| `.worktrees/` exists | Use it (verify .gitignore) |
| `worktrees/` exists | Use it (verify .gitignore) |
| Both exist | Use `.worktrees/` |
| Neither exists | Check AGENTS.md → Ask user |
| Directory not in .gitignore | Add it immediately + commit |
| Tests fail during baseline | Report failures + ask |

## Enhanced Error Handling

### Disk Space Issues
```bash
verify-disk-space() {
    local path=$1
    local required_space=1073741824  # 1GB minimum
    
    local available=$(df -B "$path" | awk 'NR==2 {print $4}')
    
    if [ "$available" -lt "$required_space" ]; then
        echo "Error: Insufficient disk space ($((available / 1024 / 1024))MB available, at least $((required_space / 1024 / 1024))MB required)"
        return 1
    fi
}
```

### Permission Issues
```bash
verify-permissions() {
    local path=$1
    
    if [ ! -w "$(dirname "$path")" ]; then
        echo "Error: No write permissions in $(dirname "$path")"
        return 1
    fi
}
```

### Git Repository Health
```bash
verify-git-health() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo "Error: Not in a git repository"
        return 1
    fi
    
    if [ -n "$(git status --porcelain)" ]; then
        echo "Warning: Working directory not clean - consider committing changes first"
    fi
}
```

### Cleanup on Failure
```bash
cleanup-on-failure() {
    local path=$1
    
    if [ -d "$path" ]; then
        echo "Cleaning up failed worktree creation at $path"
        rm -rf "$path" 2>/dev/null || true
    fi
    
    # Remove worktree reference if it was created
    git worktree prune
}