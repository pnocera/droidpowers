# Phase 1 Integration Tests

## Test Scenarios

### 1. Systematic Debugging Workflow

**Test Case:** Four-phase enforcement workflow
- **Trigger:** `/debug test failure`
- **Expected Flow:**
  1. Systematic-debugging droid launches
  2. Enforces Phase 1: Root cause investigation
  3. Guides through Pattern analysis, Hypothesis testing, Implementation
  4. Integrates with root-cause-tracing and TDD skills
- **Validation:** No fixes without proper investigation

**Verification Commands:**
```bash
# Test debugging workflow
echo "Test failure: null pointer exception" | /debug
# Expected: Phase 1 investigation prompts, no immediate fix suggestions
```

### 2. Verification Before Completion Workflow

**Test Case:** Evidence-before-assertions enforcement
- **Trigger:** `/verify all tests pass`
- **Expected Flow:**
  1. Verification droid analyzes current project structure
  2. Identifies appropriate verification commands from AGENTS.md
  3. Executes verification and captures evidence
  4. Reports actual status with evidence
- **Validation:** Evidence before claims

**Verification Commands:**
```bash
# Test verification workflow
/verify "tests pass"
# Expected: Runs actual test command, shows evidence or reports actual status
```

### 3. Code Review Workflow

**Test Case:** Subagent dispatch with git integration
- **Trigger:** `/review feature complete`
- **Expected Flow:**
  1. Requesting-code-review droid extracts git SHAs automatically
  2. Analyzes current changes and context
  3. Dispatches code-reviewer subagent
  4. Presents findings for action
- **Validation:** Technical feedback and implementation plan

**Verification Commands:**
```bash
# Test review workflow
/review "implemented authentication system"
# Expected: Git SHA extraction, subagent dispatch, technical feedback
```

### 4. Feedback Handling Workflow

**Test Case:** Technical feedback evaluation
- **Trigger:** `/handle-review [feedback-summary]`
- **Expected Flow:**
  1. Receiving-code-review droid parses feedback items into categories
  2. Verifies against codebase reality
  3. Evaluates technical validity
  4. Provides implementation plan
- **Validation:** Technical soundness verification

**Verification Commands:**
```bash
# Test feedback handling
/handle-review "Critical: fix input validation, Important: add error handling"
# Expected: Technical evaluation, implementation plan, one-item-at-a-time approach
```

### 5. Planning Workflow

**Test Case:** Project analysis and plan generation
- **Trigger:** `/plan user authentication`
- **Expected Flow:**
  1. Writing-plans droid analyzes current project structure
  2. Identifies relevant patterns and conventions
  3. Creates detailed implementation plan
  4. Saves to docs/plans/YYYY-MM-DD-feature.md
- **Validation:** Comprehensive plan with exact paths

**Verification Commands:**
```bash
# Test planning workflow
/plan "add user authentication system"
# Expected: Project analysis, detailed plan, exact file paths, complete code examples
```

## Integration Validation Checklist

### Skill Coordination
- [ ] Systematic debugging integrates with root-cause-tracing
- [ ] Verification works with all droidpowers skills
- [ ] Code review dispatches subagents correctly
- [ ] Feedback handling maintains technical rigor
- [ ] Planning provides exact implementation details

### Git Integration
- [ ] Review commands extract correct git SHAs
- [ ] All commands work within git repositories
- [ ] Changes are tracked and committed properly
- [ ] Branch and commit handling works correctly

### Project Structure Integration
- [ ] Skills adapt to different project types
- [ ] AGENTS.md configuration integration working
- [ ] File path resolution accurate across projects
- [ ] Pattern matching and conventions detected

### Command Line Interface
- [ ] All slash commands accept arguments properly
- [ ] Help and usage information accessible
- [ ] Error handling works for missing arguments
- [ ] Commands integrate with existing shell environments

### Error Handling
- [ ] Graceful handling of missing dependencies
- [ ] Clear error messages for user correction
- [ ] Recovery paths for common failure scenarios
- [ ] Validation of prerequisites before execution

## Expected Results

### Successful Integration
- All 5 core skills work independently
- Skills coordinate seamlessly when used together
- Commands provide consistent user experience
- Error handling prevents system failures
- Performance meets specified benchmarks

### Validation Commands
```bash
# Run comprehensive integration test suite
./tests/run-integration-tests.sh

# Expected output:
# ✓ Systematic debugging workflow test
# ✓ Verification enforcement test  
# ✓ Code review coordination test
# ✓ Feedback handling test
# ✓ Planning workflow test
# ✓ Git integration test
# ✓ Project structure adaptation test
# ✓ Command line interface test
# ✓ Error handling test
# ✓ Performance benchmark test
# 
# Integration Tests: 10/10 passed
# Phase 1 Migration: COMPLETE
```

## Performance Benchmarks

- **Droid initialization:** < 2 seconds
- **Command execution:** < 1 second average
- **Git integration:** < 5 seconds for SHA extraction
- **Memory usage:** < 50MB per active droid
- **Concurrent execution:** Support for multiple active skills