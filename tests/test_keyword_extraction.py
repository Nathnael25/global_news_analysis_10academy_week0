import unittest
from src.utils import extract_keywords  # assuming this function exists in utils.py

class TestKeywordExtraction(unittest.TestCase):
    def test_extract_keywords(self):
        text = "This is a sample news article for keyword extraction."
        keywords = extract_keywords(text)
        self.assertIn("sample", keywords)
        self.assertIn("news", keywords)

if __name__ == "__main__":
    unittest.main()
