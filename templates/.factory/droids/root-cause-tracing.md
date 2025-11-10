---
name: root-cause-tracing
description: Traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite, mcp__desktop-commander__start_process, mcp__desktop-commander__interact_with_process]
---

# Root Cause Tracing

## Overview
Use when errors occur deep in execution and you need to trace back to find the original trigger - systematically traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior.

## Usage

Run this droid when:
- An error occurs deep in the execution stack
- You need to find the original source of a problem
- Bugs are symptoms rather than root causes
- Multiple layers of code are involved
- Systematic-debugging indicates need for deeper analysis

## Process

### Phase 1: Error Analysis

**BEFORE starting trace:**

1. **Identify the failure point**
   - Where exactly did the error manifest?
   - What was the immediate symptom?
   - Capture full error message and stack trace
   - Document the observable effects

2. **Map the call stack**
   - Trace the complete execution path
   - Identify all functions/methods involved
   - Note parameters and return values
   - Map data flow through the system

3. **Document symptoms**
   - What went wrong (observable behavior)?
   - What should have happened?
   - Error messages, warnings, logs
   - System state at failure point

### Phase 2: Backward Tracing

**Work systematically backward from failure:**

1. **Trace data flow**
   - Follow invalid data backward through each function
   - Check parameter values at each call site
   - Verify transformation at each step
   - Look for first occurrence of bad data

2. **Check call chain**
   - Examine each function in the call stack
   - Verify preconditions and invariants
   - Check for assumption violations
   - Look for side effects

3. **Add instrumentation**
   - Insert logging/checkpoints as needed
   - Add debug prints or breakpoints
   - Create temporary validation checks
   - Monitor data at critical points

### Phase 3: Source Identification

**Pinpoint the exact origin:**

1. **Locate origin**
   - Find where the problem first appeared
   - Identify the exact line/operation
   - Determine what triggered the issue
   - Establish timeline of events

2. **Verify hypothesis**
   - Confirm this is the root cause
   - Test the hypothesis experimentally
   - Reproduce with isolated test
   - Verify fix resolves issue

3. **Document findings**
   - Clear explanation of the source
   - Steps to reproduce
   - Recommended fix approach
   - Prevention measures

## Tracing Strategies

### Data-Flow Tracing
- Follow invalid values backward
- Check transformations at each step
- Look for type mismatches
- Identify boundary violations

### Call-Stack Analysis
- Examine each caller in the stack
- Check parameter passing
- Verify function contracts
- Look for missing validation

### State-Based Tracing
- Track system state changes
- Identify when state becomes invalid
- Check race conditions
- Look for corruption sources

## Common Patterns

### "It Works Locally, Fails in Production"
- Environment differences
- Configuration mismatches
- Network/Timing dependencies
- Resource constraints

### "Intermittent Failures"
- Race conditions
- Memory corruption
- External dependencies
- Threading issues

### "Deep Stack Errors"
- Cascading failures
- Error masking
- Exception handling problems
- Resource exhaustion

## Instrumentation Techniques

### Logging
```python
# Add detailed logging at critical points
import logging

def process_data(data):
    logging.info(f"process_data input: {data}")
    result = transform(data)
    logging.info(f"transform output: {result}")
    return result
```

### Assertions
```python
# Add temporary assertions to catch violations
def calculate_value(x, y):
    assert x >= 0, f"Invalid x: {x}"
    assert y != 0, f"Division by zero: {y}"
    return x / y
```

### Debug Breakpoints
```python
# Add conditional breakpoints
if data is None:
    import pdb; pdb.set_trace()
```

## Integration

**Required by:** systematic-debugging (Phase 1, Step 5)
**Integrates with:** test-driven-development, verification-before-completion

## When to Stop Tracing

### Found Root Cause When:
- You can reproduce the issue with a minimal example
- Fixing the identified issue resolves the symptom
- The cause explains all observed behaviors
- You understand why the issue occurred

### Continue Tracing When:
- Fix doesn't resolve the symptom
- Multiple potential causes exist
- Issue is actually a symptom of deeper problem
- Architecture questions arise

## Prevention Measures

1. **Input Validation**
   - Validate at system boundaries
   - Check invariants
   - Handle edge cases
   - Fail fast with clear errors

2. **Logging Strategy**
   - Log at entry/exit points
   - Include relevant context
   - Use structured logging
   - Log errors with full context

3. **Testing Strategy**
   - Unit tests at component boundaries
   - Integration tests for data flow
   - Error condition testing
   - Performance testing under stress

## Examples

### Data Corruption Case
- **Symptom:** Database contains invalid values
- **Trace:** Back through API → service → repository → database
- **Root Cause:** Missing validation in API layer
- **Solution:** Add input validation at system boundary

### Performance Degradation
- **Symptom:** Slow response times
- **Trace:** Through middleware → service calls → database queries
- **Root Cause:** N+1 query problem in data access layer
- **Solution:** Optimize query patterns

### Memory Leak
- **Symptom:** Out of memory errors
- **Trace:** Through object creation → reference tracking
- **Root Cause:** Event listeners not being cleaned up
- **Solution:** Add proper cleanup in disposal methods