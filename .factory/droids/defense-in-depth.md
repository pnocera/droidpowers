---
name: defense-in-depth
description: Use when invalid data causes failures deep in execution, requiring validation at multiple system layers - validates at every layer data passes through to make bugs structurally impossible
model: claude-sonnet-4-5
tools: [Edit, Create, Read, Execute, Grep, Glob, LS, WebSearch, FetchUrl, GenerateDroid, TodoWrite]
---

# Defense-in-Depth Validation

## Overview

When you fix a bug caused by invalid data, adding validation at one place feels sufficient. But that single check can be bypassed by different code paths, refactoring, or mocks.

**Core principle:** Validate at EVERY layer data passes through. Make the bug structurally impossible.

## Why Multiple Layers

Single validation: "We fixed the bug"
Multiple layers: "We made the bug impossible"

Different layers catch different cases:
- Entry validation catches most bugs
- Business logic catches edge cases
- Environment guards prevent context-specific dangers
- Debug logging helps when other layers fail

## The Four Layers

### Layer 1: Entry Point Validation
**Purpose:** Reject obviously invalid input at API boundary

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory cannot be empty');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory does not exist: ${workingDirectory}`);
  }
  if (!statSync(workingDirectory).isDirectory()) {
    throw new Error(`workingDirectory is not a directory: ${workingDirectory}`);
  }
  // ... proceed
}
```

### Layer 2: Business Logic Validation
**Purpose:** Ensure data makes sense for this operation

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('projectDir required for workspace initialization');
  }
  // ... proceed
}
```

### Layer 3: Environment Guards
**Purpose:** Prevent dangerous operations in specific contexts

```typescript
async function gitInit(directory: string) {
  // In tests, refuse git init outside temp directories
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `Refusing git init outside temp dir during tests: ${directory}`
      );
    }
  }
  // ... proceed
}
```

### Layer 4: Debug Instrumentation
**Purpose:** Capture context for forensics

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('About to git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  // ... proceed
}
```

## Applying the Pattern

When you find a bug:

1. **Trace the data flow** - Where does bad value originate? Where used?
2. **Map all checkpoints** - List every point data passes through
3. **Add validation at each layer** - Entry, business, environment, debug
4. **Test each layer** - Try to bypass layer 1, verify layer 2 catches it

## Example from Session

Bug: Empty `projectDir` caused `git init` in source code

**Data flow:**
1. Test setup → empty string
2. `Project.create(name, '')`
3. `WorkspaceManager.createWorkspace('')`
4. `git init` runs in `process.cwd()`

**Four layers added:**
- Layer 1: `Project.create()` validates not empty/exists/writable
- Layer 2: `WorkspaceManager` validates projectDir not empty
- Layer 3: `WorktreeManager` refuses git init outside tmpdir in tests
- Layer 4: Stack trace logging before git init

**Result:** All 1847 tests passed, bug impossible to reproduce

## Key Insight

All four layers were necessary. During testing, each layer caught bugs the others missed:
- Different code paths bypassed entry validation
- Mocks bypassed business logic checks
- Edge cases on different platforms needed environment guards
- Debug logging identified structural misuse

**Don't stop at one validation point.** Add checks at every layer.

## When to Apply

**Apply when:**
- Bug causes system-wide failure from invalid data
- Data transformation occurs across multiple layers
- Complex state management with multiple entry points
- External inputs can trigger deep system issues
- Security implications from malformed data

**Don't apply for:**
- Simple data validation at UI level
- Temporary debugging statements (use Layer 4 alone)
- Performance-critical paths where validation cost outweighs risk

## Enforcement Rules

**ABSOLUTELY MUST use defense-in-depth when:**
- Fixing data validation bugs that caused system failures
- Adding external input handling to critical operations
- Implementing security boundaries around dangerous operations

**VIOLATION MEANS:** Add all four validation layers
- Single-point validation → Expand to four layers
- Missing environment guards → Add context-specific protection
- No debug instrumentation → Add Layer 4 logging

## Implementation Checklist

### For Each Bug Fix
- [ ] Trace complete data flow from source to failure
- [ ] Add Layer 1: Entry point validation
- [ ] Add Layer 2: Business logic validation  
- [ ] Add Layer 3: Environment protection guards
- [ ] Add Layer 4: Debug instrumentation
- [ ] Test layer bypass scenarios
- [ ] Verify bug is structurally impossible

### For New Features
- [ ] Identify potential invalid data inputs
- [ ] Map all data transformation layers
- [ ] Plan four-layer validation strategy
- [ ] Implement progressive validation layers
- [ ] Add comprehensive testing for failure modes
