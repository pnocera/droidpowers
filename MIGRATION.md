# Superpowers to Droidpowers Migration Guide

## Overview
This guide helps users migrate from Claude Code superpowers to Factory AI droidpowers while maintaining workflow benefits.

## Key Differences

### Superpowers (Claude Code)
- Plugin-based installation
- Automatic skill discovery via Skill tool
- Session hooks for mandatory usage
- Marketplace distribution

### Droidpowers (Factory AI)
- File-based configuration
- Manual setup per project
- Gateway droid for enforcement
- Project-specific customization

## Migration Steps

### 1. Project Setup
```bash
# Create Factory AI directories
mkdir -p .factory/{droids,commands}

# Copy droid files
cp droidpowers/.factory/droids/* .factory/droids/
cp droidpowers/.factory/commands/* .factory/commands/

# Configure project
cp droidpowers/AGENTS.md.template AGENTS.md
# Edit AGENTS.md for your specific project
```

### 2. Skill Mapping

| Superpowers Skill | Droidpowers Equivalent |
|-------------------|----------------------|
| Skill tool discovery | `/droid skill-checker` |
| test-driven-development | `/droid test-driven-development` or `/tdd` |
| brainstorming | `/droid brainstorming` or `/brainstorm` |
| systematic-debugging | `/droid systematic-debugging` or `/debug` |
| verification-before-completion | `/droid verification` or `/verify` |

### 3. Workflow Adaptation

**Before (Superpowers):**
```
User asks to implement feature
→ Claude automatically checks for applicable skills
→ Uses mandatory skill if found
→ Follows skill workflow exactly
```

**After (Droidpowers):**
```
User asks to implement feature
→ Claude runs skill-checker droid
→ Identifies mandatory skills
→ Routes to appropriate droid/command
→ Follows same workflow with enforcement
```

### 4. Maintaining Compliance

The same "ABSOLUTELY MUST use skill" rule applies, enforced through:
- skill-checker gateway analysis
- Droid internal validation logic
- Project configuration in AGENTS.md
- Interactive compliance prompts

## Benefits of Migration

1. **Enhanced Discovery**: Factory AI's configuration system provides better project-specific skill matching
2. **Flexible Integration**: Mix and match skills with other Factory AI tools
3. **Improved Customization**: Adapt skills to specific project needs
4. **Better Documentation**: AGENTS.md provides comprehensive project context
5. **Team Collaboration**: Easier to share and standardize workflows across teams

## Testing Migration

1. **Test with existing project**: Try droidpowers on a familiar codebase
2. **Compare workflows**: Verify same outcomes as superpowers
3. **Check enforcement**: Ensure mandatory usage still works
4. **Team validation**: Get feedback from team members

## Troubleshooting

### Skill Not Detected
- Check AGENTS.md configuration
- Verify droid files are in correct location
- Run skill-checker manually: `/droid skill-checker`

### Enforcement Not Working
- Ensure skill-checker droid is installed
- Check project-specific skill rules in AGENTS.md
- Verify droid permissions and executable status

### Workflow Differences
- Compare original SKILL.md with new droid implementation
- Check for missing validation steps
- Verify all checkpoints are preserved