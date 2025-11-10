---
id: testing-anti-patterns
title: Testing Anti-Patterns
description: Prevent testing mock behavior, production pollution with test-only methods, and mocking without understanding dependencies
category: advanced
type: educational
tags:
  - testing
  - anti-patterns
  - quality
  - test-design
  - mocking
  - test-maintainability
---

# Testing Anti-Patterns

## Overview

Use when writing or changing tests, adding mocks, or tempted to add test-only methods to production code - prevents testing mock behavior, production pollution with test-only methods, and mocking without understanding dependencies.

## Usage

**Run this droid when:**
- Writing new tests and want to avoid common mistakes
- Adding mocks to tests and need to verify they're appropriate
- Tempted to add test-only methods to production code
- Reviewing existing test code for quality issues
- Designing test architecture for new features
- Teaching testing best practices to team members

**This droid helps prevent:**
- Testing how mocks work instead of real behavior
- Polluting production code with test-only concerns
- Mocking dependencies without understanding them
- Creating test-specific production methods
- Fragile tests that break with implementation changes

## Process

### Phase 1: Identify Anti-Patterns
1. **Review test code** for common anti-patterns
2. **Check production code** for test-only additions
3. **Analyze mock usage** for understanding vs convenience
4. **Document findings** with specific examples

### Phase 2: Education and Prevention
1. **Explain each anti-pattern** with concrete examples
2. **Provide better alternatives** that achieve the same goals
3. **Show proper testing techniques** for each scenario
4. **Create prevention checklist** for future work

### Phase 3: Remediation
1. **Fix identified issues** following best practices
2. **Remove test-only production code**
3. **Replace mock behavior testing with real behavior testing**
4. **Verify all tests still pass** after improvements

### Phase 4: Validation
1. **Run complete test suite** to ensure no regressions
2. **Review test coverage** to ensure proper behavior testing
3. **Check production code** remains free of test-specific additions
4. **Document lessons learned** for the team

## Common Anti-Patterns

### 1. Mock Behavior Testing

**Problem:** Testing how mocks work instead of real behavior
```python
# ❌ BAD: Testing mock behavior, not real behavior
def test_user_service_mock():
    mock_repo = Mock()
    mock_repo.get_user.return_value = {"id": 1, "name": "John"}
    
    service = UserService(mock_repo)
    result = service.get_user(1)
    
    # Testing the mock, not the service logic
    assert mock_repo.get_user.called
    assert mock_repo.get_user.call_count == 1

# ✅ GOOD: Testing real behavior
def test_user_service_behavior():
    mock_repo = Mock()
    mock_repo.get_user.return_value = {"id": 1, "name": "John"}
    
    service = UserService(mock_repo)
    result = service.get_user(1)
    
    # Testing actual service behavior
    assert result["name"] == "John"
    assert service.format_user_name(result) == "John"
```

### 2. Production Code Pollution

**Problem:** Adding test-only methods to production code
```python
# ❌ BAD: Test-only method in production code
class UserService:
    def get_user(self, user_id):
        # Production logic
        return self.repository.get_user(user_id)
    
    def _set_test_data(self, user_data):
        # Test-only method - doesn't belong in production!
        self.test_data = user_data

# ✅ GOOD: Keep test concerns separate
class UserService:
    def get_user(self, user_id):
        return self.repository.get_user(user_id)

# Test uses proper dependency injection or test utilities
def test_user_service():
    # Use test builder pattern or factory
    test_data = create_test_user_data()
    # Or use proper mocking
    mock_repo = Mock()
    mock_repo.get_user.return_value = test_data
```

### 3. Mocking Without Understanding

**Problem:** Mocking dependencies you don't understand
```python
# ❌ BAD: Mocking without understanding the real dependency
def test_order_service():
    mock_payment_gateway = Mock()
    # What does process_payment actually do? What are the edge cases?
    mock_payment_gateway.process_payment.return_value = {"success": True}
    
    # This test might pass but not catch real integration issues
    
# ✅ GOOD: Understand dependency before mocking
def test_order_service():
    # First understand what the real payment gateway does
    # - It validates amounts
    # - It checks card validity
    # - It has specific error codes
    # - It has retry logic
    
    mock_payment_gateway = Mock()
    mock_payment_gateway.process_payment.return_value = {
        "success": True,
        "transaction_id": "tx_123",
        "amount": 100.00,
        "currency": "USD"
    }
    
    service = OrderService(mock_payment_gateway)
    order = Order(amount=100.00, payment_method="credit_card")
    
    result = service.process_order(order)
    
    # Test meaningful business outcomes
    assert result.success
    assert result.transaction_id is not None
    assert result.amount == 100.00
```

