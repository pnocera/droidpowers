"""Test suite for root-cause-tracing droid."""

import os
import sys
import unittest


def test_root_cause_tracing_droid_exists():
    """Test that root-cause-tracing droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/root-cause-tracing.md"
    assert os.path.exists(droid_path), "Root cause tracing droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Root Cause Tracing" in content, "Should have correct title"
        assert "systematic-debugging" in content, "Should reference dependent skills"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## Process" in content, "Should have Process section"
        assert "## Integration" in content, "Should have Integration section"


def test_root_cause_tracing_command_exists():
    """Test that root-cause-tracing command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/root-cause-tracing.md"
    assert os.path.exists(command_path), "Root cause tracing command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert "Root Cause Tracing" in content, "Should mention the droid name"
        assert len(content) > 0, "Command file should not be empty"


def test_root_cause_tracing_has_proper_phases():
    """Test that root-cause-tracing droid has required process phases."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/root-cause-tracing.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the three main phases mentioned in the task
    assert "Error Analysis" in content, "Should have Error Analysis phase"
    assert "Backward Tracing" in content, "Should have Backward Tracing phase"
    assert "Source Identification" in content, "Should have Source Identification phase"


def test_root_cause_tracing_usage_scenarios():
    """Test that root-cause-tracing droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/root-cause-tracing.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "deep in the execution" in content, "Should mention deep execution scenarios"
    assert "trace back" in content or "trace backward" in content, "Should mention backward tracing"
    assert "original source" in content, "Should mention finding original source"


def test_root_cause_tracing_workflow_completeness():
    """Test that root-cause-tracing droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/root-cause-tracing.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = ["## Overview", "## Usage", "## Process", "## Integration"]
    for section in required_sections:
        assert section in content, f"Should have {section} section"