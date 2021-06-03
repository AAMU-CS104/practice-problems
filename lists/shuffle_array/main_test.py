import unittest
import main_solutions

class TestMain(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(main_solutions.shuffle([1,1,2,2],2), [1,2,1,2])
        self.assertEqual(main_solutions.shuffle([1,1,1,2,2,2],3), [1,2,1,2,1,2])

if __name__ == '__main__':
    unittest.main()