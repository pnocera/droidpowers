#!/usr/bin/env node

/**
 * Quick NPM Publish Script
 * Simplified version for fast publishing when you're confident everything is ready
 */

const { execSync } = require('child_process');
const fs = require('fs');

const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  cyan: '\x1b[36m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function logSuccess(message) {
  log(`✅ ${message}`, 'green');
}

function logError(message) {
  log(`❌ ${message}`, 'red');
}

function execCommand(command) {
  try {
    execSync(command, { stdio: 'inherit' });
  } catch (error) {
    logError(`Failed: ${command}`);
    process.exit(1);
  }
}

function main() {
  log('🚀 Quick Publish to NPM', 'cyan');
  
  // Quick checks
  try {
    // Check if git is clean
    const status = execSync('git status --porcelain', { encoding: 'utf8' }).trim();
    if (status) {
      logError('Working directory is not clean');
      process.exit(1);
    }
    
    // Run tests
    log('Running tests...');
    execCommand('npm test');
    
    // Publish
    log('Publishing to npm...');
    execCommand('npm publish');
    
    // Create git tag
    const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    const version = packageJson.version;
    const tag = `v${version}`;
    
    log(`Creating git tag: ${tag}`);
    execCommand(`git tag ${tag}`);
    execCommand(`git push origin ${tag}`);
    
    logSuccess(`Published ${packageJson.name}@${version} successfully!`);
    
  } catch (error) {
    logError('Quick publish failed');
    process.exit(1);
  }
}

if (process.argv.includes('--help')) {
  console.log(`
Quick NPM Publish Script

Usage: node scripts/quick-publish.js

This script:
1. Checks git status is clean
2. Runs tests
3. Publishes to npm
4. Creates and pushes git tag

For more control, use: node scripts/publish.js
`);
  process.exit(0);
}

main();