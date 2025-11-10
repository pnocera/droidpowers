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

    // Copy the file using read/write approach (more compatible)
    const content = await fs.readFile(src);
    await fs.writeFile(dest, content);
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