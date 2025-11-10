# Request Code Review Command
Dispatch code-reviewer subagent for technical validation

## Usage
`/review` or `/review [description]`

## Process
1. Extract git SHAs automatically
2. Analyze current changes and context
3. Dispatch code-reviewer subagent
4. Present findings for action

$ARGUMENTS

**Review Triggers:**
- Task completion (subagent-driven development)
- Major feature implementation
- Before merge to main

**Getting Started:**
1. Extract BASE_SHA and HEAD_SHA automatically
2. Describe what was implemented
3. Reference plan or requirements
4. Act on feedback immediately

**Review Early, Review Often!**