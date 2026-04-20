import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
        
    def test2(self):
        self.assertEqual(two_sum([3,2,4], 6), [1,2])
        
    def test3(self):
        self.assertEqual(two_sum([3,3], 6), [0,1])
        
    def test4(self):
        self.assertEqual(two_sum([3,5], 6), [-1])

32
if __name__ == '__main__':
    unittest.main()