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

    def test_single_char(self):
        result = huffman_encoding("aaaa")
        self.assertEqual(result[1], "aaaa")
        self.assertEqual(len(result[2]), 1)

    def test_code_lengths(self):
        result = huffman_encoding("abcd")
        self.assertGreater(len(result[2]), 0)

    def test_repeated(self):
        result = huffman_encoding("aabb")
        self.assertEqual(result[1], "aabb")



if __name__ == "__main__":
    unittest.main()
