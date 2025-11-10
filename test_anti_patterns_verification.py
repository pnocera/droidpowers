#!/usr/bin/env python3
"""
Verification script for testing-anti-patterns droid implementation.
This script verifies that Task 4 has been implemented correctly.
"""

import os
import sys

def test_testing_anti_patterns_droid_exists():
    """Test that testing-anti-patterns droid is properly implemented."""
    droid_path = ".factory/droids/testing-anti-patterns.md"
    
    if not os.path.exists(droid_path):
        print("❌ testing-anti-patterns droid file does not exist")
        return False
    
    with open(droid_path, 'r') as f:
        content = f.read()
    
    # Check for required YAML frontmatter fields
    required_fields = ['id: testing-anti-patterns', 'title: Testing Anti-Patterns', 'category: advanced']
    for field in required_fields:
        if field not in content:
            print(f"❌ Missing required field: {field}")
            return False
    
    # Check for key content sections
    required_sections = [
        '# Testing Anti-Patterns',
        '## Usage',
        '## Common Anti-Patterns',
        '## Prevention Checklist',
        '## Integration'
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"❌ Missing required section: {section}")
            return False
    
    # Check for educational content
    educational_content = [
        'Mock Behavior Testing',
        'Production Code Pollution',
        'Mocking Without Understanding',
        'Test-Only Methods'
    ]
    
    for content_item in educational_content:
        if content_item not in content:
            print(f"❌ Missing educational content: {content_item}")
            return False
    
    print("✅ testing-anti-patterns droid is properly implemented")
    return True

def test_anti_patterns_command_exists():
    """Test that anti-patterns command is properly implemented."""
    command_path = ".factory/commands/anti-patterns.md"
    
    if not os.path.exists(command_path):
        print("❌ anti-patterns command file does not exist")
        return False
    
    with open(command_path, 'r') as f:
        content = f.read()
    
    # Check for required YAML frontmatter fields
    required_fields = ['id: anti-patterns', 'title: Anti-Patterns', 'droid: testing-anti-patterns']
    for field in required_fields:
        if field not in content:
            print(f"❌ Missing required command field: {field}")
            return False
    
    # Check for key command sections
    required_sections = [
        '# Anti-Patterns Command',
        '## Usage',
        '## Integration'
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"❌ Missing required command section: {section}")
            return False
    
    print("✅ anti-patterns command is properly implemented")
    return True

def test_file_sizes_and_structure():
    """Test that files have reasonable content size and structure."""
    
    droid_path = ".factory/droids/testing-anti-patterns.md"
    command_path = ".factory/commands/anti-patterns.md"
    
    # Check droid file size (should be comprehensive)
    with open(droid_path, 'r') as f:
        droid_content = f.read()
    
    if len(droid_content) < 1000:
        print("❌ testing-anti-patterns droid seems too short for comprehensive content")
        return False
    
    # Check command file size (should be concise but complete)
    with open(command_path, 'r') as f:
        command_content = f.read()
    
    if len(command_content) < 200:
        print("❌ anti-patterns command seems too short for proper implementation")
        return False
    
    print("✅ Files have appropriate content sizes")
    return True

def test_integration_references():
    """Test that integration references are correct."""
    
    droid_path = ".factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
    
    # Check for integration with other droids
    required_integrations = [
        'test-driven-development',
        'verification-before-completion',
        'systematic-debugging'
    ]
    
    for integration in required_integrations:
        if integration not in content:
            print(f"❌ Missing integration reference: {integration}")
            return False
    
    print("✅ Integration references are correct")
    return True

def main():
    """Run all verification tests."""
    print("🔍 Verifying Task 4: testing-anti-patterns implementation")
    print()
    
    tests = [
        test_testing_anti_patterns_droid_exists,
        test_anti_patterns_command_exists,
        test_file_sizes_and_structure,
        test_integration_references
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    if passed == total:
        print(f"🎉 All {total} tests passed! Task 4 implementation is complete.")
        return 0
    else:
        print(f"❌ {total - passed} tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())