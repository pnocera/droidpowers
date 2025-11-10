# Systematic Debugging Migration Specification

## Analysis Summary
**Original Superpowers Skill:** systematic-debugging
**Core Philosophy:** Four-phase framework ensuring understanding before attempting solutions
**Iron Law:** NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
**Dependencies:** root-cause-tracing (REQUIRED), test-driven-development (REQUIRED)

## Migration Strategy

### 1. Droid Structure Preservation

**Key Elements to Maintain Exactly:**
- **Four-Phase Framework:** Each phase MUST be completed before proceeding
- **Iron Law Enforcement:** Strict "no fixes without root cause" rule
- **Red Flag Detection:** Comprehensive list of rationalizations and thought patterns
- **Integration Dependencies:** REQUIRED sub-skills must be enforced

### 2. Factory AI Integration Points

**Enhanced Capabilities through Factory AI:**
- **Multi-Component Evidence Gathering:** Leverage desktop commander for instrumentation
- **Git Analysis Integration:** Use git commands for change analysis
- **Environment Detection:** Check current project context and configuration
- **Automated Testing:** Integrate with project test frameworks

### 3. Implementation Specification

#### Core Droid (.factory/droids/systematic-debugging.md)
```markdown
---
name: systematic-debugging
description: Four-phase bug investigation framework - NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite, mcp__desktop-commander__start_process, mcp__desktop-commander__interact_with_process]
---

# Systematic Debugging Droid

## Iron Law
**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**
**Violating letter of this process is violating the spirit of debugging**

## Four-Phase Enforcement
[Complete phase-by-phase workflow with validation checkpoints]
```

#### Slash Command (.factory/commands/debug)
```markdown
# Systematic Debugging Command
Enforces four-phase debugging framework - NO FIXES WITHOUT ROOT CAUSE FIRST

## Usage
`/debug [issue description]` or `/debug`

$ARGUMENTS

**Phase 1:** Root cause investigation
**Phase 2:** Pattern analysis  
**Phase 3:** Hypothesis testing
**Phase 4:** Implementation with test-driven development
```

### 4. Quality Validation Requirements

#### Enforcement Mechanisms
- [ ] Phase completion validation before proceeding
- [ ] Red flag detection and automatic process reset
- [ ] Required sub-skill integration (root-cause-tracing, TDD)
- [ ] Multiple fix failure architectural questioning

#### Integration Testing
- [ ] Multi-component system debugging scenarios
- [ ] Git change analysis workflows
- [ ] Environment and configuration investigation
- [ ] Test framework integration for Phase 4

#### Performance Standards
- [ ] Droid initialization: < 2 seconds
- [ ] Phase validation: < 500ms per checkpoint
- [ ] Memory usage: < 50MB for active debugging session

### 5. Migration Challenges and Solutions

#### Challenge 1: Complex Multi-Component Systems
**Original:** Manual instrumentation commands
**Factory AI Enhancement:** Leverage desktop commander for systematic evidence gathering

#### Challenge 2: Git Analysis Integration
**Original:** Manual git diff and log analysis
**Factory AI Enhancement:** Automated git analysis with desktop commander git commands

#### Challenge 3: Test Framework Integration
**Original:** Manual test creation after fix
**Factory AI Enhancement:** TDD droid integration with automatic failing test creation

### 6. Unique Value Additions

#### Enhanced Evidence Gathering
- **Automated Environment Detection:** Project type, build system, test framework
- **Git Context Analysis:** Recent changes, commit history, branch state
- **System Instrumentation:** Use desktop commander for systematic data collection

#### Improved User Guidance
- **Real-time Red Flag Detection:** Monitor user language and process violations
- **Phase Completion Validation:** Ensure each phase is fully complete
- **Architecture Intervention:** Automatic escalation when 3+ fixes fail

## Implementation Timeline (3 Weeks)

### Week 1: Analysis and Framework Setup
- **Days 1-2:** Deep analysis of original skill and edge cases
- **Days 3-4:** Design Factory AI integration points
- **Days 5-7:** Create implementation specification and testing plan

### Week 2: Implementation and Integration  
- **Days 8-10:** Implement core droid with four-phase enforcement
- **Days 11-12:** Create slash command with argument handling
- **Days 13-14:** Integrate with desktop commander and test frameworks

### Week 3: Testing and Refinement
- **Days 15-17:** Comprehensive testing and validation
- **Days 18-19:** Performance optimization and benchmarking
- **Days 20-21:** Documentation updates and final quality validation

## Success Criteria

### Functional Requirements
- 100% of original workflow preserved
- All red flags and rationalizations detected
- Required sub-skill dependencies enforced
- Factory AI enhancements functional

### Quality Requirements
- Load time < 2 seconds
- Zero regression in debugging effectiveness
- Enhanced evidence gathering capabilities
- Improved user guidance and enforcement

### Integration Requirements
- Seamless integration with existing droidpowers skills
- AGENTS.md configuration support
- Project-specific customization
- Comprehensive testing scenarios