# Condition-Based Waiting Migration Specification

## Analysis Summary
**Original Superpowers Skill:** condition-based-waiting
**Core Philosophy:** Wait for actual condition you care about, not a guess about how long it takes
**Key Features:** Eliminate flaky tests from timing guesses, replace arbitrary timeouts

## Migration Strategy

### 1. Enhanced Condition Management through Factory AI

**Factory AI Integration Opportunities:**
- **Smart Condition Detection:** Automatic identification of timeout patterns in code
- **Intelligent Polling Optimization:** Adaptive polling intervals based on system load
- **Advanced Timeout Analysis:** Comprehensive timeout justification and optimization
- **Test Framework Integration:** Native integration with major testing frameworks

**Advanced Waiting Patterns:**
```yaml
Condition Types:
  State-Based:
    - Description: Wait for object or system state change
    - Patterns: machine.state === 'ready', status === 'completed'
    - Use Cases: Service initialization, processing completion
    
  Event-Based:
    - Description: Wait for specific event or event pattern
    - Patterns: events.find(e => e.type === 'DONE'), count >= N
    - Use Cases: Event processing, message handling
    
  Resource-Based:
    - Description: Wait for file, network, or system resource
    - Patterns: fs.existsSync(path), response.status === 200
    - Use Cases: File operations, API calls, database queries
    
  Complex-Condition:
    - Description: Wait for multiple conditions simultaneously
    - Patterns: obj.ready && obj.value > 10, all(tasks.every(t => t.status === 'done'))
    - Use Cases: Complex workflows, parallel operations
```

### 2. Implementation Specifications

#### Core Droid Structure
```markdown
---
name: condition-based-waiting
description: Replace arbitrary timeouts with condition polling - ELIMINATE FLAKY TESTS FROM TIMING GUESSES
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__read_file, mcp__desktop-commander__start_process]
---

# Condition-Based Waiting Droid

## Core Principle
Wait for actual condition you care about, not a guess about how long it takes

## Enhanced Process
1. Detect timeout and timing patterns in code
2. Suggest condition-based alternatives
3. Provide optimized polling implementations
4. Generate framework-specific waiting helpers
```

#### Slash Command (.factory/commands/wait)
```markdown
# Condition-Based Waiting Command
Replace arbitrary timeouts with intelligent condition polling

## Usage
`/wait [file-path]` or `/wait`

## Process
1. Analyze code for timeout patterns
2. Identify flaky test candidates
3. Generate condition-based waiting solutions
4. Create framework-specific helper functions

$ARGUMENTS

**Features:**
- Automatic timeout pattern detection
- Intelligent polling optimization
- Framework-specific waiting helpers
- Performance impact analysis
```

### 3. Advanced Factory AI Features

#### Smart Pattern Detection
```bash
# Enhanced timeout detection algorithms
detect-timeout-patterns() {
    local file_path=$1
    local patterns=(
        "setTimeout\|setInterval"                     # JavaScript/TypeScript
        "time\.sleep\|asyncio\.sleep"           # Python
        "Thread\.sleep\|Object\.wait"             # Java/Other
        "time\.After\|time\.NewTimer"               # Go
        "sleep\|usleep\|nanosleep"                 # C/C++
        "await.*delay\|Task\.delay"                 # .NET
    )
    
    for pattern in "${patterns[@]}"; do
        grep -n "$pattern" "$file_path" | while read line; do
            analyze-timeout-context "$line" "$file_path"
        done
    done
}
```

#### Intelligent Polling Optimization
```typescript
// Advanced condition-based waiting with adaptive polling
class AdaptiveWaiter {
    private adaptivePolling<T>(
        condition: () => T | undefined | null | false,
        options: WaitOptions
    ): Promise<T> {
        const { description, baseTimeout = 5000, adaptive = true } = options;
        let pollInterval = 10; // Start fast
        let consecutiveFails = 0;
        
        return new Promise((resolve, reject) => {
            const startTime = Date.now();
            
            const check = () => {
                const result = condition();
                
                if (result) {
                    resolve(result);
                    return;
                }
                
                if (Date.now() - startTime > baseTimeout) {
                    reject(new Error(`Timeout waiting for ${description} after ${baseTimeout}ms`));
                    return;
                }
                
                // Adaptive polling optimization
                if (adaptive) {
                    pollInterval = this.optimizePollInterval(pollInterval, consecutiveFails);
                    consecutiveFails++;
                }
                
                setTimeout(check, pollInterval);
            };
            
            check();
        });
    }
    
    private optimizePollInterval(current: number, fails: number): number {
        // Slow down if condition frequently not met
        // Speed up if condition is usually met quickly
        if (fails > 10) return Math.min(current * 1.5, 100); // Max 100ms
        if (fails < 3) return Math.max(current / 2, 1); // Min 1ms
        return current; // Keep current
    }
}
```

