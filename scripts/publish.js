#!/usr/bin/env node

/**
 * Droidpowers NPM Publishing Script
 * 
 * This script handles the complete npm publishing workflow including:
 * - Version validation and bumping
 * - Build verification
 * - Test execution
 * - Package publishing
 * - Git tagging
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration
const CONFIG = {
  packageName: 'droidpowers',
  mainBranch: 'main',
  testScript: 'npm test',
  buildScript: null, // Add if you have a build step
  filesToCheck: [
    'package.json',
    'README.md',
    'bin/droidpowers',
    'src/installer.js'
  ],
  requiredDirectories: [
    'bin',
    'src',
    'templates'
  ]
};

// Colors for terminal output
const colors = {
  reset: '\x1b[0m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function logStep(step) {
  log(`\n📋 ${step}`, 'cyan');
}

function logSuccess(message) {
  log(`✅ ${message}`, 'green');
}

function logError(message) {
  log(`❌ ${message}`, 'red');
}

function logWarning(message) {
  log(`⚠️  ${message}`, 'yellow');
}

function execCommand(command, options = {}) {
  try {
    const result = execSync(command, { 
      encoding: 'utf8', 
      stdio: options.silent ? 'pipe' : 'inherit',
      ...options 
    });
    return result;
  } catch (error) {
    if (!options.silent) {
      logError(`Command failed: ${command}`);
      logError(error.message);
    }
    throw error;
  }
}

function checkPrerequisites() {
  logStep('Checking prerequisites');
  
  // Check if npm is authenticated
  try {
    const whoami = execCommand('npm whoami', { silent: true }).trim();
    logSuccess(`Authenticated as: ${whoami}`);
  } catch (error) {
    logError('Not authenticated with npm. Run: npm login');
    process.exit(1);
  }
  
  // Check if we're on the main branch
  try {
    const currentBranch = execCommand('git rev-parse --abbrev-ref HEAD', { silent: true }).trim();
    if (currentBranch !== CONFIG.mainBranch) {
      logWarning(`Not on main branch (currently on ${currentBranch})`);
      const answer = require('readline-sync').question('Continue anyway? (y/N): ');
      if (answer.toLowerCase() !== 'y') {
        process.exit(1);
      }
    } else {
      logSuccess(`On correct branch: ${currentBranch}`);
    }
  } catch (error) {
    logError('Could not determine current branch');
    process.exit(1);
  }
  
  // Check if working directory is clean
  try {
    const status = execCommand('git status --porcelain', { silent: true }).trim();
    if (status) {
      logError('Working directory is not clean. Commit or stash changes first.');
      logError('Uncommitted changes:');
      console.log(status);
      process.exit(1);
    } else {
      logSuccess('Working directory is clean');
    }
  } catch (error) {
    logError('Could not check git status');
    process.exit(1);
  }
}

function validateFiles() {
  logStep('Validating required files');
  
  // Check required files
  CONFIG.filesToCheck.forEach(file => {
    if (fs.existsSync(file)) {
      logSuccess(`Found: ${file}`);
    } else {
      logError(`Missing required file: ${file}`);
      process.exit(1);
    }
  });
  
  // Check required directories
  CONFIG.requiredDirectories.forEach(dir => {
    if (fs.existsSync(dir) && fs.statSync(dir).isDirectory()) {
      logSuccess(`Found directory: ${dir}`);
    } else {
      logError(`Missing required directory: ${dir}`);
      process.exit(1);
    }
  });
  
  // Validate package.json
  try {
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    if (!packageJson.version) {
      logError('No version specified in package.json');
      process.exit(1);
    }
    if (!packageJson.name) {
      logError('No name specified in package.json');
      process.exit(1);
    }
    logSuccess(`Package: ${packageJson.name}@${packageJson.version}`);
  } catch (error) {
    logError('Invalid package.json');
    process.exit(1);
  }
}

function runTests() {
  logStep('Running tests');
  
  try {
    execCommand(CONFIG.testScript);
    logSuccess('All tests passed');
  } catch (error) {
    logError('Tests failed');
    process.exit(1);
  }
}

function buildProject() {
  if (CONFIG.buildScript) {
    logStep('Building project');
    try {
      execCommand(CONFIG.buildScript);
      logSuccess('Build completed');
    } catch (error) {
      logError('Build failed');
      process.exit(1);
    }
  }
}

function checkVersion() {
  logStep('Checking version');
  
  try {
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    const currentVersion = packageJson.version;
    
    // Check if version already exists on npm
    try {
      execCommand(`npm view ${CONFIG.packageName}@${currentVersion} version`, { silent: true });
      logWarning(`Version ${currentVersion} already exists on npm`);
      const answer = require('readline-sync').question('Bump version? (Y/n): ');
      if (answer.toLowerCase() !== 'n') {
        bumpVersion();
      }
    } catch (error) {
      // Version doesn't exist, which is good
      logSuccess(`Version ${currentVersion} is new`);
    }
  } catch (error) {
    logError('Could not check version');
    process.exit(1);
  }
}

function bumpVersion() {
  logStep('Bumping version');
  
  const readlineSync = require('readline-sync');
  const choices = ['patch', 'minor', 'major', 'prerelease'];
  const index = readlineSync.keyInSelect(choices, 'Choose version bump type:');
  
  if (index === -1) {
    logError('Version bump cancelled');
    process.exit(1);
  }
  
  const bumpType = choices[index];
  
  try {
    execCommand(`npm version ${bumpType}`);
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    logSuccess(`Version bumped to ${packageJson.version}`);
  } catch (error) {
    logError('Failed to bump version');
    process.exit(1);
  }
}

function publishToNpm() {
  logStep('Publishing to npm');
  
  try {
    // Check if we're publishing with --tag=next for prereleases
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    const isPrerelease = packageJson.version.includes('-');
    
    const publishCommand = isPrerelease 
      ? `npm publish --tag next`
      : 'npm publish';
    
    log(`Running: ${publishCommand}`, 'blue');
    execCommand(publishCommand);
    
    logSuccess(`Published ${CONFIG.packageName}@${packageJson.version} to npm`);
  } catch (error) {
    logError('Failed to publish to npm');
    process.exit(1);
  }
}

function createGitTag() {
  logStep('Creating git tag');
  
  try {
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    const version = packageJson.version;
    const tagName = `v${version}`;
    
    // Create and push tag
    execCommand(`git tag ${tagName}`);
    execCommand(`git push origin ${tagName}`);
    
    logSuccess(`Created and pushed tag: ${tagName}`);
  } catch (error) {
    logWarning('Failed to create git tag (you may need to create it manually)');
  }
}

function showPostPublishInfo() {
  const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
  const version = packageJson.version;
  
  log('\n🎉 Publish successful!', 'green');
  log('\nPost-publish information:', 'cyan');
  log(`Package: ${CONFIG.packageName}@${version}`);
  log(`Install: npm install ${CONFIG.packageName}`);
  log(`Global: npm install -g ${CONFIG.packageName}`);
  log(`npm page: https://www.npmjs.com/package/${CONFIG.packageName}`);
  
  if (version.includes('-')) {
    log(`\nTo install this prerelease: npm install ${CONFIG.packageName}@next`, 'yellow');
  }
}

function main() {
  log('🚀 Droidpowers NPM Publishing Script', 'magenta');
  log('=====================================', 'magenta');
  
  try {
    checkPrerequisites();
    validateFiles();
    runTests();
    buildProject();
    checkVersion();
    publishToNpm();
    createGitTag();
    showPostPublishInfo();
  } catch (error) {
    logError(`Publishing failed: ${error.message}`);
    process.exit(1);
  }
}

// Handle command line arguments
const args = process.argv.slice(2);

if (args.includes('--help') || args.includes('-h')) {
  console.log(`
Usage: node scripts/publish.js [options]

Options:
  --help, -h     Show this help message
  --skip-tests   Skip running tests
  --skip-build   Skip build step
  --dry-run      Run through all checks without actually publishing

Examples:
  node scripts/publish.js              # Full publish workflow
  node scripts/publish.js --dry-run    # Dry run without publishing
`);
  process.exit(0);
}

if (args.includes('--dry-run')) {
  log('🔍 DRY RUN MODE - No actual publishing will occur', 'yellow');
  // Override publish and tag functions to simulate the process
  publishToNpm = () => {
    logStep('[DRY RUN] Would publish to npm');
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    logSuccess(`[DRY RUN] Would publish ${CONFIG.packageName}@${packageJson.version}`);
  };
  createGitTag = () => {
    logStep('[DRY RUN] Would create git tag');
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    logSuccess(`[DRY RUN] Would create tag v${packageJson.version}`);
  };
}

if (args.includes('--skip-tests')) {
  runTests = () => {
    logStep('Skipping tests');
    logWarning('Tests skipped by request');
  };
}

if (args.includes('--skip-build')) {
  buildProject = () => {
    logStep('Skipping build');
    logWarning('Build skipped by request');
  };
}

// Check if readline-sync is available
try {
  require('readline-sync');
} catch (error) {
  logError('readline-sync is required for interactive prompts');
  logError('Install it with: npm install readline-sync');
  process.exit(1);
}

main();