# Testing Skills With Subagents Migration Specification

## Analysis Summary
**Original Superpowers Skill:** testing-skills-with-subagents
**Core Philosophy:** TDD applied to process documentation - RED-GREEN-REFACTOR for skills
**Key Features:** Pressure scenarios, rationalization capture, loophole closing, bulletproof validation

## Migration Strategy

### 1. Enhanced Skill Testing through Factory AI

**Factory AI Integration Opportunities:**
- **Automated Pressure Scenario Generation:** Intelligent test case creation
- **Subagent Performance Analysis:** Track compliance and violation patterns
- **Real-time Rationalization Detection:** Natural language processing for excuse patterns
- **Bulletproof Validation:** Comprehensive skill validation under maximum pressure

**Advanced Testing Framework:**
```yaml
TDD for Skills Testing:
  RED Phase:
    - Baseline skill testing (without target skill)
    - Pressure scenario execution with realistic constraints
    - Verbatim failure documentation
    
  GREEN Phase:
    - Target skill implementation addressing specific failures
    - Pressure scenario execution (with skill active)
    - Compliance verification
    
  REFACTOR Phase:
    - Loophole identification and counter addition
    - Rationalization table updates
    - Meta-testing for skill clarity
```

### 2. Implementation Specifications

#### Core Droid Structure
```markdown
---
name: testing-skills-with-subagents
description: TDD for process documentation - RED-GREEN-REFACTOR CYCLE TO MAKE SKILLS BULLETPROOF
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, mcp__desktop-commander__start_process]
---

# Testing Skills With Subagents Droid

## Core Principle
TDD applied to process documentation: RED-GREEN-REFACTOR cycle to make skills bulletproof

## Enhanced Testing Process
1. RED: Baseline testing without target skill
2. GREEN: Implement skill addressing specific failures
3. REFACTOR: Close loopholes and prevent rationalizations
```

#### Slash Command (.factory/commands/testskill)
```markdown
# Test Skill Command
Apply TDD to process documentation for bulletproof validation

## Usage
`/testskill [skill-file]` or `/testskill`

## Process
1. Run baseline scenarios without target skill
2. Document failures and rationalizations verbatim
3. Implement skill improvements
4. Re-test with skill under pressure scenarios

$ARGUMENTS

**Features:**
- Automated pressure scenario generation
- Verbatim rationalization capture
- Loophole identification and closing
- Bulletproof validation under maximum pressure
```

### 3. Advanced Factory AI Features

#### Intelligent Pressure Scenario Generation
```typescript
// Advanced scenario generation algorithms
class PressureScenarioGenerator {
    generateRealisticScenarios(skillType: SkillType): PressureScenario[] {
        const baseScenarios = this.getBaseScenarios(skillType);
        const combinedPressures = this.combinePressures(baseScenarios);
        
        return combinedScenarios.map(pressure => ({
            type: pressure.type,
            constraints: pressure.constraints,
            timeLimit: pressure.timeLimit,
            authorityLevel: pressure.authority,
            realContext: this.generateRealContext(pressure),
            concreteOptions: this.generateConcreteOptions(pressure)
        }));
    }
    
    private combinePressures(scenarios: BaseScenario[]): CombinedPressure[] {
        // Combine 2-3 pressures for realistic scenarios
        return this.createPressureCombinations(scenarios, 3);
    }
}
```

#### Real-time Rationalization Detection
```typescript
// Natural language processing for excuse patterns
class RationalizationDetector {
    detectRationalizations(agentResponse: string): RationalizationPattern[] {
        const patterns = [
            /this case is different because/i,
            /i'm following the spirit not the letter/i,
            /being pragmatic means adapting/i,
            /deleting.*would be wasteful/i,
            /already manually tested/i,
            /tests after achieve same goals/i
        ];
        
        return patterns.map(pattern => ({
            type: this.categorizeRationalization(pattern),
            match: agentResponse.match(pattern),
            severity: this.assessSeverity(pattern),
            suggestedCounter: this.generateCounter(pattern)
        }));
    }
}
```

#### Comprehensive Loophole Analysis
```typescript
// Advanced loophole identification and closing
class LoopholeAnalyzer {
    identifyLoopholes(skillContent: string, observedViolations: Violation[]): Loophole[] {
        const loopholes = [];
        
        // Analyze skill content for potential escape routes
        const escapeRoutes = this.findEscapeRoutes(skillContent);
        
        for (const violation of observedViolations) {
            const matchingLoopholes = escapeRoutes.filter(
                route => route.matches(violation.type)
            );
            
            loopholes.push({
                type: violation.type,
                description: violation.description,
                currentGap: matchingLoopholes[0]?.description,
                suggestedFix: this.generateCounterMeasure(violation),
                severity: this.assessLoopholeRisk(violation)
            });
        }
        
        return loopholes;
    }
}
```

### 4. Success Criteria

**Functional Requirements:**
- 100% of original TDD for skills workflow preserved
- Automated pressure scenario generation working
- Real-time rationalization detection with >95% accuracy
- Comprehensive loophole analysis and closing

**Quality Requirements:**
- Pressure scenario generation covers all major pressure types
- Subagent compliance tracking and analytics functional
- Bulletproof validation under maximum pressure scenarios
- Zero false positives in rationalization detection

## Implementation Timeline (3 Weeks)

Same as other Phase 3 skills with focus on pressure scenario automation and loophole analysis.

## Success Criteria

### Functional Requirements
- 100% of original skill testing workflow preserved
- Automated pressure scenario generation working
- Real-time rationalization detection functional
- Comprehensive loophole analysis and closing

### Quality Requirements
- Pressure scenario realism and effectiveness > 90%
- Rationalization detection accuracy > 95%
- Loophole identification completeness > 98%
- Bulletproof validation success rate > 99%

### Integration Requirements
- Seamless integration with skill creation workflows
- Support for all skill types and categories
- Comprehensive analytics and reporting
- Team collaboration for skill testing