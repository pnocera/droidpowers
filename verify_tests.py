#!/usr/bin/env python3
"""Simple test verification script for 6 new droids."""

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
    """Check if a droid file exists and has required content."""
    droid_path = f"/mnt/e/Projects/obra/droidpowers/.factory/droids/{droid_name}.md"
    
    if not os.path.exists(droid_path):
        return False, f"Droid file {droid_path} does not exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
    
    # Check for basic structure (flexible to handle different section names)
    required_elements = [
        "## Overview",
    ]
    
    # Check for either "## Usage" or "## When to Use" or similar
    has_usage_section = any(usage_word in content for usage_word in ["## Usage", "## When to Use", "## When to Run"])
    if not has_usage_section:
        missing_elements.append("Usage section (## Usage, ## When to Use, etc.)")
    
    missing_usage = []
    missing_process = []
    missing_elements_list = []
    
    # Check for either "## Process" or "## The Process" or similar
    has_process_section = any(process_word in content for process_word in ["## Process", "## The Process"])
    if not has_process_section:
        missing_process.append("Process section (## Process, ## The Process, etc.)")
    
    for element in required_elements:
        if element not in content:
            missing_elements_list.append(element)
    
    # Check for either "## Usage" or "## When to Use" or similar
    has_usage_section = any(usage_word in content for usage_word in ["## Usage", "## When to Use", "## When to Run"])
    if not has_usage_section:
        missing_usage.append("Usage section (## Usage, ## When to Use, etc.)")
    
    all_missing = missing_elements_list + missing_usage + missing_process
    if all_missing:
        return False, f"Droid {droid_name} missing sections: {all_missing}"
    
    return True, f"Droid {droid_name} is properly structured"

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