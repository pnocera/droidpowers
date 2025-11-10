"""Test suite for finishing-a-development-branch droid."""

import os
import pytest


def test_finishing_branch_droid_exists():
    """Test that finishing-a-development-branch droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/finishing-a-development-branch.md"
    assert os.path.exists(droid_path), "Finishing a development branch droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Finishing a Development Branch" in content, "Should have correct title"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## Process" in content, "Should have Process section"
        assert "## Integration" in content, "Should have Integration section"


def test_finishing_branch_command_exists():
    """Test that finish-branch command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/finish-branch.md"
    assert os.path.exists(command_path), "Finish branch command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert len(content) > 0, "Command file should not be empty"


def test_finishing_branch_has_proper_phases():
    """Test that finishing-a-development-branch droid has required process phases."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/finishing-a-development-branch.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the three main phases mentioned in the task
    assert "Completion Assessment" in content, "Should have Completion Assessment phase"
    assert "Integration Options" in content, "Should have Integration Options phase"
    assert "Next Steps" in content, "Should have Next Steps phase"


def test_finishing_branch_usage_scenarios():
    """Test that finishing-a-development-branch droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/finishing-a-development-branch.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "implementation is complete" in content, "Should mention completion scenario"
    assert "all tests pass" in content, "Should mention test completion"
    assert "integration" in content, "Should mention integration options"


def test_finishing_branch_integration_options():
    """Test that finishing-a-development-branch droid provides integration options."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/finishing-a-development-branch.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for integration options mentioned in the task
    assert "Pull Request" in content, "Should mention Pull Request option"
    assert "Direct Merge" in content, "Should mention Direct Merge option"
    assert "Cleanup" in content, "Should mention cleanup option"


def test_finishing_branch_workflow_completeness():
    """Test that finishing-a-development-branch droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/finishing-a-development-branch.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = ["## Overview", "## Usage", "## Process", "## Integration"]
    for section in required_sections:
        assert section in content, f"Should have {section} section"