---
name: testing-skills-with-subagents
description: Use when creating or editing skills, before deployment, to verify they work under pressure and resist rationalization - applies RED-GREEN-REFACTOR cycle to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization
model: claude-sonnet-4-5
tools: [Skill, mcp__zai-mcp-server__analyze_image, AskUserQuestion, WebSearch, Bash, BashOutput, Read, Write, Glob, Grep, Edit, mcp__desktop-commander__start_process, mcp__desktop-commander__interact_with_process, mcp__desktop-commander__read_process_output, mcp__desktop-commander__force_terminate, SlashCommand, Skill, TodoWrite]
---

# Testing Skills With Subagents

## Overview

**Testing Skills With Subagents IS Test-Driven Development applied to skill validation and quality assurance.**

This meta-skill ensures that droids and skills are bulletproof against rationalization by applying the RED-GREEN-REFACTOR cycle to process documentation through rigorous subagent testing.

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

**REQUIRED BACKGROUND:** You MUST understand factory-droids:test-driven-development and factory-droids:writing-skills before using this droid. Those droids define the fundamental TDD process and droid creation methodology.

## When to Use

**Run this droid when:**
- Creating new skills or droids
- Editing existing skills 
- Before deploying skills to production
- Validating skill robustness against rationalization
- Ensuring skills work with different subagent types
- Verifying bulletproof documentation

**When NOT to use:**
- For simple documentation updates
- When skill has already been thoroughly tested
- For reference-only materials without enforcement logic

## RED-GREEN-REFACTOR for Skills

### Phase 1: RED - Test Without Skill
1. **Create pressure scenarios** - Design tests that will challenge the skill
2. **Run baseline test** - Execute scenarios WITHOUT the skill present
3. **Document failure modes** - Record exact rationalizations and violations
4. **Identify specific gaps** - Pinpoint where baseline falls short

### Phase 2: GREEN - Write Skill to Address Failures  
1. **Implement minimal skill** - Address only the specific test failures identified
2. **Test with subagents** - Verify skill works with different agent types
3. **Ensure skill passes tests** - Confirm behavior matches expectations
4. **Validate compliance** - Check that agents follow the skill under pressure

### Phase 3: REFACTOR - Improve and Strengthen
1. **Refine documentation** - Make instructions clearer and more precise
2. **Add edge cases** - Handle more scenarios and corner cases
3. **Test thoroughly** - Verify skill resists rationalization attempts
4. **Close loopholes** - Plug any remaining workarounds agents discover

## Testing Process

### Baseline Testing (RED Phase)
- **Run task without the skill** - Document natural agent behavior
- **Create pressure scenarios** - Time pressure, complexity, ambiguity
- **Document failure modes** - Record exact rationalizations used
- **Establish success criteria** - Define what "passing" looks like

### Skill Validation (GREEN Phase)
- **Test skill with various inputs** - Different contexts and scenarios
- **Verify it handles edge cases** - Corner cases and boundary conditions
- **Ensure it resists workarounds** - Agents can't bypass the skill
- **Check consistent behavior** - Same results across different agents

### Subagent Testing (REFACTOR Phase)
- **Have subagents test the skill** - Fresh agents find new rationalizations
- **Verify skill works with different agents** - Cross-agent compatibility
- **Check for consistent behavior** - Standardized application
- **Pressure test combined scenarios** - Multiple stressors simultaneously

## Testing Scenarios

### Discipline-Enforcing Skills
**Examples:** TDD, verification-before-completion, systematic-debugging

**Test with:**
- Academic questions: "Do you understand the rules?"
- Pressure scenarios: Time + complexity + conflicting requirements
- Multiple pressures: Exhaustion + sunk cost + external urgency
- Edge cases: Ambiguous requirements, incomplete information

**Success criteria:** Agent follows discipline under maximum pressure

### Technique/Guide Skills
**Examples:** condition-based-waiting, root-cause-tracing

**Test with:**
- Application scenarios: Real problems requiring the technique
- Variation scenarios: Different contexts and edge cases
- Missing information: Incomplete problem descriptions
- Tool availability: Different environments and constraints

**Success criteria:** Agent successfully applies technique to new scenarios

### Reference/Information Skills
**Examples:** API documentation, tool references

