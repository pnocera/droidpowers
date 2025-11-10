# Testing Anti-Patterns Migration Specification

## Analysis Summary
**Original Superpowers Skill:** testing-anti-patterns
**Core Philosophy:** Test what code does, not what mocks do - mocks are tools to isolate, not the thing being tested
**Key Features:** 5 iron laws, gate functions, complete mock behavior prevention

## Migration Strategy

### 1. Enhanced Anti-Pattern Detection through Factory AI

**Factory AI Integration Opportunities:**
- **Smart Code Analysis:** Automatic detection of testing anti-patterns across languages
- **Real-time Gate Functions:** Interactive prevention during development
- **Advanced Mock Validation:** Comprehensive mock structure verification
- **Integration Testing Support:** Validation of integration vs unit test boundaries

**Advanced Anti-Pattern Detection:**
```yaml
Detection Categories:
  Mock Behavior Testing:
    - Pattern: Assertion checks for mock elements (*-mock, *-fake)
    - Detection: AST analysis of test files
    - Prevention: Real-time gate functions
    
  Test-Only Code Pollution:
    - Pattern: Production methods only called in test files
    - Detection: Cross-reference analysis between production and test code
    - Prevention: Test utility relocation guidance
    
  Over-Mocking Without Understanding:
    - Pattern: Complex mocks without dependency analysis
    - Detection: Mock complexity vs test complexity analysis
    - Prevention: Dependency graph visualization
    
  Incomplete Mock Structures:
    - Pattern: Mock responses missing real API fields
    - Detection: Schema comparison between mocks and real APIs
    - Prevention: Automatic mock completion suggestions
```

### 2. Implementation Specifications

#### Core Droid Structure
```markdown
---
name: testing-anti-patterns
description: Prevent testing mock behavior, production pollution, and incomplete mocking - TEST WHAT CODE DOES, NOT WHAT MOCKS DO
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__read_file, mcp__desktop-commander__start_process]
---

# Testing Anti-Patterns Droid

## Core Principle
Test what code does, not what mocks do. Mocks are tools to isolate, not the thing being tested.

## Enhanced Anti-Pattern Prevention
1. Real-time code analysis for anti-pattern detection
2. Interactive gate functions for immediate prevention
3. Comprehensive mock validation and completion
4. Test structure optimization guidance
```

#### Slash Command (.factory/commands/antitest)
```markdown
# Anti-Pattern Testing Command
Prevent testing mock behavior and production code pollution

## Usage
`/antitest [test-files]` or `/antitest`

## Process
1. Analyze code for testing anti-patterns
2. Provide real-time gate functions for prevention
3. Suggest refactoring and test improvements
4. Validate mock completeness and structure

$ARGUMENTS

**Features:**
- Real-time anti-pattern detection
- Interactive gate functions
- Mock structure validation
- Test utility organization
```

### 3. Advanced Factory AI Features

#### Smart Code Analysis Engine
```typescript
// Advanced anti-pattern detection algorithms
class AntiPatternAnalyzer {
    analyzeTestFiles(testFiles: string[]): AntiPatternReport {
        const issues: AntiPatternIssue[] = [];
        
        for (const testFile of testFiles) {
            const ast = this.parseAST(testFile);
            
            // Detect mock behavior testing
            const mockBehaviorTests = this.detectMockBehaviorTesting(ast);
            issues.push(...mockBehaviorTests);
            
            // Detect test-only methods in production
            const testOnlyMethods = this.detectTestOnlyCodeInProduction(ast);
            issues.push(...testOnlyMethods);
            
            // Detect over-mocking without understanding
            const complexMocks = this.detectOverMocking(ast);
            issues.push(...complexMocks);
            
            // Detect incomplete mock structures
            const incompleteMocks = this.detectIncompleteMocks(ast);
            issues.push(...incompleteMocks);
        }
        
        return new AntiPatternReport(issues);
    }
    
    private detectMockBehaviorTesting(ast: AST): AntiPatternIssue[] {
        // Find assertions on mock elements
        const mockAssertions = ast.findNodes({
            type: 'CallExpression',
            callee: { name: /getByTestId.*mock/ }
        });
        
        return mockAssertions.map(assertion => ({
            type: 'mock-behavior-testing',
            severity: 'high',
            location: assertion.location,
            message: `Testing mock behavior with getByTestId('${assertion.callee.name}')`,
            suggestion: 'Test real component behavior or remove mock'
        }));
    }
}
```

#### Interactive Gate Functions
```typescript
// Real-time prevention during development
class GateFunctionManager {
    showGateFunction(issue: AntiPatternIssue): void {
        const actions = this.generateFixActions(issue);
        
        this.showInteractivePrompt({
            title: `🚨 Testing Anti-Pattern Detected: ${issue.type}`,
            message: issue.message,
            severity: issue.severity,
            actions: actions,
            requireConfirmation: issue.severity === 'high'
        });
    }
    
    private generateFixActions(issue: AntiPatternIssue): FixAction[] {
        switch (issue.type) {
            case 'mock-behavior-testing':
                return [
                    { label: 'Test Real Component', action: 'unmock-component' },
                    { label: 'Fix Mock Strategy', action: 'adjust-mock' },
                    { label: 'Ignore Risk', action: 'continue-with-warning' }
                ];
                
            case 'test-only-code-pollution':
                return [
                    { label: 'Move to Test Utils', action: 'relocate-method' },
                    { label: 'Refactor Class Design', action: 'redesign-class' },
                    { label: 'Add Production Usage', action: 'add-real-usage' }
                ];
                
            case 'over-mocking-without-understanding':
                return [
                    { label: 'Analyze Dependencies', action: 'analyze-deps' },
                    { label: 'Simplify Mock', action: 'reduce-mock' },
                    { label: 'Use Real Implementation', action: 'use-real' }
                ];
                
            case 'incomplete-mock-structures':
                return [
                    { label: 'Complete Mock Structure', action: 'complete-mock' },
                    { label: 'Mirror Real API', action: 'mirror-api' },
                    { label: 'Use Integration Tests', action: 'switch-to-integration' }
                ];
        }
    }
}
```

