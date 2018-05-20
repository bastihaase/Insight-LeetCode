# In this file, I will implement my own ring queue / buffer

class Buffer:

    def __init__(self, size, values=[]):
        self.queue = [None] * size
        self.size = size
        self.start = - 1
        self.end = - 1
        self.add_list(values)

    def __str__(self):
        return str(self.queue)

    def add(self, value):
        self.end = (self.end + 1) % self.size
        self.queue[self.end] = value
        if self.end == self.start or self.start == -1:
            self.start = (self.start + 1) % self.size

    def add_list(self, values):
        for x in values:
            self.add(x)

    def get_start(self):
        return self.queue[self.start]

    def get_end(self):
        return self.queue[self.end]

    def is_full(self):
        return (self.end + 1) % self.size == self.start


import unittest


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.size = 10
        self.queue1 = Buffer(self.size)
        self.queue2 = Buffer(self.size, values=range(10))

    def test_init(self):
        self.assertEqual(self.queue1.queue, [None] * self.size)
        self.assertEqual(self.queue1.start, -1)
        self.assertEqual(self.queue1.end, -1)

        self.assertEqual(self.queue2.queue, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(self.queue2.start, 0)
        self.assertEqual(self.queue2.end, 9)

    def test_str(self):
        self.assertEqual(str(self.queue2), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")


    def test_add(self):
        self.queue1.add(20)
        self.assertEqual(self.queue1.start, 0)
        self.assertEqual(self.queue1.end, 0)
        self.assertEqual(self.queue1.queue, [20] + [None] * (self.size - 1))

        self.queue2.add(20)
        self.assertEqual(self.queue2.start, 1)
        self.assertEqual(self.queue2.end, 0)
        self.assertEqual(self.queue2.queue, [20, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_start(self):
        self.assertEqual(self.queue1.get_start(), None)
        self.assertEqual(self.queue2.get_start(), 0)

    def test_get_end(self):
        self.assertEqual(self.queue1.get_end(), None)
        self.assertEqual(self.queue2.get_end(), 9)


    def is_full(self, string):
        self.assertEqual(self.queue1.is_full(), False)
        self.assertEqual(self.queue2.is_full(), True)
