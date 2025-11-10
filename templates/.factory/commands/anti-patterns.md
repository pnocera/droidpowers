---
id: anti-patterns
title: Anti-Patterns
description: Factory AI command for testing anti-patterns prevention
type: command
category: testing
droid: testing-anti-patterns
tags:
  - testing
  - anti-patterns
  - quality
  - test-design
---

# Anti-Patterns Command

Factory AI command implementation for testing-anti-patterns droid.

## Usage

```bash
/anti-patterns
```

This command activates the testing-anti-patterns droid to help prevent common testing mistakes and maintain test quality.

## What This Command Does

When you run `/anti-patterns`, it will:

1. **Analyze your current testing context** - Identify if you're writing tests, adding mocks, or reviewing existing test code

2. **Provide prevention guidance** - Help you avoid common testing anti-patterns like:
   - Testing mock behavior instead of real behavior
   - Adding test-only methods to production code
   - Mocking without understanding dependencies
   - Creating fragile tests

3. **Educate on best practices** - Share proven testing patterns and approaches

4. **Review current approach** - Check if your current testing strategy follows best practices

## Example Scenarios

**Writing New Tests:**
```bash
/anti-patterns
# "I'm writing tests for a new user authentication feature"
# Droid provides guidance on avoiding mock behavior testing and production pollution
```

**Adding Mocks:**
```bash
/anti-patterns
# "I need to mock a payment gateway for my order service tests"
# Droid helps ensure you understand the dependency before mocking
```

**Code Review:**
```bash/anti-patterns
# "I'm reviewing test code that seems to have test-only methods"
# Droid provides specific guidance on fixing production pollution
```

## Integration

- **Activates:** testing-anti-patterns droid
- **Pairs with:** /tdd for comprehensive testing workflow
- **Follows:** /verify for quality assurance
- **Leads to:** /review for code review guidance

## Quick Start

1. Run `/anti-patterns` when working with tests
2. Answer questions about your testing context
3. Apply the prevention checklist provided
4. Review examples of good vs. bad patterns
5. Implement recommended improvements

This command ensures your tests remain maintainable, meaningful, and free from common anti-patterns.