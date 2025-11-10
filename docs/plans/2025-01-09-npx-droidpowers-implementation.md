# Npx Droidpowers Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create npm package that installs Droidpowers Factory AI skills system in any project with `npx droidpowers` command

**Architecture:** Simple Node.js CLI with minimal dependencies that copies templates from package to user project directory

**Tech Stack:** Node.js (>=14), built-in fs/promises, process.argv for CLI parsing

---

### Task 1: Create package.json configuration

**Files:**
- Create: `package.json`

**Step 1: Create package.json with complete configuration**

```json
{
  "name": "droidpowers",
  "version": "1.0.0",
  "description": "Install Droidpowers Factory AI skills system in any project",
  "main": "src/installer.js",
  "bin": {
    "droidpowers": "bin/droidpowers"
  },
  "scripts": {
    "test": "node test/test.js",
    "prepublishOnly": "node test/test.js"
  },
  "keywords": [
    "ai",
    "claude",
    "factory",
    "skills",
    "development",
    "cli"
  ],
  "author": "Droidpowers",
  "license": "MIT",
  "engines": {
    "node": ">=14.0.0"
  },
  "files": [
    "bin/",
    "src/",
    "templates/"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/your-org/droidpowers.git"
  }
}
```

**Step 2: Commit**

```bash
git add package.json
git commit -m "feat: add package.json configuration for droidpowers CLI"
```

---

### Task 2: Create file operations utilities

**Files:**
- Create: `src/file-operations.js`

**Step 1: Write failing test for file operations**

```javascript
// test/file-operations.test.js
const { copyDirectory, copyFile, fileExists, directoryExists } = require('../src/file-operations');
const fs = require('fs');
const path = require('path');

async function testCopyFile() {
  const src = path.join(__dirname, 'fixtures', 'test.txt');
  const dest = path.join(__dirname, 'output', 'test.txt');

  // Ensure destination doesn't exist
  if (fs.existsSync(dest)) fs.unlinkSync(dest);

  await copyFile(src, dest);

  if (!fs.existsSync(dest)) {
    throw new Error('File was not copied');
  }

  const srcContent = fs.readFileSync(src, 'utf8');
  const destContent = fs.readFileSync(dest, 'utf8');

  if (srcContent !== destContent) {
    throw new Error('File content does not match');
  }
}

testCopyFile().catch(console.error);
```

**Step 2: Create test fixtures**

```bash
mkdir -p test/fixtures test/output
echo "test content" > test/fixtures/test.txt
```

**Step 3: Run test to verify it fails**

```bash
node test/file-operations.test.js
```
Expected: Error "Cannot find module '../src/file-operations'"

**Step 4: Implement file-operations.js**

```javascript
// src/file-operations.js
const fs = require('fs').promises;
const path = require('path');

async function copyDirectory(src, dest, options = {}) {
  const { force = false, skipExisting = true } = options;

  try {
    // Check if destination exists
    if (await directoryExists(dest) && !force) {
      throw new Error(`Directory ${dest} already exists. Use --force to overwrite.`);
    }

    // Remove destination if force is true
    if (await directoryExists(dest) && force) {
      await fs.rmdir(dest, { recursive: true });
    }

    // Create destination directory
    await fs.mkdir(dest, { recursive: true });

    // Copy all files and subdirectories
    const entries = await fs.readdir(src, { withFileTypes: true });

    for (const entry of entries) {
      const srcPath = path.join(src, entry.name);
      const destPath = path.join(dest, entry.name);

      if (entry.isDirectory()) {
        await copyDirectory(srcPath, destPath, options);
      } else {
        await copyFile(srcPath, destPath, { skipExisting });
      }
    }
  } catch (error) {
    throw new Error(`Failed to copy directory ${src} to ${dest}: ${error.message}`);
  }
}

async function copyFile(src, dest, options = {}) {
  const { skipExisting = true } = options;

  try {
    // Check if destination exists and should be skipped
    if (await fileExists(dest) && skipExisting) {
      return; // Skip existing files
    }

    // Ensure destination directory exists
    const destDir = path.dirname(dest);
    await fs.mkdir(destDir, { recursive: true });

    // Copy the file
    await fs.copyFile(src, dest);
  } catch (error) {
    throw new Error(`Failed to copy file ${src} to ${dest}: ${error.message}`);
  }
}

async function fileExists(filePath) {
  try {
    const stat = await fs.stat(filePath);
    return stat.isFile();
  } catch {
    return false;
  }
}

async function directoryExists(dirPath) {
  try {
    const stat = await fs.stat(dirPath);
    return stat.isDirectory();
  } catch {
    return false;
  }
}

module.exports = {
  copyDirectory,
  copyFile,
  fileExists,
  directoryExists
};
```

