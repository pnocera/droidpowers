"""Test suite for dispatching-parallel-agents droid."""

import os
import pytest


def test_dispatching_parallel_droid_exists():
    """Test that dispatching-parallel-agents droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    assert os.path.exists(droid_path), "Dispatching parallel agents droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Dispatching Parallel Agents" in content, "Should have correct title"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## Process" in content, "Should have Process section"
        assert "## Requirements" in content, "Should have Requirements section"


def test_dispatching_parallel_command_exists():
    """Test that parallel command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/parallel.md"
    assert os.path.exists(command_path), "Parallel command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert len(content) > 0, "Command file should not be empty"


def test_dispatching_parallel_has_proper_phases():
    """Test that dispatching-parallel-agents droid has required process phases."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the three main phases mentioned in the task
    assert "Problem Analysis" in content, "Should have Problem Analysis phase"
    assert "Parallel Dispatch" in content, "Should have Parallel Dispatch phase"
    assert "Integration" in content, "Should have Integration phase"


def test_dispatching_parallel_usage_scenarios():
    """Test that dispatching-parallel-agents droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "independent failures" in content, "Should mention independent failures"
    assert "parallel" in content, "Should mention parallel execution"
    assert "concurrent" in content or "concurrency" in content, "Should mention concurrency"


def test_dispatching_parallel_requirements():
    """Test that dispatching-parallel-agents droid specifies proper requirements."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for requirements mentioned in the task
    assert "3" in content and "independent" in content, "Should mention minimum 3 independent failures"
    assert "no shared state" in content or "shared state" in content, "Should mention shared state constraints"


def test_dispatching_parallel_workflow_completeness():
    """Test that dispatching-parallel-agents droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = ["## Overview", "## Usage", "## Process", "## Requirements"]
    for section in required_sections:
        assert section in content, f"Should have {section} section"


def test_dispatching_parallel_advanced_workflow():
    """Test that dispatching-parallel-agents is marked as advanced workflow."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/dispatching-parallel-agents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Should be marked as advanced workflow for complex debugging scenarios
    assert "Advanced" in content, "Should be marked as advanced workflow"
    assert "debugging" in content, "Should mention debugging scenarios"