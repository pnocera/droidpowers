# Using Git Worktrees Migration Specification

## Analysis Summary
**Original Superpowers Skill:** using-git-worktrees
**Core Philosophy:** Systematic directory selection + safety verification = reliable isolation
**Key Features:** Priority-based directory selection, .gitignore verification, project setup automation

## Migration Strategy

### 1. Enhanced Worktree Management through Factory AI

**Factory AI Integration Opportunities:**
- **Smart Directory Detection:** Automatic discovery of existing worktree locations
- **Project Type Recognition:** Enhanced project setup beyond package managers
- **Safety Verification:** Automated .gitignore checking and fixing
- **Worktree Cleanup:** Integration with finishing-a-development-branch

**Advanced Workspace Management:**
```yaml
Directory Priority (Enhanced):
  1. Project-local: .worktrees/ (hidden, preferred)
  2. Project-local: worktrees/ (visible, alternative)
  3. Global: ~/.config/droidpowers/worktrees/<project>/
  4. Global: ~/worktrees/<project>/ (fallback)

Safety Verification (Enhanced):
  - .gitignore validation with automatic fixing
  - Permission checking for directory creation
  - Disk space verification before worktree creation
  - Git repository health verification
```

### 2. Implementation Specifications

#### Core Droid Structure
```markdown
---
name: using-git-worktrees
description: Creates isolated git worktrees with smart directory selection and safety verification
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__list_directory, mcp__desktop-commander__create_directory, mcp__desktop-commander__start_process]
---

# Using Git Worktrees Droid

## Core Principle
Systematic directory selection + safety verification = reliable isolation

## Enhanced Directory Selection
1. Check existing directories in priority order
2. Verify safety requirements (.gitignore, permissions)
3. Create appropriate directory structure
4. Set up isolated workspace with project detection
```

#### Slash Command (.factory/commands/worktree)
```markdown
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
```

### 3. Advanced Factory AI Features

#### Enhanced Project Detection
```yaml
Project Types and Setup Commands:
  React/Vue/Angular:
    - Files: package.json, vite.config.ts, webpack.config.js
    - Setup: npm install, npm run dev-setup
    - Tests: npm test, npm run type-check
    
  Python (Poetry):
    - Files: pyproject.toml, poetry.lock
    - Setup: poetry install, poetry run pre-commit install
    - Tests: poetry run pytest, poetry run mypy
    
  Python (Pip):
    - Files: requirements.txt, setup.py
    - Setup: pip install -r requirements.txt, pip install -e .
    - Tests: pytest, python -m mypy
    
  Rust:
    - Files: Cargo.toml, Cargo.lock
    - Setup: cargo build, cargo fetch
    - Tests: cargo test, cargo clippy
    
  Go:
    - Files: go.mod, go.sum
    - Setup: go mod download, go mod tidy
    - Tests: go test ./..., go vet ./...
    
  TypeScript/Node:
    - Files: tsconfig.json, package.json
    - Setup: npm install, npm run build
    - Tests: npm test, npm run type-check
```

#### Smart Workspace Configuration
```bash
# Enhanced worktree creation with configuration
create-worktree() {
    local branch=$1
    local location=$(select-worktree-location)
    local project=$(get-project-name)
    local path="$location/$branch"
    
    # Pre-creation safety checks
    verify-disk-space "$path"
    verify-permissions "$path"
    verify-git-health
    fix-gitignore-if-needed "$location"
    
    # Create worktree with enhanced error handling
    git worktree add "$path" -b "$branch" || {
        cleanup-on-failure "$path"
        return 1
    }
    
    # Enhanced project setup
    setup-project-environment "$path" "$project"
    verify-clean-baseline "$path"
    report-worktree-ready "$path" "$branch"
}
```

#### Worktree Management Features
- **Workspace Tracking:** Maintain registry of active worktrees
- **Automatic Cleanup:** Integration with branch deletion
- **Resource Monitoring:** Track disk usage and performance
- **Team Coordination:** Worktree sharing and handoff capabilities

### 4. Quality Validation Requirements

#### Safety Verification Validation
- [ ] .gitignore verification and automatic fixing
- [ ] Permission checking for directory creation
- [ ] Disk space verification before worktree creation
- [ ] Git repository health validation

#### Project Setup Validation
- [ ] Automatic project type detection working
- [ ] Enhanced setup commands beyond package managers
- [ ] Clean baseline verification with multiple test frameworks
- [ ] Error handling and rollback capabilities

#### Integration Testing Scenarios
- [ ] Multiple worktree types (project-local, global)
- [ ] Different project types and setups
- [ ] Edge cases (disk full, permission denied, corrupt git)
- [ ] Team coordination and worktree sharing

### 5. Migration Challenges and Solutions

#### Challenge 1: Enhanced Project Detection
**Original:** Basic package.json detection
**Factory AI Enhancement:** Comprehensive project type recognition with custom setups

#### Challenge 2: Advanced Safety Verification
**Original:** Basic .gitignore checking
**Factory AI Enhancement:** Multi-layer safety verification with automatic fixing

#### Challenge 3: Worktree Lifecycle Management
**Original:** Simple creation without cleanup
**Factory AI Enhancement:** Complete worktree lifecycle with tracking and cleanup

### 6. Enhanced Features

#### Worktree Analytics
- **Usage Statistics:** Track most used worktrees and branches
- **Performance Metrics:** Monitor setup times and test execution
- **Resource Usage:** Track disk space and memory consumption
- **Team Insights:** Worktree sharing and collaboration patterns

#### Advanced Worktree Operations
```bash
# Worktree status and health
worktree-status() {
    echo "Active worktrees:"
    git worktree list
    echo ""
    echo "Disk usage:"
    du -sh .worktrees/* 2>/dev/null || echo "No local worktrees"
    echo ""
    echo "Branch status:"
    git branch -vv
}

# Worktree cleanup and maintenance
cleanup-worktrees() {
    # Remove worktrees for deleted branches
    # Clean up stale directories
    # Verify git consistency
    # Report cleanup actions
}
```

#### Integration with Other Droids
- **brainstorming:** Automatic worktree creation for implementation
- **finishing-a-development-branch:** Seamless cleanup and integration
- **subagent-driven-development:** Worktree isolation for task execution
- **executing-plans:** Worktree-based plan implementation

## Implementation Timeline (3 Weeks)

### Week 1: Core Framework and Safety
- **Days 1-3:** Deep analysis of original skill and safety mechanisms
- **Days 4-5:** Design enhanced directory selection and safety verification
- **Days 6-7:** Create enhanced project detection and setup framework

### Week 2: Implementation and Integration
- **Days 8-10:** Implement core droid with enhanced safety features
- **Days 11-12:** Create slash command with advanced workspace management
- **Days 13-14:** Integrate with desktop commander and directory management

### Week 3: Advanced Features and Testing
- **Days 15-17:** Implement worktree lifecycle management and analytics
- **Days 18-19:** Comprehensive testing with various project types
- **Days 20-21:** Performance optimization and documentation

## Success Criteria

### Functional Requirements
- 100% of original worktree creation workflow preserved
- Enhanced safety verification working correctly
- Automatic project type detection accurate
- Advanced workspace management functional

### Quality Requirements
- Worktree creation < 30 seconds including setup
- Project type detection > 95% accuracy
- Zero data loss during worktree operations
- Complete rollback capability on failures

### Integration Requirements
- Seamless integration with brainstorming skill
- Automatic cleanup with finishing-a-development-branch
- Worktree tracking and management working
- Support for major project types and custom setups