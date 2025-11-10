# Test Skills Command

## Usage
```bash
/droid testing-skills-with-subagents
```
或
```bash
/test-skills [skill-name-or-description]
```

## Description
Applies rigorous RED-GREEN-REFACTOR cycle to validate and strengthen skills through subagent pressure testing. Ensures skills are bulletproof against rationalization before deployment.

## Process

### Phase 1: RED - Baseline Testing
1. Creates pressure scenarios without the skill
2. Documents agent rationalizations and failures
3. Establishes success criteria for validation

### Phase 2: GREEN - Skill Validation  
1. Tests skill effectiveness with subagents
2. Verifies compliance under pressure scenarios
3. Validates cross-agent compatibility

### Phase 3: REFACTOR - Loophole Closure
1. Identifies new rationalization attempts
2. Strengthens skill documentation
3. Ensures bulletproof resistance to workarounds

## Examples

### Testing a New Skill
```bash
/test-skills "my-new-debugging-skill"
# Runs complete TDD validation cycle for the skill
```

### Testing Existing Skill Robustness
```bash
/droid testing-skills-with-subagents
# Interactive session for comprehensive skill testing
```

## Arguments
$ARGUMENTS

**Skill Testing Workflow:**
1. RED: Test without skill → Document failures
2. GREEN: Test with skill → Verify compliance  
3. REFACTOR: Close loopholes → Ensure bulletproof

**Supported Skill Types:**
- Discipline skills (rules enforcement)
- Technique skills (how-to guides)
- Reference skills (information lookup)

**Quality Assurance:**
- All skills must pass pressure testing
- No rationalization workarounds allowed
- Cross-agent compatibility required
- Edge cases must be handled