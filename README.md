# Droidpowers CLI

Install Droidpowers Factory AI skills system in any project with a single command.

## Quick Start

```bash
npx droidpowers
```

That's it! The `.factory/` directory and template files will be copied to your project.

## What Gets Installed

- **`.factory/`** - Complete Factory AI integration with 21 specialized droids
- **`AGENTS.md.template`** - Project configuration template
- **`DSM_README.md`** - Droidpowers-specific documentation

## Options

```bash
npx droidpowers --force    # Overwrite existing .factory directory
npx droidpowers --help     # Show help
npx droidpowers --version  # Show version
```

## Next Steps

1. Copy `AGENTS.md.template` to `AGENTS.md` and customize for your project
2. Start any task with `/droid using-droids`
3. Use `/droid skill-checker` for automatic droid routing

## Available Droids

- **test-driven-development** - Strict TDD workflow
- **systematic-debugging** - Four-phase bug investigation
- **brainstorming** - Collaborative design refinement
- **verification-before-completion** - Pre-commit validation
- And 17 more specialized workflows

## Requirements

- Node.js >= 14.0.0
- Works with any project (package.json or git repo recommended)

## Learn More

See [DSM_README.md](DSM_README.md) after installation for complete usage guide.