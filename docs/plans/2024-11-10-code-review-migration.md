# Code Review Skills Migration Specification

## Analysis Summary
**Original Superpowers Skills:** requesting-code-review, receiving-code-review
**Core Philosophy:** Technical rigor over social comfort, verification before implementation
**Key Features:** Subagent dispatch, structured feedback handling, YAGNI enforcement, pushback protocols

## Migration Strategy

### 1. Enhanced Code Review through Factory AI

**Factory AI Integration Opportunities:**
- **Automated Git Analysis:** Use desktop commander for SHA extraction and diff analysis
- **Subagent Dispatch:** Leverage Task tool for code-reviewer subagent calls
- **Project Context Awareness:** AGENTS.md integration for review standards
- **Team Collaboration:** Multi-reviewer workflows and feedback tracking

**Smart Review Management:**
```yaml
Review Triggers:
  - Task completion (subagent-driven development)
  - Major feature implementation
  - Before merge to main
  - When development stuck
  - Before refactoring (baseline check)

Review Context:
  - Project type and architecture
  - Team coding standards
  - Recent changes and impact
  - Performance and security considerations
```

### 2. Implementation Specifications

#### Requesting Code Review Droid
```markdown
---
name: requesting-code-review
description: Dispatch code-reviewer subagent to catch issues before they cascade - REVIEW EARLY, REVIEW OFTEN
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process]
---

# Requesting Code Review Droid

## Core Principle
Review early, review often.

## When to Request Review
**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug
```

#### Receiving Code Review Droid
```markdown
---
name: receiving-code-review
description: Technical evaluation of feedback before implementation - VERIFY BEFORE IMPLEMENTING, not performative agreement
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process]
---

# Receiving Code Review Droid

## Core Principle
Technical correctness over social comfort. Verify before implementing.

## Response Pattern
1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: Technical acknowledgment or reasoned pushback
6. IMPLEMENT: One item at a time, test each
```

#### Slash Commands
```markdown
# Request Code Review Command
Dispatch code-reviewer subagent for technical validation

## Usage
`/review` or `/review [description]`

## Process
1. Extract git SHAs automatically
2. Analyze current changes and context
3. Dispatch code-reviewer subagent
4. Present findings for action

# Receive Review Command
Handle feedback with technical rigor

## Usage
`/handle-review [feedback-summary]`

## Process
1. Parse feedback items
2. Verify against codebase reality
3. Evaluate technical validity
4. Provide implementation plan
```

### 3. Advanced Factory AI Features

#### Automated Git Context Analysis
```bash
# Enhanced SHA Extraction
BASE_SHA=$(git merge-base HEAD origin/main)  # Intelligent base detection
HEAD_SHA=$(git rev-parse HEAD)

# Change Impact Analysis
git diff --stat $BASE_SHA..HEAD  # File changes and complexity
git log --oneline $BASE_SHA..HEAD  # Commit messages and context
```

#### Smart Reviewer Selection
- **Project Type Matching:** Reviewers familiar with current technology stack
- **Code Area Expertise:** Reviewers with domain-specific knowledge
- **Availability Considerations:** Active reviewers vs time zone constraints
- **Load Balancing:** Distribute reviews across team members

#### Review Quality Enhancement
```yaml
Review Categories:
  - Critical: Security, performance, breaking changes
  - Important: Logic errors, missing requirements
  - Minor: Style, documentation, naming
  
Automated Checks:
  - Lint and format validation
  - Test coverage analysis
  - Security vulnerability scanning
  - Performance regression detection
```

### 4. Quality Validation Requirements

#### Code Review Droid Validation
- [ ] Proper SHA extraction and git integration
- [ ] Subagent dispatch with correct parameters
- [ ] Review trigger detection and enforcement
- [ ] Feedback categorization and prioritization

#### Feedback Handling Validation
- [ ] Technical verification before implementation
- [ ] YAGNI enforcement for unused features
- [ ] Pushback protocols and technical reasoning
- [ ] Implementation order and testing validation

#### Integration Testing Scenarios
- [ ] Multiple reviewer feedback consolidation
- [ ] Conflicting feedback resolution
- [ ] External reviewer skepticism protocols
- [ ] Team coordination and communication

### 5. Migration Challenges and Solutions

#### Challenge 1: Multi-Reviewer Coordination
**Original:** Single subagent approach
**Factory AI Enhancement:** Multiple reviewer workflows with feedback consolidation

#### Challenge 2: Technical Verification Automation
**Original:** Manual codebase checking
**Factory AI Enhancement:** Automated codebase analysis and impact assessment

#### Challenge 3: Review Quality Consistency
**Original:** Manual review standards
**Factory AI Enhancement:** Project-aware review standards from AGENTS.md

### 6. Enhanced Features

#### Review Analytics
- **Review Metrics:** Time to review, feedback quality, fix rates
- **Reviewer Performance:** Consistency, thoroughness, technical accuracy
- **Code Quality Trends:** Bug detection rates, regression patterns
- **Team Velocity:** Impact of reviews on development speed

#### Continuous Integration
- **Automated Review Triggers:** PR-based review initiation
- **Review Status Tracking:** Real-time feedback on review progress
- **Quality Gates:** Block merges until review completion
- **Escalation Protocols:** Automatic escalation for blocked reviews

## Implementation Timeline (3 Weeks)

### Week 1: Core Framework Development
- **Days 1-3:** Deep analysis of both code review skills and edge cases
- **Days 4-5:** Design Factory AI integration and reviewer coordination
- **Days 6-7:** Create git automation and subagent dispatch framework

### Week 2: Implementation and Integration
- **Days 8-10:** Implement both code review droids with full enforcement
- **Days 11-12:** Create slash commands with automated git analysis
- **Days 13-14:** Integrate with desktop commander and task management

### Week 3: Advanced Features and Testing
- **Days 15-17:** Implement multi-reviewer coordination and analytics
- **Days 18-19:** Comprehensive testing with various feedback scenarios
- **Days 20-21:** Performance optimization and documentation

## Success Criteria

### Functional Requirements
- 100% of original review protocols preserved
- Automated git SHA extraction and analysis working
- Subagent dispatch with proper parameter filling
- Technical verification before implementation enforcement

### Quality Requirements
- Review initiation < 10 seconds
- Feedback analysis accuracy > 95%
- Multi-reviewer coordination without conflicts
- Zero regression in review quality

### Integration Requirements
- Seamless integration with existing development workflows
- Team coordination features functional
- Review analytics and metrics tracking
- Comprehensive documentation and examples