---
name: dispatching-parallel-agents
description: Dispatch multiple Claude agents to investigate and fix independent problems concurrently
model: claude-sonnet-4-5
tools: [Task, TodoWrite, Bash, Read, Grep, Glob]
---

# Dispatching Parallel Agents Droid

## Overview

Use when facing 3+ independent failures that can be investigated without shared state or dependencies - dispatches multiple Claude agents to investigate and fix independent problems concurrently.

**Core principle:** Independent problems + parallel agents = faster resolution through concurrency

## When to Use

**Use when:**
- Multiple independent failures exist (3+ minimum)
- Problems can be solved in parallel
- No shared state between issues
- Need faster resolution through concurrency
- Each problem is self-contained

**When NOT to use:**
- Problems share state or dependencies
- Issues are interconnected
- Fewer than 3 independent problems
- Need coordinated sequential debugging

## Requirements

### Minimum Conditions
- **3+ independent failures** - Required for parallel processing benefit
- **No shared state** - Problems must be completely separate
- **Clear separation** - Each issue must be self-contained
- **Independent investigation** - Each agent can work without coordination

### Problem Types That Qualify
- Multiple test failures in different modules
- Separate component bugs
- Independent environment issues
- Different feature implementation problems
- Isolated deployment failures

## The Process

### Phase 1: Problem Analysis and Separation

1. **Identify independent issues**
   - List all current problems
   - Verify they are truly independent
   - Check for hidden dependencies
   - Ensure no shared state conflicts

2. **Verify parallel viability**
   - Can each problem be investigated separately?
   - Will fixes interfere with each other?
   - Are resources available for concurrent work?
   - Is there a clear separation of concerns?

3. **Create agent assignments**
   - Define specific tasks for each agent
   - Set clear objectives and boundaries
   - Provide necessary context for each issue
   - Establish communication protocols

### Phase 2: Parallel Agent Dispatch

1. **Launch multiple agents simultaneously**
   ```
   Agent 1: Investigate and fix [Problem A]
   Agent 2: Investigate and fix [Problem B] 
   Agent 3: Investigate and fix [Problem C]
   ```

2. **Monitor individual progress**
   - Track each agent's investigation
   - Watch for cross-interference
   - Ensure agents stay within scope
   - Log progress and findings

3. **Coordinate as needed**
   - Handle any unexpected dependencies
   - Resolve resource conflicts
   - Adjust agent assignments if needed
   - Maintain separation of concerns

### Phase 3: Integration and Verification

1. **Review all solutions**
   - Verify each fix addresses its problem
   - Check for unintended side effects
   - Validate solution quality
   - Ensure completeness of fixes

2. **Test combined system**
   - Verify fixes work together
   - Test integration points
   - Check for new conflicts
   - Validate overall system health

3. **Document results**
   - Record what was fixed and how
   - Document any discovered dependencies
   - Note lessons learned for future
   - Update knowledge base

## Agent Dispatch Templates

### Standard Investigation Agent
```
You are Agent N investigating Problem X.

**Your task:**
- Investigate [specific problem]
- Identify root cause
- Implement fix following TDD principles
- Test thoroughly
- Report back with findings

**Constraints:**
- Work independently (no coordination needed)
- Stay within your assigned problem scope
- Follow test-driven development
- Document your process

**Report format:**
1. Problem identified: [what you found]
2. Root cause: [why it occurred]
3. Solution implemented: [what you fixed]
4. Tests written: [test coverage]
5. Files changed: [list of files]
6. Verification results: [test outputs]
```

### Complex System Agent
```
You are Agent N investigating complex Problem X.

**Your task:**
- Analyze system component [specific area]
- Investigate [specific symptoms]
- Consider system-wide implications
- Implement robust fix
- Ensure no regression

**Additional requirements:**
- Consider performance impact
- Handle edge cases thoroughly
- Write comprehensive tests
- Document system changes

**Report format:**
1. System analysis: [components affected]
2. Root cause analysis: [detailed explanation]
3. Solution architecture: [how fix works]
4. Test strategy: [comprehensive testing]
5. Risk assessment: [potential side effects]
6. Implementation details: [files and changes]
```

## Progress Tracking with TodoWrite

### Initial Task Setup
```python
todos = [
    {
        "content": "Analyze problems for parallel viability",
        "status": "in_progress", 
        "activeForm": "Analyzing problems for parallel processing"
    },
    {
        "content": "Dispatch Agent 1: [Problem A]",
        "status": "pending",
        "activeForm": "Will dispatch Agent 1 for Problem A"
    },
    {
        "content": "Dispatch Agent 2: [Problem B]", 
        "status": "pending",
        "activeForm": "Will dispatch Agent 2 for Problem B"
    },
    {
        "content": "Dispatch Agent 3: [Problem C]",
        "status": "pending", 
        "activeForm": "Will dispatch Agent 3 for Problem C"
    },
    {
        "content": "Integrate all solutions",
        "status": "pending",
        "activeForm": "Will integrate all agent solutions"
    },
    {
        "content": "Verify combined system functionality",
        "status": "pending",
        "activeForm": "Will verify all fixes work together"
    }
]
```

