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
    // Use the script directly since it's executable
    const child = spawn(script, args, {
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

// Run test if this file is executed directly
if (require.main === module) {
  testCLI().catch(error => {
    console.error('❌ CLI test failed:', error.message);
    process.exit(1);
  });
}

module.exports = { testCLI };