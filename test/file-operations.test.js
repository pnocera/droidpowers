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

// Export test function for use in test runner
module.exports = { testCopyFile };

// Run test if this file is executed directly
if (require.main === module) {
  testCopyFile().catch(console.error);
}