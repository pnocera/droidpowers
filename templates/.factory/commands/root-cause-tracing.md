# Root Cause Tracing Command
Traces bugs backward through call stack to find original source of invalid data or incorrect behavior

## Usage
`/droid root-cause-tracing` or `/droid root-cause-tracing [error description]`

## Process
1. Analyzes the failure point and symptoms
2. Maps the complete call stack and data flow
3. Traces backward through execution path
4. Adds instrumentation where needed
5. Identifies exact origin of the problem
6. Documents findings and fix recommendations

$ARGUMENTS

**Phase 1:** Error Analysis - identify failure point, map call stack, document symptoms
**Phase 2:** Backward Tracing - follow data flow, check call chain, add instrumentation  
**Phase 3:** Source Identification - locate origin, verify hypothesis, document findings

**Getting Started:**
1. Describe the failure point and symptoms
2. Provide error messages and stack traces
3. Explain what should have happened
4. Share relevant code context

**Tracing Strategies:**
- Data-flow tracing (follow invalid values backward)
- Call-stack analysis (examine each function in stack)
- State-based tracing (track system state changes)

**Common Use Cases:**
- Deep stack errors with multiple layers involved
- Intermittent failures that are hard to reproduce
- Performance degradation or resource issues
- Bugs that appear as symptoms of deeper problems

**Integration with:**
- systematic-debugging (required when Phase 1 indicates deep analysis needed)
- test-driven-development (for creating minimal reproduction tests)
- verification-before-completion (to validate fixes address root cause)

**Remember:** Fix the source, not the symptom!