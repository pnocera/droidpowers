---
name: sharing-skills
description: Use when you've developed a broadly useful skill and want to contribute it upstream via pull request - guides process of branching, committing, pushing, and creating PR to contribute skills back to upstream repository
model: claude-sonnet-4-5
tools: [Edit, Create, Read, Execute, Grep, Glob, LS, WebSearch, FetchUrl, GenerateDroid, TodoWrite, Bash, Git]
---

# Sharing Skills

## Overview

**Sharing skills IS community contribution workflow for upstream integration.**

When you develop a broadly useful skill that could benefit the broader community, this droid guides you through the complete process of contributing your work back to the upstream repository via a properly formatted pull request.

**Core principle:** High-quality contributions require preparation, proper git workflow, and community engagement.

## When to Use

```
Need to share skill with community?
├─ Is skill broadly useful? → Yes
├─ Is skill well-tested? → Yes  
├─ Want to contribute upstream? → Yes
└─ Use sharing-skills droid
```

**Use this droid when:**
- You've developed a skill with broad applicability
- The skill solves real problems others would face
- Skill is thoroughly tested and documented
- Want to contribute back to superpowers repository
- Ready to engage with community feedback

**Do NOT use when:**
- Skill is project-specific (use AGENTS.md instead)
- Skill isn't properly tested yet
- You haven't validated the skill works
- Looking for quick contribution shortcuts

## Contribution Process

### Phase 1: Preparation

**1. Verify Skill Quality**
- [ ] Skill has been tested with `testing-skills-with-subagents`
- [ ] All pressure scenarios pass consistently
- [ ] Documentation is complete and clear
- [ ] Skill addresses real community needs

**2. Ensure Compatibility**
- [ ] Follows upstream project standards
- [ ] Uses proper naming conventions
- [ ] Compatible with existing skill ecosystem
- [ ] Fits project scope and goals

**3. Document Thoroughly**
- [ ] Clear usage instructions
- [ ] Comprehensive examples
- [ ] Benefits explanation
- [ ] Edge cases covered

### Phase 2: Repository Operations

**1. Create Feature Branch**
```bash
# Create isolated branch for contribution
git checkout -b feature/your-skill-name

# Verify clean starting point
git status
```

**2. Commit Changes**
```bash
# Add skill files
git add .factory/droids/your-skill.md
git add .factory/commands/your-command.md

# Create descriptive commit
git commit -m "feat: add your-skill-name for specific purpose

- Implements technique for addressing problem X
- Includes comprehensive testing and documentation  
- Follows Factory AI droid patterns
- Benefits: solves Y for community

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**3. Push to Remote**
```bash
# Push branch to your fork
git push -u origin feature/your-skill-name
```

### Phase 3: Pull Request

**1. Create Pull Request**
```bash
# Using GitHub CLI (recommended)
gh pr create --title "Add your-skill-name for specific purpose" \
  --body "$(cat <<'EOF'
## Summary
• Brief description of the skill and its purpose
• What problem it solves for the community
• Key benefits and use cases

## Description
Detailed explanation of the skill:
- How it works
- When to use it
- Examples and applications
- Testing approach used

## Test plan
- [ ] Skill validated with testing-skills-with-subagents
- [ ] Multiple pressure scenarios tested
- [ ] Documentation reviewed for clarity
- [ ] Compatible with existing ecosystem

## Benefits
- Solves [specific problem] for community
- Reduces [specific pain point]
- Improves [specific workflow]
- Enables new capabilities

