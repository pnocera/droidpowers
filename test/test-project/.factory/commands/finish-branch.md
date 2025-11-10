# Finish Development Branch Command

Guides completion of development work by presenting structured options for merge, PR, or cleanup when implementation is complete and all tests pass.

## Usage
`/finish-branch [integration-option]` or `/finish-branch`

## Process
1. Analyzes current branch status and implementation completeness
2. Verifies all tests are passing and code meets quality standards  
3. Presents integration options: PR, direct merge, or cleanup
4. Guides through selected integration path
5. Ensures proper documentation and workspace cleanup

$ARGUMENTS

**Integration Options:**
- **pr**: Create comprehensive pull request with review
- **merge**: Direct merge to main branch (simple changes)
- **cleanup**: Feature branch cleanup and archival

**Getting Started:**
1. Ensure implementation is complete
2. Verify all tests are passing
3. Run this command for integration guidance
4. Follow presented options for next steps

**Prerequisites:**
- Implementation complete
- All tests passing
- Code meets quality standards
- Ready for integration or cleanup

**Integration with:**
- verification-before-completion (pre-completion validation)
- requesting-code-review (for PR creation and review)