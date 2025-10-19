# test_batchjobs.py
"""
Tests for BatchJobs module.
"""

import unittest
from batchjobs import BatchJobs

class TestBatchJobs(unittest.TestCase):
    """Test cases for BatchJobs class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BatchJobs()
        self.assertIsInstance(instance, BatchJobs)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BatchJobs()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