### 4. Test-Only Methods

**Problem:** Creating methods just for testing
```python
# ❌ BAD: Method created only for testing
class ReportGenerator:
    def generate_report(self, data):
        # Complex report generation
        pass
    
    def _get_report_data_for_testing(self):
        # Method exists only so tests can verify internal state
        return self.internal_report_data

# ✅ GOOD: Test the public interface or use proper test patterns
class ReportGenerator:
    def generate_report(self, data):
        # Complex report generation
        return report

# Test the public interface or use test doubles
def test_report_generator():
    generator = ReportGenerator()
    test_data = create_test_report_data()
    report = generator.generate_report(test_data)
    
    # Verify the observable output, not internal state
    assert report.contains_summary()
    assert report.total_matches(test_data.calculate_total())
```

## Prevention Checklist

**Before Writing Tests:**
- [ ] **Understand the requirements** - What behavior should this test verify?
- [ ] **Identify public interface** - What can I test without accessing internals?
- [ ] **Plan test structure** - What test pattern best fits this scenario?
- [ ] **Consider integration needs** - Do I need real dependencies or test doubles?

**When Adding Mocks:**
- [ ] **Understand real dependency** - What does the actual dependency do?
- [ ] **Mock behavior accurately** - Does my mock represent real behavior?
- [ ] **Test meaningful outcomes** - Am I testing business logic or mock setup?
- [ ] **Verify mock necessity** - Could I test this without a mock?

**When Tempted to Add Test-Only Code:**
- [ ] **Question the necessity** - Why do I need to test this internal state?
- [ ] **Consider alternatives** - Can I test through the public interface?
- [ ] **Use proper patterns** - Should I use a builder, factory, or test utility?
- [ ] **Separate concerns** - Can test logic live in test files only?

**During Test Review:**
- [ ] **No test-only methods in production** - All production methods have business value
- [ ] **Mocks represent real dependencies** - Mocks accurately model real behavior
- [ ] **Tests verify actual behavior** - Tests check business logic, not implementation details
- [ ] **Production code remains test-agnostic** - No testing-specific logic in production
- [ ] **No testing-specific logic in production** - Production code doesn't know about tests

## Educational Components

### Understanding Test Smells

**Overspecified Tests:**
- Testing implementation details instead of behavior
- Too many mock expectations
- Fragile tests that break with refactoring

**Test Indecision:**
- Not sure what to test
- Testing too much or too little
- Unclear test responsibilities

### Good Testing Patterns

**Behavior-Driven Testing:**
```python
# Focus on what the code should do, not how it does it
def test_user_can_login_with_valid_credentials():
    # Given: A user with valid credentials
    user = create_user(email="test@example.com", password="valid123")
    
    # When: Attempting to login
    result = auth_service.login("test@example.com", "valid123")
    
    # Then: Login succeeds and returns user data
    assert result.success
    assert result.user.email == "test@example.com"
```

**Test Data Builders:**
```python
# Create reusable test data builders instead of test-only production methods
class UserBuilder:
    def __init__(self):
        self.email = "test@example.com"
        self.name = "Test User"
        self.active = True
    
    def with_email(self, email):
        self.email = email
        return self
    
    def inactive(self):
        self.active = False
        return self
    
    def build(self):
        return User(email=self.email, name=self.name, active=self.active)

# Usage in tests
def test_inactive_user_cannot_login():
    inactive_user = UserBuilder().with_email("inactive@test.com").inactive().build()
    result = auth_service.login(inactive_user.email, "password")
    assert not result.success
```

## Integration

**Educational component** for maintaining test quality and preventing common testing mistakes

**Required by:** test-driven-development
**Integrates with:** verification-before-completion, systematic-debugging

**Used in conjunction with:**
- test-driven-development - for writing good tests initially
- verification-before-completion - for ensuring test quality
- systematic-debugging - for identifying test-related issues

## Common Questions

**Q: When should I use mocks?**
A: Use mocks when dependencies are slow, unreliable, or have side effects. Always understand the real dependency first.

**Q: How do I test internal logic without test-only methods?**
A: Test through the public interface, use integration tests, or consider if the internal logic should be a separate class.

**Q: What if I need to verify internal state?**
A: Question whether that state should be observable through the public interface. If not, consider if you're testing implementation details.

**Q: How detailed should my tests be?**
A: Focus on behavior and business outcomes. Test enough to be confident the code works correctly, but avoid testing every implementation detail.

## Examples

See the test patterns in this droid for comprehensive examples of good vs. bad testing practices.