#!/usr/bin/env python3
"""Verify that all critical droids are implemented."""

import os
import sys

REQUIRED_DROIDS = [
    "test-driven-development",
    "systematic-debugging", 
    "brainstorming",
    "verification-before-completion",
    "condition-based-waiting",
    "defense-in-depth",
    "writing-plans",
    "executing-plans",
    "requesting-code-review",
    "receiving-code-review",
    "using-git-worktrees",
    "subagent-driven-development",
    "root-cause-tracing",           # NEW
    "finishing-a-development-branch", # NEW
    "dispatching-parallel-agents",  # NEW
    "testing-anti-patterns",        # NEW
    "testing-skills-with-subagents", # NEW
    "sharing-skills",               # NEW
    "writing-skills",
    "using-droids",
    "skill-checker"
]

def verify_droids():
    """Check that all required droids exist."""
    missing = []
    for droid in REQUIRED_DROIDS:
        droid_path = f".factory/droids/{droid}.md"
        if not os.path.exists(droid_path):
            missing.append(droid)
    
    if missing:
        print(f"❌ Missing droids: {missing}")
        return False
    else:
        print(f"✅ All {len(REQUIRED_DROIDS)} droids implemented")
        return True

def verify_commands():
    """Check that all required commands exist."""
    # Command mappings from droid names to command names
    command_mappings = {
        "test-driven-development": "tdd",
        "systematic-debugging": "debug",
        "brainstorming": "brainstorm", 
        "verification-before-completion": "verify",
        "condition-based-waiting": "condition-wait",
        "defense-in-depth": "defense-in-depth",
        "writing-plans": "plan",
        "executing-plans": "execute",
        "requesting-code-review": "review",
        "receiving-code-review": "handle-review",
        "using-git-worktrees": "worktree",
        "subagent-driven-development": "subdev",
        "root-cause-tracing": "root-cause-tracing",
        "finishing-a-development-branch": "finish-branch",
        "dispatching-parallel-agents": "parallel",
        "testing-anti-patterns": "anti-patterns",
        "testing-skills-with-subagents": "test-skills",
        "sharing-skills": "share",
        "writing-skills": "write-droid",
        "using-droids": "droids",
        "skill-checker": "skill-checker"
    }
    
    missing = []
    for droid, command in command_mappings.items():
        command_path = f".factory/commands/{command}.md"
        if not os.path.exists(command_path):
            missing.append(f"{droid} -> {command}")
    
    if missing:
        print(f"❌ Missing commands: {missing}")
        return False
    else:
        print(f"✅ All {len(command_mappings)} commands implemented")
        return True

def main():
    """Run all verification checks."""
    print("🔍 Droidpowers Completeness Verification")
    print("=" * 50)
    
    droids_ok = verify_droids()
    commands_ok = verify_commands()
    
    print("=" * 50)
    if droids_ok and commands_ok:
        print("🎉 All components implemented successfully!")
        print(f"📊 Summary: {len(REQUIRED_DROIDS)} droids + {len(REQUIRED_DROIDS)} commands = {len(REQUIRED_DROIDS) * 2} total files")
        return True
    else:
        print("❌ Verification failed - missing components detected")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)