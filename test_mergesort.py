import unittest
from mergesort import merge

class MergeTest(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([6], [5]), [5,6])
        self.assertEqual(merge([7,8],[2,4]), [2,4,7,8])
        self.assertEqual(merge([1,3,5,6], [2,4,7,8]), [1,2,3,4,5,6,7,8])
        
        
# class MergeSortTest(unittest.TestCase):
    # def test_merge_sort(self):

if __name__ == '__main__':
    unittest.main() 