#### Framework Integration Patterns
```yaml
Framework-Specific Helpers:
  Jest/JavaScript:
    - waitForElement: DOM element appearance
    - waitForState: React component state changes
    - waitForApiResponse: API response completion
    - waitForEvent: Custom event emission
    
  Pytest/Python:
    - wait_for_condition: Generic condition waiting
    - wait_for_file: File system operations
    - wait_for_database: Database query completion
    - wait_for_async_task: Async function completion
    
  Go Testing:
    - WaitForCondition: Generic condition waiting
    - WaitForChannel: Go channel operations
    - WaitForHTTP: HTTP request completion
    - WaitForGoroutine: Goroutine synchronization
```

### 4. Quality Validation Requirements

#### Pattern Detection Validation
- [ ] Timeout pattern detection working across languages
- [ ] Context analysis for distinguishing valid vs flaky timeouts
- [ ] Intelligent suggestion system for condition alternatives
- [ ] Framework-specific optimization working

#### Polling Optimization Validation
- [ ] Adaptive polling intervals working correctly
- [ ] Performance impact minimal (CPU usage < 1%)
- [ ] Timeout handling with clear error messages
- [ ] Edge case handling (never-met conditions)

#### Integration Testing Scenarios
- [ ] JavaScript/TypeScript async operations
- [ ] Python async/await patterns
- [ ] Go goroutine synchronization
- [ ] Multi-language project integration

### 5. Migration Challenges and Solutions

#### Challenge 1: Multi-Language Support
**Original:** Basic JavaScript/TypeScript patterns
**Factory AI Enhancement:** Comprehensive multi-language timeout detection

#### Challenge 2: Adaptive Polling
**Original:** Fixed 10ms polling intervals
**Factory AI Enhancement:** Intelligent polling optimization based on system load

#### Challenge 3: Framework Integration
**Original:** Generic waiting patterns
**Factory AI Enhancement:** Framework-specific optimized helpers

### 6. Enhanced Features

#### Performance Analysis
- **Timing Analysis:** Measure test execution times and optimization impact
- **Race Condition Detection:** Identify and prevent race conditions
- **Resource Usage Monitoring:** Track CPU and memory impact of polling
- **Test Stability Metrics:** Measure pass rate improvements

#### Advanced Testing Integration
```bash
# Enhanced test analysis and improvement
analyze-and-improve-tests() {
    local test_directory=$1
    
    # Find all flaky test candidates
    find-flaky-tests "$test_directory"
    
    # Analyze timeout patterns in each test
    for test in $(get-flaky-tests); do
        analyze-timeout-usage "$test"
        suggest-condition-alternatives "$test"
    done
    
    # Generate optimized test implementations
    generate-optimized-tests "$test_directory"
}
```

#### Developer Experience Features
- **IDE Integration:** Real-time timeout detection and suggestions
- **Documentation Generation:** Automatic waiting pattern documentation
- **Code Transformation:** Automated conversion from timeouts to conditions
- **Teaching Mode**: Interactive guidance on condition-based waiting principles

## Implementation Timeline (3 Weeks)

### Week 1: Core Framework and Pattern Detection
- **Days 1-3:** Deep analysis of original skill and timeout patterns
- **Days 4-5:** Design multi-language detection and optimization
- **Days 6-7:** Create adaptive polling and optimization framework

### Week 2: Implementation and Integration
- **Days 8-10:** Implement core droid with enhanced pattern detection
- **Days 11-12:** Create slash command with framework integration
- **Days 13-14:** Integrate with testing frameworks and optimization

### Week 3: Advanced Features and Testing
- **Days 15-17:** Implement performance analysis and IDE features
- **Days 18-19:** Comprehensive testing with various languages and frameworks
- **Days 20-21:** Performance optimization and documentation

## Success Criteria

### Functional Requirements
- 100% of original condition-based waiting workflow preserved
- Multi-language timeout pattern detection working
- Adaptive polling optimization functional
- Framework-specific integration for major testing frameworks

### Quality Requirements
- Pattern detection accuracy > 95%
- Adaptive polling performance improvement > 40%
- Zero increase in test execution time
- CPU usage during polling < 1%

### Integration Requirements
- Support for JavaScript/TypeScript, Python, Go, Java
- Native integration with Jest, Pytest, Go testing frameworks
- IDE plugins and real-time suggestions
- Comprehensive documentation and examples