# test_zentoken.py
"""
Tests for ZenToken module.
"""

import unittest
from zentoken import ZenToken

class TestZenToken(unittest.TestCase):
    """Test cases for ZenToken class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenToken()
        self.assertIsInstance(instance, ZenToken)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenToken()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
