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

// Export test function for use in test runner
module.exports = { testInstall };

// Run test if this file is executed directly
if (require.main === module) {
  testInstall().catch(console.error);
}