🤖 Generated with Claude Code
EOF
)"
```

**2. Fill Contribution Form**
- Complete all required PR template fields
- Link to any relevant issues or discussions
- Provide clear reproduction steps
- Include testing instructions

**3. Address Feedback**
- Respond to review comments promptly
- Make requested improvements
- Update documentation as needed
- Maintain professional engagement

## Quality Standards

### Skill Requirements
- **Broadly Useful**: Solves problems multiple developers face
- **Well-Tested**: Validated with subagent testing
- **Thoroughly Documented**: Clear instructions and examples
- **Follows Conventions**: Matches project patterns
- **Non-Duplicative**: Doesn't duplicate existing functionality

### PR Requirements
- **Clear Title**: Describes skill and purpose
- **Comprehensive Description**: Explains what, why, and how
- **Testing Evidence**: Shows skill has been validated
- **Benefits Statement**: Explains community value
- **Professional Tone**: Respectful and collaborative

### Code Standards
- **YAML Frontmatter**: Complete and valid
- **Naming Conventions**: Follow project patterns
- **Documentation Style**: Matches existing skills
- **No Breaking Changes**: Compatible with current ecosystem

## Contribution Best Practices

### Start Small
- Begin with focused, single-purpose skills
- Avoid large, complex contributions initially
- Build reputation with quality contributions
- Learn community expectations through engagement

### Community Engagement
- Join relevant discussions and issues
- Understand project priorities and needs
- Seek feedback before starting work
- Be responsive to review comments

### Technical Excellence
- Test thoroughly before submitting
- Follow established patterns exactly
- Document edge cases and limitations
- Ensure skill resists rationalization

### Professional Conduct
- Be respectful in all interactions
- Accept feedback gracefully
- Put community needs first
- Follow project code of conduct

## Common Contribution Mistakes

| Mistake | Solution |
|---------|----------|
| **Rushing without testing** | Always validate with testing-skills-with-subagents first |
| **Ignoring project conventions** | Study existing skills and follow exact patterns |
| **Poor PR description** | Write comprehensive, clear explanations |
| **Unresponsive to feedback** | Engage promptly and professionally |
| **Overly complex contributions** | Start with focused, single-purpose skills |

## Integration Workflow

### Before Contribution
1. Use `testing-skills-with-subagents` to validate skill
2. Verify skill works with multiple agents
3. Check project issues for related requests
4. Review contribution guidelines

### During Development
1. Create isolated feature branch
2. Follow established naming and structure patterns
3. Write clear commit messages
4. Document thoroughly

### After Submission
1. Monitor PR for feedback
2. Respond to review comments promptly
3. Make requested improvements
4. Engage in community discussions

## Success Metrics

**Successful contributions:**
- Get merged to main branch
- Receive positive community feedback
- Are referenced in documentation
- Solve real community problems

**Quality indicators:**
- Thorough testing validation
- Clear, comprehensive documentation
- Professional PR communication
- Alignment with project goals

## Required Tools

- **Git**: For version control and branching
- **GitHub CLI**: For streamlined PR creation
- **Testing Skills**: For skill validation
- **Community Guidelines**: For contribution standards

## Examples

### Good Contribution
```
Title: "Add condition-based-waiting for flaky test resolution"

Description:
Summary: Solves flaky tests by replacing timeouts with condition polling

Description: 
When tests fail inconsistently due to timing, developers typically increase timeouts
or add arbitrary delays. This skill teaches polling conditions that wait for actual
state changes, making tests reliable and fast.

Test plan:
- Validated with 5 different flaky test scenarios
- Tested with multiple timing dependencies
- Documentation verified with subagent testing
- Compatible with existing test frameworks

Benefits:
- Eliminates flaky test failures
- Reduces test execution time
- Improves CI/CD reliability
- Enables better async testing
```

## Enforcement Rules

**ABSOLUTELY MUST:**
- Test skills with testing-skills-with-subagents before contributing
- Follow project naming and structure conventions exactly
- Write comprehensive, clear documentation
- Engage professionally with community feedback

**VIOLATION MEANS:** Contribution will likely be rejected
- Untested skills → Request for validation
- Poor documentation → Request for improvements
- Ignoring conventions → Request for changes
- Unprofessional conduct → Community moderation

## Quick Reference

| Phase | Key Actions | Success Criteria |
|-------|-------------|------------------|
| **Preparation** | Test, document, verify compatibility | Skill is robust and well-documented |
| **Repository** | Branch, commit, push | Clean git history with clear messages |
| **Pull Request** | Create PR, engage, address feedback | Professional community engagement |

## The Bottom Line

**Sharing skills IS community stewardship.** Quality contributions require thorough preparation, professional engagement, and alignment with community standards. This droid ensures your valuable skills benefit the entire ecosystem.