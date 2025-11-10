# Publishing Droidpowers to NPM

This guide covers how to publish the droidpowers package to npm.

## Prerequisites

1. **NPM Account**: You must have an npm account
2. **Package Access**: You must be added as a maintainer of the `droidpowers` package
3. **Authentication**: Run `npm login` to authenticate

```bash
npm login
```

## Quick Start

### Option 1: Using Make (Recommended)

```bash
# Quick publish (when confident everything is ready)
make publish-quick

# Full workflow with all validations
make publish

# Dry run to test without publishing
make publish-dry-run
```

### Option 2: Using npm scripts

```bash
# Quick publish
npm run publish:quick

# Full workflow
npm run publish

# Dry run
npm run publish:dry-run
```

### Option 3: Direct script execution

```bash
# Full publishing workflow
node scripts/publish.js

# Quick publish
node scripts/quick-publish.js

# Dry run
node scripts/publish.js --dry-run
```

## Publishing Workflows

### Quick Publish (`publish:quick`)

Fastest option when you're confident everything is ready:

1. ✅ Check git status is clean
2. ✅ Run tests
3. ✅ Publish to npm
4. ✅ Create and push git tag

```bash
npm run publish:quick
# or
make publish-quick
```

### Full Publish (`publish`)

Comprehensive workflow with all validations:

1. ✅ Check npm authentication
2. ✅ Verify correct git branch
3. ✅ Check working directory is clean
4. ✅ Validate required files and directories
5. ✅ Run tests
6. ✅ Check if version already exists on npm
7. ✅ Optionally bump version
8. ✅ Publish to npm
9. ✅ Create and push git tag
10. ✅ Show post-publish information

```bash
npm run publish
# or
make publish
```

## Version Management

### Automatic Version Bumping

The full publish script can automatically bump versions:

```bash
node scripts/publish.js
# Follow prompts to choose: patch, minor, major, or prerelease
```

### Manual Version Bumping with Publish

```bash
# Patch version (1.0.0 → 1.0.1)
make publish-patch
# or
npm version patch && npm run publish:quick

# Minor version (1.0.0 → 1.1.0)
make publish-minor
# or
npm version minor && npm run publish:quick

# Major version (1.0.0 → 2.0.0)
make publish-major
# or
npm version major && npm run publish:quick
```

### Prerelease Versions

For beta/alpha versions:

```bash
# Create prerelease
npm version prerelease
npm run publish:quick

# This will publish with --tag=next
# Users can install with: npm install droidpowers@next
```

## Dry Run Testing

Always test with dry run first:

```bash
make publish-dry-run
# or
npm run publish:dry-run
```

This runs through all checks without actually publishing.

## What Gets Published

The `package.json` `files` field controls what gets included:

```json
"files": [
  "bin/",
  "src/",
  "templates/"
]
```

Only these directories and files are included in the npm package.

## Pre-publish Checks

The publish scripts automatically run:

- **Tests**: `npm test` must pass
- **Git Status**: Working directory must be clean
- **Branch Check**: Should be on main branch (with override option)
- **File Validation**: Required files must exist
- **Version Check**: Prevents publishing existing versions

## Post-Publish Actions

After successful publishing:

1. **Git Tag**: Automatically created and pushed (e.g., `v1.0.0`)
2. **npm Registry**: Package is available immediately
3. **Documentation**: Update any documentation if needed

## Troubleshooting

### Common Issues

**"Not authenticated with npm"**
```bash
npm login
```

**"Working directory is not clean"**
```bash
git status
git add .
git commit -m "Prepare for publish"
```

**"Version already exists"**
```bash
npm version patch  # or minor/major
```

**"Tests failed"**
```bash
npm test  # Fix failing tests first
```

**"Permission denied"**
- Ensure you're added as a maintainer of the droidpowers package
- Contact the package owner for access

### Manual Recovery

If scripts fail, you can publish manually:

```bash
# Run tests first
npm test

# Publish manually
npm publish

# Create tag manually
git tag v1.0.0  # Use your version
git push origin v1.0.0
```

## Best Practices

1. **Always test with dry run first**
2. **Keep git history clean before publishing**
3. **Use semantic versioning for version bumps**
4. **Update CHANGELOG.md with version changes**
5. **Test installation after publish**
6. **Monitor npm downloads and issues**

## Testing After Publish

Always test the published package:

```bash
# Test in a new directory
mkdir test-droidpowers
cd test-droidpowers

# Install from npm
npm install droidpowers

# Test CLI
npx droidpowers --help

# Test installation in a project
mkdir my-project
cd my-project
npx droidpowers install
```

## Rollback (If Needed)

If you need to unpublish:

```bash
# Deprecate a version (recommended)
npm deprecate droidpowers@1.0.0 "Critical bug in version 1.0.0, use 1.0.1 instead"

# Unpublish entire package (only if <24h and critical)
npm unpublish droidpowers --force
```

**Warning**: Unpublishing should be avoided unless absolutely necessary. Use deprecation instead.