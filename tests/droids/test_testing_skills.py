"""Test suite for testing-skills-with-subagents droid."""

import os
import pytest


def test_testing_skills_droid_exists():
    """Test that testing-skills-with-subagents droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    assert os.path.exists(droid_path), "Testing skills with subagents droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Testing Skills With Subagents" in content, "Should have correct title"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## RED-GREEN-REFACTOR for Skills" in content, "Should have TDD cycle section"
        assert "## Testing Process" in content, "Should have Testing Process section"


def test_testing_skills_command_exists():
    """Test that test-skills command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/test-skills.md"
    assert os.path.exists(command_path), "Test-skills command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert len(content) > 0, "Command file should not be empty"


def test_testing_skills_tdd_cycle():
    """Test that testing-skills-with-subagents droid covers TDD cycle."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the three TDD phases mentioned in the task
    assert "RED:" in content, "Should have RED phase"
    assert "GREEN:" in content, "Should have GREEN phase"
    assert "REFACTOR:" in content, "Should have REFACTOR phase"


def test_testing_skills_red_phase():
    """Test that testing-skills-with-subagents droid has proper RED phase."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for RED phase components
    assert "Run baseline test" in content, "Should mention baseline testing"
    assert "Document expected behavior" in content, "Should mention documenting behavior"
    assert "failure without skill" in content, "Should mention testing without skill"


def test_testing_skills_green_phase():
    """Test that testing-skills-with-subagents droid has proper GREEN phase."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for GREEN phase components
    assert "Implement minimal skill" in content, "Should mention minimal implementation"
    assert "Test with subagents" in content, "Should mention testing with subagents"
    assert "passes tests" in content, "Should mention passing tests"


def test_testing_skills_usage_scenarios():
    """Test that testing-skills-with-subagents droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "creating new skills" in content, "Should mention creating skills"
    assert "editing existing skills" in content, "Should mention editing skills"
    assert "before deploying" in content, "Should mention deployment validation"


def test_testing_skills_testing_process():
    """Test that testing-skills-with-subagents droid has comprehensive testing process."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for testing process components
    assert "Baseline Testing" in content, "Should have baseline testing section"
    assert "Skill Validation" in content, "Should have skill validation section"
    assert "Subagent Testing" in content, "Should have subagent testing section"


def test_testing_skills_meta_skill():
    """Test that testing-skills-with-subagents droid is marked as meta-skill."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Should be marked as meta-skill for skill validation
    assert "Meta-skill" in content, "Should be marked as meta-skill"
    assert "validation" in content, "Should mention validation"
    assert "quality assurance" in content, "Should mention quality assurance"


def test_testing_skills_workflow_completeness():
    """Test that testing-skills-with-subagents droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = [
        "## Overview", 
        "## Usage", 
        "## RED-GREEN-REFACTOR for Skills",
        "## Testing Process",
        "## Integration"
    ]
    for section in required_sections:
        assert section in content, f"Should have {section} section"


def test_testing_skills_robustness():
    """Test that testing-skills-with-subagents droid emphasizes robustness."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/testing-skills-with-subagents.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for robustness mentions
    assert "robust" in content, "Should mention robustness"
    assert "resists rationalization" in content, "Should mention resisting rationalization"
    assert "bulletproof" in content, "Should mention bulletproofing"