#### Comprehensive Mock Validation
```typescript
// Advanced mock structure verification
class MockValidator {
    validateMockCompleteness(mockResponse: any, realApiSchema: APISchema): ValidationResult {
        const validationResults = {
            missingFields: [],
            extraFields: [],
            typeMismatches: [],
            structuralDifferences: []
        };
        
        // Recursive validation of nested objects
        this.validateObjectStructure(mockResponse, realApiSchema, validationResults);
        
        // Generate detailed feedback
        if (validationResults.missingFields.length > 0) {
            return {
                valid: false,
                issues: [
                    `Missing fields in mock: ${validationResults.missingFields.join(', ')}`
                ],
                suggestions: this.generateCompletionSuggestions(validationResults)
            };
        }
        
        return { valid: true, issues: [] };
    }
    
    private generateCompletionSuggestions(results: ValidationResults): string[] {
        return [
            `Add missing fields: ${results.missingFields.join(', ')}`,
            `Review real API documentation`,
            `Use API schema generation tools`,
            `Consider integration tests instead of complex mocks`
        ];
    }
}
```

### 4. Quality Validation Requirements

#### Anti-Pattern Detection Validation
- [ ] Real-time detection of all 5 anti-pattern types
- [ ] Interactive gate functions with immediate prevention
- [ ] Multi-language support (TypeScript, Python, Java, Go)
- [ ] Integration with IDE editors for live detection

#### Mock Validation Testing
- [ ] Mock structure completeness verification
- [ ] Real API comparison and schema validation
- [ ] Test utility organization and pollution prevention
- [ ] Integration vs unit test boundary analysis

#### Developer Experience Validation
- [ ] Clear error messages with specific fix suggestions
- [ ] Interactive prompts with multiple resolution options
- [ ] Learning mode with detailed explanations
- [ ] Integration with existing testing frameworks

### 5. Migration Challenges and Solutions

#### Challenge 1: Real-time Anti-Pattern Detection
**Original:** Manual code review for anti-patterns
**Factory AI Enhancement:** Real-time AST analysis with immediate feedback

#### Challenge 2: Interactive Gate Functions
**Original:** Static guidelines and examples
**Factory AI Enhancement:** Interactive prevention during development with multiple options

#### Challenge 3: Mock Validation Across APIs
**Original:** Basic mock structure checking
**Factory AI Enhancement:** Comprehensive API schema validation with real-time comparison

### 6. Enhanced Features

#### Advanced Testing Analytics
- **Anti-Pattern Trends:** Track most common issues across codebase
- **Mock Complexity Metrics:** Monitor mock vs test complexity ratios
- **Test Quality Scores:** Evaluate test effectiveness and coverage
- **Refactoring Recommendations:** Suggest improvements to test structure

#### Integration with Testing Frameworks
```yaml
Framework Integration:
  Jest/React Testing:
    - Real-time component analysis during testing
    - Mock structure validation for React Testing Library
    - Integration with React Developer Tools
    
  Pytest/Python:
    - Mock validation against actual Python objects
    - Test file structure analysis and organization
    - Integration with Python AST analysis
    
  Go Testing:
    - Interface mock validation for Go interfaces
    - Test utility organization and structure
    - Integration with go test tooling
```

#### Team Collaboration Features
- **Anti-Pattern Prevention:** Team-wide standards and enforcement
- **Knowledge Sharing:** Common anti-patterns and solutions
- **Code Review Integration:** Automatic anti-pattern detection in PR reviews
- **Quality Gates:** Pre-commit validation with real-time feedback

## Implementation Timeline (3 Weeks)

### Week 1: Core Framework and Detection
- **Days 1-3:** Deep analysis of original skill and anti-pattern types
- **Days 4-5:** Design real-time detection algorithms and gate functions
- **Days 6-7:** Create comprehensive mock validation framework

### Week 2: Implementation and Integration
- **Days 8-10:** Implement core droid with enhanced anti-pattern detection
- **Days 11-12:** Create slash command with interactive gate functions
- **Days 13-14:** Integrate with testing frameworks and IDE support

### Week 3: Advanced Features and Testing
- **Days 15-17:** Implement analytics and team collaboration features
- **Days 18-19:** Comprehensive testing with various anti-pattern scenarios
- **Days 20-21:** Performance optimization and documentation

## Success Criteria

### Functional Requirements
- 100% of original anti-pattern prevention workflow preserved
- Real-time detection of all 5 anti-pattern types working
- Interactive gate functions with multiple resolution options
- Comprehensive mock validation and completion

### Quality Requirements
- Anti-pattern detection accuracy > 95%
- Mock structure validation coverage > 98%
- Zero false positives in critical anti-patterns
- Integration with major testing frameworks seamless

### Integration Requirements
- Support for TypeScript, Python, Java, Go
- Real-time IDE integration with immediate feedback
- Team collaboration and standards enforcement
- Comprehensive analytics and quality tracking