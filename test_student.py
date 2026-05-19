import unittest
from proj3 import *

class TestBenStudent(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap([Node(5, "a"), Node(3, "b")])
        result = heapify_up(heap, 1)
        self.assertEqual(result.data[0].freq, 3)

    def test_insert(self):
        heap = MinHeap()
        heap = insert(heap, Node(5, "a"))
        self.assertEqual(heap.data[0].freq, 5)
        self.assertEqual(len(heap.data), 1)

    def test_extract_min(self):
        heap = MinHeap([Node(2, 'b'), Node(5, 'a')])
        result = extract_min(heap)
        self.assertEqual(result[1].freq, 2)
        self.assertEqual(len(result[0].data), 1)



if __name__ == "__main__":
    unittest.main()
