# Droidpowers NPM Publishing Makefile

.PHONY: help publish publish-quick publish-dry-run test setup

# Default target
help:
	@echo "Droidpowers NPM Publishing Commands:"
	@echo ""
	@echo "  make publish       - Full publishing workflow with all checks"
	@echo "  make publish-quick - Quick publish (tests + publish + tag)"
	@echo "  make publish-dry-run- Dry run to test everything without publishing"
	@echo "  make test          - Run tests"
	@echo "  make setup         - Install dependencies for publishing"
	@echo ""
	@echo "Examples:"
	@echo "  make publish-quick    # Fast publish when confident"
	@echo "  make publish          # Full workflow with validation"
	@echo "  make publish-dry-run  # Test without actually publishing"

# Install dependencies needed for publishing
setup:
	@echo "Installing publishing dependencies..."
	npm install readline-sync
	@echo "Dependencies installed!"

# Run tests
test:
	@echo "Running tests..."
	npm test

# Full publishing workflow
publish:
	@echo "Starting full publishing workflow..."
	node scripts/publish.js

# Quick publishing
publish-quick:
	@echo "Starting quick publish..."
	node scripts/quick-publish.js

# Dry run publishing
publish-dry-run:
	@echo "Running dry-run publish..."
	node scripts/publish.js --dry-run

# Version bump and publish
publish-patch:
	@echo "Bumping patch version and publishing..."
	npm version patch
	$(MAKE) publish-quick

publish-minor:
	@echo "Bumping minor version and publishing..."
	npm version minor
	$(MAKE) publish-quick

publish-major:
	@echo "Bumping major version and publishing..."
	npm version major
	$(MAKE) publish-quick

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf node_modules/.cache
	npm cache clean --force