**Step 5: Run test to verify it passes**

```bash
node test/file-operations.test.js
```
Expected: No errors

**Step 6: Commit**

```bash
git add src/file-operations.js test/file-operations.test.js test/fixtures/test.txt
git commit -m "feat: implement file operations utilities with tests"
```

---

### Task 3: Create installer core logic

**Files:**
- Create: `src/installer.js`

**Step 1: Write failing test for installer**

```javascript
// test/installer.test.js
const { installDroidpowers } = require('../src/installer');
const fs = require('fs');
const path = require('path');

async function testInstall() {
  const testDir = path.join(__dirname, 'test-project');
  const templatesDir = path.join(__dirname, '..', 'templates');

  // Clean up test directory
  if (fs.existsSync(testDir)) {
    fs.rmSync(testDir, { recursive: true });
  }
  fs.mkdirSync(testDir);

  // Ensure templates directory has required files
  if (!fs.existsSync(templatesDir)) {
    fs.mkdirSync(templatesDir, { recursive: true });
    fs.mkdirSync(path.join(templatesDir, '.factory'), { recursive: true });
    fs.writeFileSync(path.join(templatesDir, '.factory', 'test.txt'), 'test');
    fs.writeFileSync(path.join(templatesDir, 'AGENTS.md.template'), '# Agents');
    fs.writeFileSync(path.join(templatesDir, 'DSM_README.md'), '# Droidpowers README');
  }

  await installDroidpowers(testDir, { force: false });

  // Verify files were copied
  if (!fs.existsSync(path.join(testDir, '.factory'))) {
    throw new Error('.factory directory was not created');
  }

  if (!fs.existsSync(path.join(testDir, 'AGENTS.md.template'))) {
    throw new Error('AGENTS.md.template was not copied');
  }

  if (!fs.existsSync(path.join(testDir, 'DSM_README.md'))) {
    throw new Error('DSM_README.md was not copied');
  }
}

testInstall().catch(console.error);
```

**Step 2: Run test to verify it fails**

```bash
node test/installer.test.js
```
Expected: Error "Cannot find module '../src/installer'"

**Step 3: Implement installer.js**

```javascript
// src/installer.js
const path = require('path');
const { copyDirectory, copyFile, directoryExists, fileExists } = require('./file-operations');

async function installDroidpowers(targetDir = process.cwd(), options = {}) {
  const { force = false } = options;

  try {
    // Validate target directory
    await validateTargetDirectory(targetDir);

    // Get templates directory (relative to this file)
    const templatesDir = path.join(__dirname, '..', 'templates');

    // Check if templates directory exists
    if (!(await directoryExists(templatesDir))) {
      throw new Error(`Templates directory not found: ${templatesDir}`);
    }

    // Install .factory directory
    const factorySrc = path.join(templatesDir, '.factory');
    const factoryDest = path.join(targetDir, '.factory');

    if (await directoryExists(factorySrc)) {
      await copyDirectory(factorySrc, factoryDest, { force, skipExisting: false });
    } else {
      throw new Error('.factory template not found');
    }

    // Install AGENTS.md.template
    const agentsTemplateSrc = path.join(templatesDir, 'AGENTS.md.template');
    const agentsTemplateDest = path.join(targetDir, 'AGENTS.md.template');

    if (await fileExists(agentsTemplateSrc)) {
      await copyFile(agentsTemplateSrc, agentsTemplateDest, { skipExisting: true });
    }

    // Install DSM_README.md
    const readmeSrc = path.join(templatesDir, 'DSM_README.md');
    const readmeDest = path.join(targetDir, 'DSM_README.md');

    if (await fileExists(readmeSrc)) {
      await copyFile(readmeSrc, readmeDest, { skipExisting: true });
    }

    console.log('✅ Droidpowers installed successfully!');
    console.log('📁 .factory/ directory added');
    console.log('📄 AGENTS.md.template added');
    console.log('📄 DSM_README.md added');
    console.log('');
    console.log('Next steps:');
    console.log('1. Copy AGENTS.md.template to AGENTS.md and customize');
    console.log('2. Start with /droid using-droids for any task');

  } catch (error) {
    console.error(`❌ Installation failed: ${error.message}`);
    process.exit(1);
  }
}

async function validateTargetDirectory(dir) {
  // Check if directory exists
  try {
    const stat = await require('fs').promises.stat(dir);
    if (!stat.isDirectory()) {
      throw new Error('Target is not a directory');
    }
  } catch {
    throw new Error('Target directory does not exist');
  }

  // Basic validation that this looks like a project
  // At least one of: package.json, .git, or any source code file
  const { fileExists, directoryExists } = require('./file-operations');

  const hasPackageJson = await fileExists(path.join(dir, 'package.json'));
  const hasGit = await directoryExists(path.join(dir, '.git'));

  if (!hasPackageJson && !hasGit) {
    console.warn('⚠️  Warning: This does not appear to be a project directory');
    console.warn('   Consider running this in a directory with package.json or .git');
  }
}

module.exports = { installDroidpowers };
```