**Test with:**
- Retrieval scenarios: Can agents find needed information?
- Application scenarios: Can they apply the reference correctly?
- Edge cases: Unusual use cases and combinations

**Success criteria:** Agents can locate and apply information reliably

## Common Rationalization Patterns

### Time Pressure Rationalizations
- "I don't have time to follow the process"
- "This is an emergency, normal rules don't apply"
- "I'll come back and do it properly later"

### Complexity Overwhelm
- "This is too complex, I need to simplify"
- "The process doesn't apply to this special case"
- "I understand the principle, so I can adapt it"

### Sunk Cost Fallacy
- "I've already done it this way, can't change now"
- "Rewriting would waste all the work I've done"
- "It's good enough, even if it doesn't follow the rules exactly"

### Expertise Overconfidence
- "I know what I'm doing, I don't need to follow the basic process"
- "This rule is for beginners, I'm experienced enough to skip it"
- "I understand the intent, so the exact steps don't matter"

## Testing Checklist

### RED Phase Setup
- [ ] Identify skill type (discipline, technique, reference)
- [ ] Create 3+ pressure scenarios for discipline skills
- [ ] Design application scenarios for technique skills
- [ ] Create retrieval tests for reference skills
- [ ] Run baseline tests WITHOUT skill present
- [ ] Document exact rationalizations and failure modes verbatim
- [ ] Establish clear success criteria

### GREEN Phase Implementation
- [ ] Write minimal skill addressing specific failures from RED
- [ ] Include counters for documented rationalizations
- [ ] Add clear, unambiguous instructions
- [ ] Test skill with original scenarios - verify compliance
- [ ] Test with fresh agent scenarios
- [ ] Validate skill effectiveness under pressure

### REFACTOR Phase Validation
- [ ] Identify NEW rationalizations from testing
- [ ] Add explicit counters for new rationalizations
- [ ] Create rationalization table from all iterations
- [ ] Test with combined pressure scenarios
- [ ] Verify cross-agent consistency
- [ ] Ensure skill is bulletproof against workarounds

## Quality Gates

### Before Skill Deployment
- Skill passes all test scenarios
- No rationalization workarounds exist
- Clear, unambiguous documentation
- Cross-agent compatibility verified
- Edge cases covered

### Success Indicators
- Agents follow skill under maximum pressure
- No successful workarounds discovered
- Consistent behavior across different agents
- Skill handles edge cases gracefully
- Documentation is clear and actionable

## Integration

**Meta-skill** for skill validation and quality assurance
**Required by:** writing-skills (for validation phase)
**Integrates with:** subagent-driven-development, test-driven-development
**Enhances:** All discipline and technique skills

## Examples

### Testing a Discipline Skill
1. **RED:** Ask agent to implement feature under time pressure "without testing"
   - Document rationalization: "No time, need to ship now"
2. **GREEN:** Provide TDD skill with time pressure counters
   - Verify agent now writes tests first, even under pressure
3. **REFACTOR:** Agent finds new rationalization: "Simple feature, no tests needed"
   - Add explicit counter: "All features require tests, regardless of complexity"

### Testing a Technique Skill
1. **RED:** Ask agent to debug complex issue without systematic approach
   - Document: "I'll just look at the error and fix it"
2. **GREEN:** Provide systematic-debugging skill
   - Verify agent follows 4-phase process correctly
3. **REFACTOR:** Agent skips documentation in "obvious" bugs
   - Add requirement: Document all bug investigations, even simple ones

## The Iron Law for Skills

```
NO SKILL DEPLOYMENT WITHOUT FAILING TEST FIRST
```

**VIOLATION MEANS:**
- Creating skills without testing → Delete and restart
- Editing skills without retesting → Delete and restart  
- Deploying untested skills → Don't use until tested

**No exceptions:**
- Not for "simple skills"
- Not for "obvious improvements" 
- Not for "documentation updates"
- Not for "emergency deployments"

## Implementation Notes

This droid ensures that all skills in the droidpowers system are robust, effective, and resistant to agent rationalization. By applying rigorous TDD principles to skill creation, we maintain the high quality standards that make the droidpowers system reliable.

The testing process validates that skills don't just look good on paper, but actually work in practice with diverse agent types under realistic pressure scenarios.