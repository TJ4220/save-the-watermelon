import unittest
from src.logic import mask_word, is_win, normalize_guess, apply_guess, MAX_SLICES
class TestLogic(unittest.TestCase):
    def test_mask(self):
        self.assertEqual(mask_word("apple", set()), "_____")
    def test_win(self):
        self.assertTrue(is_win("abc", {"a","b","c"}))
        self.assertFalse(is_win("abc", {"a","b"}))
    def test_normalize(self):
        self.assertEqual(normalize_guess("A"), "a")
        self.assertIsNone(normalize_guess("ab"))
    def test_apply(self):
        g,s,hit = apply_guess("melon", set(), "m", MAX_SLICES)
        self.assertTrue(hit); self.assertIn("m", g); self.assertEqual(s, MAX_SLICES)
if __name__ == "__main__":
    unittest.main()