**Step 4: Run test to verify it passes**

```bash
node test/installer.test.js
```
Expected: Success message and no errors

**Step 5: Commit**

```bash
git add src/installer.js test/installer.test.js
git commit -m "feat: implement installer core logic with tests"
```

---

### Task 4: Create executable CLI script

**Files:**
- Create: `bin/droidpowers`

**Step 1: Create executable script**

```bash
#!/usr/bin/env node

const path = require('path');
const { installDroidpowers } = require('../src/installer');

function parseArguments() {
  const args = process.argv.slice(2);
  const options = { force: false };

  if (args.includes('--force') || args.includes('-f')) {
    options.force = true;
  }

  if (args.includes('--help') || args.includes('-h')) {
    showHelp();
    process.exit(0);
  }

  if (args.includes('--version') || args.includes('-v')) {
    showVersion();
    process.exit(0);
  }

  return options;
}

function showHelp() {
  console.log(`
Usage: npx droidpowers [options]

Options:
  --force, -f    Force overwrite existing .factory directory
  --help, -h     Show this help message
  --version, -v  Show version number

Description:
  Install Droidpowers Factory AI skills system in the current project.
  Copies .factory/ directory and template files to enable AI-powered development workflows.
  `);
}

function showVersion() {
  const packageJson = require('../package.json');
  console.log(`droidpowers v${packageJson.version}`);
}

async function main() {
  try {
    const options = parseArguments();

    if (options.force) {
      console.log('🔄 Force mode enabled - will overwrite existing .factory directory');
    }

    await installDroidpowers(process.cwd(), options);

  } catch (error) {
    console.error(`❌ Fatal error: ${error.message}`);
    process.exit(1);
  }
}

// Handle unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('❌ Unhandled Rejection at:', promise, 'reason:', reason);
  process.exit(1);
});

main();
```

**Step 2: Make script executable**

```bash
chmod +x bin/droidpowers
```

**Step 3: Test CLI help and version**

```bash
node bin/droidpowers --help
node bin/droidpowers --version
```
Expected: Help text and version information displayed

**Step 4: Commit**

```bash
git add bin/droidpowers
git commit -m "feat: add executable CLI script with help and version"
```

---

### Task 5: Set up templates directory

**Files:**
- Create: `templates/.factory/` (copy from current project)
- Create: `templates/AGENTS.md.template` (copy from current project)
- Create: `templates/DSM_README.md`

**Step 1: Copy .factory directory**

```bash
mkdir -p templates
cp -r .factory templates/
```

**Step 2: Copy AGENTS.md.template**

```bash
cp AGENTS.md.template templates/
```

**Step 3: Create DSM_README.md**

```markdown
# Droidpowers Factory AI Integration

This project is equipped with Droidpowers - a complete Factory AI skills system with 21 specialized droids for enhanced development workflows.

## Quick Start

1. **Configure your project**: Copy `AGENTS.md.template` to `AGENTS.md` and customize for your project type
2. **Start any task**: Run `/droid using-droids` before beginning any work
3. **Follow routing**: Use `/droid skill-checker` to automatically route to the right droid

## Essential Commands

- `/droid using-droids` - **MANDATORY** first step for all task analysis
- `/droid test-driven-development` or `/tdd` - Strict TDD workflow
- `/droid systematic-debugging` or `/debug` - Four-phase bug investigation
- `/droid brainstorming` or `/brainstorm` - Design refinement
- `/droid verification-before-completion` or `/verify` - Pre-commit validation

## Configuration

Edit `AGENTS.md` to customize:
- Project type and language specifics
- Build/test/lint commands
- Directory structure
- Team conventions
- Mandatory vs recommended droids

## Learn More

Run `/droid droids` to see all available droids and their capabilities.

## Documentation

For complete documentation, see the original Droidpowers repository.
```

**Step 4: Verify templates structure**

```bash
ls -la templates/
ls -la templates/.factory/
```
Expected: All required template files present

**Step 5: Commit**

```bash
git add templates/
git commit -m "feat: add templates directory with droidpowers files"
```

---

### Task 6: Create comprehensive test suite

**Files:**
- Create: `test/integration.test.js`
- Create: `test/cli.test.js`

**Step 1: Create integration test**

