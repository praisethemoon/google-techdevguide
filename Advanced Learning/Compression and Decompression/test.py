import unittest
from app import decompress
class TestDecompress(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(
            decompress("10[a]"),
            "aaaaaaaaaa"
        )
    
    def test2(self):
        self.assertEqual(
            decompress("2[3[a]b]"),
            "aaabaaab"
        )
    
    def test3(self):
        self.assertEqual(
            decompress("3[abc]4[ab]c"),
            "abcabcabcababababc"
        )
    
if __name__ == '__main__':
    unittest.main()