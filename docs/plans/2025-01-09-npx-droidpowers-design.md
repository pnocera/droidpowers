# Droidpowers npm Package Design

## Overview
Implement `npx droidpowers` command to install Droidpowers Factory AI skills system in any project with simple file copying operations.

## Architecture
- **Package Name**: `droidpowers`
- **Entry Point**: `bin/droidpowers` executable
- **Core Logic**: `src/installer.js` and `src/file-operations.js`
- **Templates**: `templates/` directory with distributable files

## CLI Interface
```bash
npx droidpowers [--force]
```

## File Copying Rules
- `.factory/` - Always copy, delete existing if `--force`, error if exists without `--force`
- `AGENTS.md.template` - Copy only if doesn't exist
- `DSM_README.md` - Copy only if doesn't exist

## Implementation Details
- **Dependencies**: Node.js built-in modules only
- **Node Version**: >=14.0.0
- **Error Handling**: Graceful with clear messages and exit codes
- **Validation**: Check target directory is a valid project

## Exit Codes
- 0 - Success
- 1 - General error
- 2 - Permission issues
- 3 - Invalid target directory

## Package Structure
```
droidpowers-package/
├── bin/droidpowers          # Executable CLI entry point
├── src/installer.js         # Core installation logic
├── src/file-operations.js   # File system utilities
├── templates/               # Files to copy to user projects
│   ├── .factory/           # Complete .factory directory
│   ├── AGENTS.md.template  # Agents template
│   └── DSM_README.md       # Droidpowers-specific README
├── package.json
└── README.md
```

## Next Steps
Ready to set up for implementation using isolated git worktree.