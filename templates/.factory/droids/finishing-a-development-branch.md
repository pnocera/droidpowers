---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
model: claude-sonnet-4-5
tools: [Task, Read, Write, Edit, Bash, TodoWrite]
---

# Finishing a Development Branch

## Overview

Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup.

## Usage

Run this droid when:
- Implementation is complete
- All tests are passing
- You need to decide next steps for integration

## Process

### Phase 1: Completion Assessment
1. **Verify implementation** - Is the feature complete?
2. **Check test coverage** - Are all scenarios tested?
3. **Review quality** - Does code meet standards?

### Phase 2: Integration Options
1. **Create Pull Request** - For review and collaboration
2. **Direct Merge** - For simple changes
3. **Cleanup and Archive** - For experimental work

### Phase 3: Next Steps
1. **Execute chosen option** - Follow the selected path
2. **Clean up workspace** - Remove temporary files
3. **Update documentation** - Ensure docs are current

## Integration

**Required by:** multiple skills for workflow completion
**Integrates with:** verification-before-completion, requesting-code-review

## Options Presented

- Create PR with comprehensive description
- Direct merge to main branch
- Feature branch cleanup
- Documentation updates