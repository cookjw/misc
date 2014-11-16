import unittest
from mergesort import merge, merge_sort

class MergeTest(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([6], [5]), [5,6])
        self.assertEqual(merge([7,8],[2,4]), [2,4,7,8])
        self.assertEqual(merge([1,3,5,6], [2,4,7,8]), [1,2,3,4,5,6,7,8])        
        self.assertEqual(merge([1,2],[3]),[1,2,3])
        self.assertEqual(merge([6,7,8,9], [1,2,3,4,5]), [1,2,3,4,5,6,7,8,9])       
        
        
class MergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(merge_sort([9,8,7,6,6,5,23,1]), [1,5,6,6,7,8,9,23])

if __name__ == '__main__':
    unittest.main() 
