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

// Run test if this file is executed directly
if (require.main === module) {
  testFullIntegration().catch(error => {
    console.error('❌ Integration test failed:', error.message);
    process.exit(1);
  });
}

module.exports = { testFullIntegration };