```javascript
// test/integration.test.js
const { installDroidpowers } = require('../src/installer');
const fs = require('fs');
const path = require('path');

async function testFullIntegration() {
  console.log('🧪 Running full integration test...');

  const testProjectDir = path.join(__dirname, 'integration-test-project');

  // Clean up any existing test directory
  if (fs.existsSync(testProjectDir)) {
    fs.rmSync(testProjectDir, { recursive: true });
  }

  // Create test project directory
  fs.mkdirSync(testProjectDir);

  // Create a mock package.json to make it look like a real project
  fs.writeFileSync(
    path.join(testProjectDir, 'package.json'),
    JSON.stringify({ name: 'test-project', version: '1.0.0' })
  );

  try {
    // Test installation
    await installDroidpowers(testProjectDir, { force: false });

    // Verify all expected files exist
    const expectedFiles = [
      '.factory',
      'AGENTS.md.template',
      'DSM_README.md'
    ];

    for (const file of expectedFiles) {
      const filePath = path.join(testProjectDir, file);
      if (!fs.existsSync(filePath)) {
        throw new Error(`Expected file not found: ${file}`);
      }
      console.log(`✅ Found: ${file}`);
    }

    // Test that .factory contains expected content
    const factoryFiles = fs.readdirSync(path.join(testProjectDir, '.factory'));
    if (factoryFiles.length === 0) {
      throw new Error('.factory directory is empty');
    }
    console.log(`✅ .factory contains ${factoryFiles.length} files/directories`);

    // Test --force behavior
    console.log('🧪 Testing force reinstall...');
    await installDroidpowers(testProjectDir, { force: true });
    console.log('✅ Force reinstall successful');

    console.log('🎉 All integration tests passed!');

  } finally {
    // Clean up
    if (fs.existsSync(testProjectDir)) {
      fs.rmSync(testProjectDir, { recursive: true });
    }
  }
}

testFullIntegration().catch(error => {
  console.error('❌ Integration test failed:', error.message);
  process.exit(1);
});
```

**Step 2: Create CLI test**

```javascript
// test/cli.test.js
const { spawn } = require('child_process');
const path = require('path');

async function testCLI() {
  console.log('🧪 Testing CLI interface...');

  const cliScript = path.join(__dirname, '..', 'bin', 'droidpowers');

  // Test help
  console.log('Testing --help...');
  const helpResult = await runCLI(cliScript, ['--help']);
  if (!helpResult.includes('Usage:')) {
    throw new Error('Help output not correct');
  }
  console.log('✅ Help command works');

  // Test version
  console.log('Testing --version...');
  const versionResult = await runCLI(cliScript, ['--version']);
  if (!versionResult.includes('droidpowers v')) {
    throw new Error('Version output not correct');
  }
  console.log('✅ Version command works');

  console.log('🎉 All CLI tests passed!');
}

function runCLI(script, args) {
  return new Promise((resolve, reject) => {
    const child = spawn('node', [script, ...args], {
      stdio: 'pipe',
      cwd: path.join(__dirname, 'cli-test-project')
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    child.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    child.on('close', (code) => {
      if (code !== 0 && !args.includes('--help') && !args.includes('--version')) {
        reject(new Error(`CLI exited with code ${code}: ${stderr}`));
      } else {
        resolve(stdout);
      }
    });

    child.on('error', reject);
  });
}

testCLI().catch(error => {
  console.error('❌ CLI test failed:', error.message);
  process.exit(1);
});
```

**Step 3: Run all tests**

```bash
npm test
```
Expected: All tests pass

**Step 4: Commit**

```bash
git add test/integration.test.js test/cli.test.js
git commit -m "feat: add comprehensive test suite"
```

---

### Task 7: Create package README

**Files:**
- Create: `README.md`

**Step 1: Create README.md**

```markdown
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
```

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add comprehensive README for npm package"
```

---

### Task 8: Final validation and preparation

**Files:**
- Modify: `package.json` (add test script if missing)

**Step 1: Run final test suite**

```bash
npm test
```

**Step 2: Test CLI in temporary directory**

```bash
mkdir /tmp/test-droidpowers
cd /tmp/test-droidpowers
echo '{"name":"test"}' > package.json
node /mnt/e/Projects/obra/droidpowers/bin/droidpowers
ls -la
```
Expected: Installation succeeds and files are created

**Step 3: Validate package structure**

```bash
npm pack --dry-run
```
Expected: Shows all necessary files included

**Step 4: Final commit**

```bash
git add .
git commit -m "feat: complete npx droidpowers CLI implementation"
```

---

## Implementation Complete

The npx droidpowers CLI is now ready for npm publishing and distribution.