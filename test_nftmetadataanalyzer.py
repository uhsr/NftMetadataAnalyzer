# test_nftmetadataanalyzer.py
"""
Tests for NftMetadataAnalyzer module.
"""

import unittest
from nftmetadataanalyzer import NftMetadataAnalyzer

class TestNftMetadataAnalyzer(unittest.TestCase):
    """Test cases for NftMetadataAnalyzer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataAnalyzer()
        self.assertIsInstance(instance, NftMetadataAnalyzer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataAnalyzer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
