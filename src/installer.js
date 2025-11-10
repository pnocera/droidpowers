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