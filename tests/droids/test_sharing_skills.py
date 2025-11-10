"""Test suite for sharing-skills droid."""

import os
import pytest


def test_sharing_skills_droid_exists():
    """Test that sharing-skills droid is properly implemented."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    assert os.path.exists(droid_path), "Sharing skills droid should exist"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        assert "Sharing Skills" in content, "Should have correct title"
        assert "## Overview" in content, "Should have Overview section"
        assert "## Usage" in content, "Should have Usage section"
        assert "## Contribution Process" in content, "Should have Contribution Process section"
        assert "## Integration" in content, "Should have Integration section"


def test_sharing_skills_command_exists():
    """Test that share command is implemented."""
    command_path = "/mnt/e/Projects/obra/droidpowers/.factory/commands/share.md"
    assert os.path.exists(command_path), "Share command should exist"
    
    with open(command_path, 'r') as f:
        content = f.read()
        assert len(content) > 0, "Command file should not be empty"


def test_sharing_skills_contribution_process():
    """Test that sharing-skills droid has proper contribution process."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for the three main phases mentioned in the task
    assert "Preparation" in content, "Should have Preparation phase"
    assert "Repository Operations" in content, "Should have Repository Operations phase"
    assert "Pull Request" in content, "Should have Pull Request phase"


def test_sharing_skills_usage_scenarios():
    """Test that sharing-skills droid specifies proper usage scenarios."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for key usage scenarios
    assert "developed a useful skill" in content, "Should mention skill development"
    assert "contribute" in content, "Should mention contributing back"
    assert "upstream" in content, "Should mention upstream repository"


def test_sharing_skills_contribution_guidelines():
    """Test that sharing-skills droid includes contribution guidelines."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for contribution guideline sections
    assert "Quality Standards" in content, "Should have quality standards"
    assert "PR Requirements" in content, "Should have PR requirements"
    assert "thoroughly tested" in content, "Should mention testing requirements"


def test_sharing_skills_workflow_completeness():
    """Test that sharing-skills droid has complete workflow structure."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Verify YAML frontmatter exists
    assert content.startswith("---"), "Should have YAML frontmatter"
    assert "---" in content[10:], "Should have closing YAML frontmatter"
    
    # Verify key sections
    required_sections = [
        "## Overview", 
        "## Usage", 
        "## Contribution Process",
        "## Contribution Guidelines",
        "## Integration"
    ]
    for section in required_sections:
        assert section in content, f"Should have {section} section"


def test_sharing_skills_contribution_workflow():
    """Test that sharing-skills droid is marked as contribution workflow."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Should be marked as contribution workflow
    assert "Contribution workflow" in content, "Should be marked as contribution workflow"
    assert "community" in content, "Should mention community engagement"


def test_sharing_skills_repository_operations():
    """Test that sharing-skills droid covers proper repository operations."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for repository operation components
    assert "feature branch" in content, "Should mention feature branch creation"
    assert "commit" in content, "Should mention committing changes"
    assert "push" in content, "Should mention pushing to remote"


def test_sharing_skills_quality_standards():
    """Test that sharing-skills droid specifies quality standards."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for quality standards mentioned in the task
    assert "Documentation" in content, "Should mention documentation requirements"
    assert "conventions" in content, "Should mention coding standards"
    assert "solve real problems" in content, "Should mention solving real problems"


def test_sharing_skills_pr_requirements():
    """Test that sharing-skills droid specifies PR requirements."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for PR requirements mentioned in the task
    assert "description" in content, "Should mention clear description"
    assert "Examples" in content, "Should mention usage examples"
    assert "benefits" in content, "Should mention community benefits"


def test_sharing_skills_integrations():
    """Test that sharing-skills droid mentions proper integrations."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for integrations mentioned in the task
    assert "writing-skills" in content, "Should integrate with writing-skills"
    assert "testing-skills-with-subagents" in content, "Should integrate with testing-skills"


def test_sharing_skills_best_practices():
    """Test that sharing-skills droid includes best practices."""
    droid_path = "/mnt/e/Projects/obra/droidpowers/.factory/droids/sharing-skills.md"
    
    with open(droid_path, 'r') as f:
        content = f.read()
        
    # Check for best practices
    assert "Best Practices" in content, "Should have best practices section"
    assert "Start with small" in content, "Should mention starting small"
    assert "Engage" in content, "Should mention community engagement"