# test_computeprovisioning.py
"""
Tests for ComputeProvisioning module.
"""

import unittest
from computeprovisioning import ComputeProvisioning

class TestComputeProvisioning(unittest.TestCase):
    """Test cases for ComputeProvisioning class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ComputeProvisioning()
        self.assertIsInstance(instance, ComputeProvisioning)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ComputeProvisioning()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
