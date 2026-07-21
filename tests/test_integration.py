"""Integration tests for myproject package."""

import pytest

from myproject.pkg1 import simple_fn
from myproject.pkg2 import complex_fn


def test_integration_pkg1_and_pkg2():
    """Test integration between pkg1 and pkg2."""
    # Use pkg1 function
    result1 = simple_fn.add(5, 3)
    
    # Use the result in pkg2
    result2 = complex_fn.multiply(result1, 2)
    
    assert result2 == 16


def test_integration_workflow():
    """Test a complete workflow using both packages."""
    # Start with simple operations
    val1 = simple_fn.add(10, 5)
    val2 = simple_fn.diff(10, 5)
    
    # Combine results
    final_result = complex_fn.multiply(val1, val2)
    
    assert final_result == 75  # (15) * (5) = 75


def test_error_handling():
    """Test error handling across packages."""
    with pytest.raises(Exception):
        complex_fn.multiply(5, "invalid")
