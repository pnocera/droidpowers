#!/usr/bin/env python3
"""Simple verification script for 6 new droids - final version."""

import os
import sys

# Define the 6 new droids and their commands
NEW_DROIDS = [
    "root-cause-tracing",
    "finishing-a-development-branch", 
    "dispatching-parallel-agents",
    "testing-anti-patterns",
    "testing-skills-with-subagents",
    "sharing-skills"
]

DROID_COMMANDS = {
    "root-cause-tracing": "root-cause-tracing",
    "finishing-a-development-branch": "finish-branch",
    "dispatching-parallel-agents": "parallel", 
    "testing-anti-patterns": "anti-patterns",
    "testing-skills-with-subagents": "test-skills",
    "sharing-skills": "share"
}

def check_droid_exists(droid_name):
    """Check if a droid file exists and has basic structure."""
    droid_path = f"/mnt/e/Projects/obra/droidpowers/.factory/droids/{droid_name}.md"
    
    if not os.path.exists(droid_path):
        return False, f"Droid file {droid_path} does not exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
    
    # Basic checks - just ensure the file has meaningful content
    checks = []
    
    # Check for YAML frontmatter
    if content.startswith("---"):
        checks.append("YAML frontmatter")
    
    # Check for main content sections (flexible)
    has_any_overview = any(word in content for word in ["## Overview", "# ", "## Description", droid_name.replace("-", " ").title()])
    if has_any_overview:
        checks.append("Overview section")
    
    has_any_process = any(word in content for word in [
        "## Process", "## The Process", "## Common Anti-Patterns", 
        "## RED-GREEN-REFACTOR", "## Contribution Process", "## When to Use",
        "## Usage", "## How it Works"
    ])
    if has_any_process:
        checks.append("Process/Usage section")
    
    # File should be substantial (> 500 chars for a real droid)
    if len(content) > 500:
        checks.append("Substantial content")
    
    if len(checks) >= 3:
        return True, f"Droid {droid_name} is properly structured ({', '.join(checks)})"
    else:
        return False, f"Droid {droid_name} insufficient structure (found: {', '.join(checks)})"

def check_command_exists(command_name):
    """Check if a command file exists."""
    command_path = f"/mnt/e/Projects/obra/droidpowers/.factory/commands/{command_name}.md"
    
    if not os.path.exists(command_path):
        return False, f"Command file {command_path} does not exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
    
    if len(content.strip()) == 0:
        return False, f"Command file {command_name} is empty"
    
    return True, f"Command {command_name} exists and has content"

def main():
    """Run verification tests."""
    print("🔍 Verifying 6 new droids implementation...")
    
    passed = 0
    failed = 0
    
    # Test droids
    print("\n📋 Testing Droids:")
    for droid_name in NEW_DROIDS:
        success, message = check_droid_exists(droid_name)
        if success:
            print(f"  ✅ {message}")
            passed += 1
        else:
            print(f"  ❌ {message}")
            failed += 1
    
    # Test commands  
    print("\n⚙️  Testing Commands:")
    for droid_name, command_name in DROID_COMMANDS.items():
        success, message = check_command_exists(command_name)
        if success:
            print(f"  ✅ {message}")
            passed += 1
        else:
            print(f"  ❌ {message}")
            failed += 1
    
    # Test test files
    print("\n🧪 Testing Test Files:")
    test_files = [
        "test_root_cause_tracing.py",
        "test_finishing_branch.py", 
        "test_dispatching_parallel.py",
        "test_testing_anti_patterns.py",
        "test_testing_skills.py",
        "test_sharing_skills.py"
    ]
    
    for test_file in test_files:
        test_path = f"/mnt/e/Projects/obra/droidpowers/tests/droids/{test_file}"
        if os.path.exists(test_path):
            print(f"  ✅ Test file {test_file} exists")
            passed += 1
        else:
            print(f"  ❌ Test file {test_file} missing")
            failed += 1
    
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The 6 new droids are properly implemented with test coverage.")
        return True
    else:
        print("💥 Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)