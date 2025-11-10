// test/test.js - Main test runner
const path = require('path');
const fs = require('fs');

// Import test functions
const { testCopyFile } = require('./file-operations.test.js');
const { testInstall } = require('./installer.test.js');

async function runTests() {
  console.log('🚀 Running Droidpowers Test Suite...\n');
  
  let passed = 0;
  let failed = 0;
  
  const tests = [
    {
      name: 'File Operations Tests',
      test: async () => {
        console.log('📁 Running file operations tests...');
        await testCopyFile();
        console.log('✅ File operations tests passed\n');
      }
    },
    {
      name: 'Installer Tests', 
      test: async () => {
        console.log('📦 Running installer tests...');
        await testInstall();
        console.log('✅ Installer tests passed\n');
      }
    }
  ];
  
  for (const { name, test } of tests) {
    try {
      await test();
      passed++;
    } catch (error) {
      console.error(`❌ ${name} failed:`, error.message);
      failed++;
    }
  }
  
  console.log('\n📊 Test Results:');
  console.log(`✅ Passed: ${passed}`);
  console.log(`❌ Failed: ${failed}`);
  console.log(`📈 Total: ${passed + failed}`);
  
  if (failed > 0) {
    console.log('\n💥 Some tests failed!');
    process.exit(1);
  } else {
    console.log('\n🎉 All tests passed!');
    process.exit(0);
  }
}

// Run tests if this file is executed directly
if (require.main === module) {
  runTests().catch(error => {
    console.error('💥 Test runner failed:', error);
    process.exit(1);
  });
}

module.exports = { runTests };