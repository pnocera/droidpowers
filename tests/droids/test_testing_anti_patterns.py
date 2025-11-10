"""Test suite for testing-anti-patterns droid."""

import os
import pytest


def test_testing_anti_patterns_droid_exists():
    """Test that testing-anti-patterns droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    assert os.path.exists(droid_path), "Testing anti-patterns droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Testing Anti-Patterns" in content, "Should have correct title"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## Common Anti-Patterns" in content, "Should have Common Anti-Patterns section"
        assert "## Prevention Checklist" in content, "Should have Prevention Checklist section"


def test_testing_anti_patterns_command_exists():
    """Test that anti-patterns command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/anti-patterns.md"
    assert os.path.exists(command_path), "Anti-patterns command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert len(content) > 0, "Command file should not be empty"


def test_testing_anti_patterns_common_patterns():
    """Test that testing-anti-patterns droid covers common anti-patterns."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the 4 main anti-patterns mentioned in the task
    assert "Mock Behavior Testing" in content, "Should cover Mock Behavior Testing"
    assert "Production Code Pollution" in content, "Should cover Production Code Pollution"
    assert "Mocking Without Understanding" in content, "Should cover Mocking Without Understanding"
    assert "Test-Only Methods" in content, "Should cover Test-Only Methods"


def test_testing_anti_patterns_usage_scenarios():
    """Test that testing-anti-patterns droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "writing tests" in content, "Should mention writing new tests"
    assert "mocks" in content, "Should mention adding mocks"
    assert "test-only methods" in content, "Should mention test-only methods in production"


def test_testing_anti_patterns_prevention_checklist():
    """Test that testing-anti-patterns droid has a proper prevention checklist."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for checklist items mentioned in the task
    assert "No test-only methods" in content, "Should mention no test-only methods"
    assert "mocks represent real dependencies" in content, "Should mention accurate mocks"
    assert "actual behavior" in content, "Should mention testing actual behavior"


def test_testing_anti_patterns_educational_component():
    """Test that testing-anti-patterns droid is marked as educational component."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Should be marked as educational component for test quality
    assert "Educational" in content, "Should be marked as educational component"
    assert "test quality" in content, "Should mention test quality"


def test_testing_anti_patterns_workflow_completeness():
    """Test that testing-anti-patterns droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = [
        "## Overview", 
        "## Usage", 
        "## Common Anti-Patterns", 
        "## Prevention Checklist",
        "## Integration"
    ]
    for section in required_sections:
        assert section in content, f"Should have {section} section"


def test_testing_anti_patterns_integrations():
    """Test that testing-anti-patterns droid mentions proper integrations."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-anti-patterns.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for integrations mentioned in the task
    assert "test-driven-development" in content, "Should integrate with TDD"
    assert "verification-before-completion" in content, "Should integrate with verification"