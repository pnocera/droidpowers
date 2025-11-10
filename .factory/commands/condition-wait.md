# Condition-Based Waiting Command

## Usage
```bash
/droid condition-based-waiting
```

## Description
Analyzes and replaces flaky test timeouts with condition-based waiting patterns.

## Process
1. Scan test files for arbitrary timeouts (`setTimeout`, `sleep`, etc.)
2. Identify race conditions and timing dependencies
3. Replace with `waitFor` condition polling
4. Add proper timeout handling with meaningful errors
5. Verify parallel test execution stability

## Examples
```bash
/droid condition-based-waiting
# Analyzes current test suite and applies condition-based patterns
```

## Arguments
$ARGUMENTS