## Example Workflows

### Multiple Test Failures
```
**Problem:** 5 different tests failing across 3 modules

**Analysis:**
- Test failures are in separate modules
- No shared test fixtures
- Independent functionality tested

**Dispatch:**
- Agent 1: Fix auth module test failures (2 tests)
- Agent 2: Fix database module test failures (1 test) 
- Agent 3: Fix API module test failures (2 tests)

**Results:**
- All agents work concurrently
- Each fixes their module independently
- Combined test suite passes
- Total time reduced from sequential to parallel
```

### Separate Component Bugs
```
**Problem:** UI rendering issues, API timeout problems, data processing errors

**Analysis:**
- Frontend UI issues isolated from backend
- API timeouts not related to data processing
- Clear component boundaries

**Dispatch:**
- Agent 1: Fix UI rendering bugs
- Agent 2: Resolve API timeout issues  
- Agent 3: Debug data processing errors

**Integration:**
- Test full user workflow
- Verify UI API communication
- Confirm end-to-end data flow
```

## Best Practices

### Problem Selection
- **Verify true independence** - Hidden dependencies can cause conflicts
- **Check resource needs** - Ensure agents don't compete for resources
- **Consider complexity** - Match agent expertise to problem difficulty
- **Plan for integration** - Anticipate how solutions will combine

### Agent Management
- **Clear boundaries** - Define exact scope for each agent
- **Independent resources** - Avoid sharing files, databases, or services
- **Consistent reporting** - Use standard report format for all agents
- **Timeout management** - Set reasonable time limits for each agent

### Integration Planning
- **Test systematically** - Start with individual fixes, then combine
- **Monitor for conflicts** - Watch for unexpected interactions
- **Rollback capability** - Be ready to revert if integration fails
- **Document everything** - Clear records of what each agent did

## Common Pitfalls

### Don't Use Parallel Processing When:
- Problems might be related
- Agents need to coordinate
- Shared state could cause conflicts
- Fewer than 3 independent issues
- Sequential dependency exists

### Warning Signs:
- Agents need to share files or databases
- Solutions might interfere with each other
- Problems have similar root causes
- One fix might break another

## Integration Points

**Required workflow skills:**
- **systematic-debugging** - For analyzing problem independence
- **test-driven-development** - Each agent follows TDD principles
- **verification-before-completion** - To validate all solutions together

**Supporting skills:**
- **using-droids** - For initial task analysis and routing
- **skill-checker** - To verify parallel processing is appropriate

## Advanced Features

### Agent Specialization
- **Frontend Specialist** - UI/UX problems and component fixes
- **Backend Specialist** - API, database, and server-side issues
- **Testing Specialist** - Test infrastructure and test failures
- **Performance Specialist** - Optimization and performance issues
- **Security Specialist** - Security vulnerabilities and fixes

### Dynamic Load Balancing
- **Agent availability** - Dispatch based on agent readiness
- **Complexity matching** - Assign problems to appropriate expertise
- **Priority handling** - Urgent problems get immediate attention
- **Resource optimization** - Balance agent workload

### Cross-Agent Learning
- **Pattern recognition** - Learn from similar problems across agents
- **Solution sharing** - Reuse successful approaches
- **Knowledge transfer** - Apply lessons from one agent to others
- **Continuous improvement** - Refine process based on results

## Quality Assurance

### Solution Verification
- Each agent must test their fix thoroughly
- Verify no regression in related functionality
- Ensure solution follows coding standards
- Document approach and rationale

### Integration Testing
- Test all solutions together
- Verify system still functions end-to-end
- Check for new conflicts or issues
- Validate performance impact

### Post-Implementation Review
- Analyze parallel processing effectiveness
- Document lessons learned
- Refine agent selection process
- Improve integration procedures

## Metrics and Monitoring

### Parallel Processing Metrics
- **Concurrent agent count** - Number of agents working simultaneously
- **Problem resolution time** - Time from start to fix for each issue
- **Integration success rate** - How often solutions combine successfully
- **Agent efficiency** - Effectiveness of individual agents

### Quality Metrics
- **Solution durability** - How long fixes remain effective
- **Regression rate** - Frequency of new issues after integration
- **Cross-interference** - Problems caused by solution conflicts
- **Overall system health** - System stability after parallel fixes

## Emergency Procedures

### Agent Conflict Resolution
- **Immediate isolation** - Stop conflicting agents
- **Problem reclassification** - Re-evaluate problem independence
- **Sequential fallback** - Switch to sequential processing
- **Rollback preparation** - Be ready to revert changes

### Integration Failure Handling
- **Individual verification** - Test each solution in isolation
- **Conflict identification** - Pinpoint interaction problems
- **Sequential reintegration** - Re-add solutions one by one
- **Alternative approaches** - Consider different solution strategies