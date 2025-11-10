# Droidpowers Testing Guide

## Manual Testing Checklist

### Gateway Droid (skill-checker)
- [ ] Detects "implement" tasks → routes to TDD
- [ ] Detects "debug" tasks → routes to systematic-debugging  
- [ ] Detects "design" tasks → routes to brainstorming
- [ ] Enforces mandatory skill usage
- [ ] Provides clear routing instructions

### TDD Droid
- [ ] Enforces "no code without test first" rule
- [ ] Validates test failure before implementation
- [ ] Ensures minimal implementation approach
- [ ] Maintains test during refactoring
- [ ] Supports multiple test frameworks

### Brainstorming Droid
- [ ] Asks clarifying questions one at a time
- [ ] Explores multiple approaches
- [ ] Presents design incrementally
- [ ] Documents final design
- [ ] Creates implementation plan

### Slash Commands
- [ ] `/tdd` launches TDD workflow correctly
- [ ] `/brainstorm` starts collaborative design
- [ ] Commands accept arguments properly
- [ ] Error handling works for missing arguments

### Project Configuration
- [ ] AGENTS.md template works for different project types
- [ ] Skills correctly mapped to project needs
- [ ] Build commands integrate properly
- [ ] Team conventions documented clearly

## Automated Testing

### Droid YAML Validation
```bash
# Validate all droid YAML frontmatter
for droid in .factory/droids/*.md; do
    echo "Validating $droid"
    # Add YAML validation command
done
```

### Command Permissions
```bash
# Ensure all commands are executable
find .factory/commands -type f -exec chmod +x {} \;
find .factory/commands -type f -exec test -x {} \; -print
```

### Integration Tests
- Test skill discovery with various project types
- Verify enforcement mechanisms work
- Check compliance tracking functionality
- Validate migration from superpowers

## Performance Testing

- Droid loading time: < 2 seconds
- Skill analysis time: < 1 second  
- Command response time: < 500ms
- Memory usage: < 50MB per active droid