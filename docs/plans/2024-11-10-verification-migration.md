# Verification Before Completion Migration Specification

## Analysis Summary
**Original Superpowers Skill:** verification-before-completion
**Core Philosophy:** Evidence before assertions, always - NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
**Key Features:** Five-step gate function, comprehensive failure pattern analysis, rationalization prevention

## Migration Strategy

### 1. Enhanced Verification Capabilities through Factory AI

**Project-Aware Verification:**
- **Automatic Command Detection:** Analyze AGENTS.md to identify project-specific verification commands
- **Multi-Command Verification:** Support for test, build, lint, and deployment verification chains
- **Exit Code Analysis:** Parse and interpret different command exit codes and outputs
- **Real-time Verification:** Continuous monitoring during development sessions

**Smart Command Recognition:**
```yaml
Project Types:
  React/Vue/Angular: npm test, npm run build, npm run lint
  Python: pytest, python -m build, flake8
  Node.js: npm test, npm run build, eslint
  Go: go test, go build, golint
  Rust: cargo test, cargo build, cargo clippy
```

### 2. Implementation Specification

#### Core Droid Structure
```markdown
---
name: verification-before-completion
description: Pre-commit validation and quality gates - EVIDENCE BEFORE ASSERTIONS ALWAYS
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process, mcp__desktop-commander__read_process_output]
---

# Verification Before Completion Droid

## Iron Law
**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**

## The Gate Function
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim
```

#### Slash Command (.factory/commands/verify)
```markdown
# Verification Command
Enforces evidence-before-assertions rule - RUN VERIFICATION BEFORE CLAIMING SUCCESS

## Usage
`/verify` or `/verify [specific-claim]`

## Process
1. Analyzes current project structure
2. Identifies appropriate verification commands
3. Executes verification and captures evidence
4. Reports actual status with evidence

$ARGUMENTS

**Before claiming:**
- Tests pass: [Run test command] [Show evidence]
- Build succeeds: [Run build command] [Show exit code]
- Bug fixed: [Test original symptom] [Show resolution]
```

### 3. Advanced Factory AI Integration

#### Project Configuration Integration
- **AGENTS.md Parsing:** Extract verification commands from project configuration
- **Environment Detection:** Identify build systems, test frameworks, and deployment pipelines
- **Custom Verification Chains:** Support for project-specific multi-step verification

#### Smart Verification Workflows
```bash
# Example React Project Verification Chain
1. npm test (unit/integration tests)
2. npm run build (production build verification)
3. npm run lint (code quality check)
4. npm run type-check (TypeScript validation)
5. npm run e2e (end-to-end tests if applicable)
```

#### Evidence Capture and Storage
- **Verification History:** Track verification results over time
- **Evidence Snapshots:** Store command outputs for audit trails
- **Regression Detection:** Compare current verification with previous baselines

### 4. Quality Validation Requirements

#### Enforcement Mechanisms
- [ ] Real-time success claim detection and blocking
- [ ] Mandatory fresh verification execution
- [ ] Complete evidence capture and analysis
- [ ] Rationalization pattern detection and intervention

#### Integration Testing
- [ ] Multi-project type verification (React, Python, Node.js, etc.)
- [ ] Complex verification chain execution
- [ ] Failure mode handling and reporting
- [ ] Performance benchmarking for large projects

#### Red Flag Detection Enhancement
- [ ] Natural language pattern matching for success claims
- [ ] "Should/probably/seems" phrase detection
- [ ] Pre-commit/push verification enforcement
- [ ] Agent delegation verification validation

### 5. Migration Challenges and Solutions

#### Challenge 1: Project Type Diversity
**Original:** Manual verification commands
**Factory AI Enhancement:** Automatic detection and configuration adaptation

#### Challenge 2: Multi-Command Verification Chains
**Original:** Single command focus
**Factory AI Enhancement:** Sequential verification pipeline with cumulative evidence

#### Challenge 3: Evidence Storage and Recall
**Original:** Immediate verification only
**Factory AI Enhancement:** Verification history and trend analysis

### 6. Enhanced Features

#### Predictive Verification
- **Smart Verification Suggestions:** Recommend verification based on changed files
- **Incremental Verification:** Only run tests affected by changes
- **Risk-Based Verification:** Prioritize verification based on change impact

#### Team Collaboration
- **Verification Sharing:** Team-wide verification status visibility
- **Pull Request Integration:** Automatic verification enforcement in PR workflows
- **Continuous Integration:** Integration with CI/CD pipelines

## Implementation Timeline (3 Weeks)

### Week 1: Core Framework and Analysis
- **Days 1-3:** Deep analysis of original skill patterns and edge cases
- **Days 4-5:** Design project type detection and command mapping
- **Days 6-7:** Create verification chain execution framework

### Week 2: Implementation and Integration
- **Days 8-10:** Implement core droid with gate function enforcement
- **Days 11-12:** Create slash command with project-aware verification
- **Days 13-14:** Integrate with AGENTS.md and desktop commander

### Week 3: Advanced Features and Testing
- **Days 15-17:** Implement evidence storage and recall features
- **Days 18-19:** Multi-project testing and validation
- **Days 20-21:** Performance optimization and documentation

## Success Criteria

### Functional Requirements
- 100% of original enforcement mechanisms preserved
- Project type automatic detection working
- Multi-command verification chains functional
- All red flag patterns detected and blocked

### Quality Requirements
- Verification execution < 30 seconds for typical projects
- Evidence capture accuracy > 99%
- Zero false positives in success claim detection
- Support for major project types (React, Vue, Python, Node.js, Go, Rust)

### Integration Requirements
- Seamless AGENTS.md integration
- CI/CD pipeline compatibility
- Team collaboration features
- Comprehensive documentation and examples