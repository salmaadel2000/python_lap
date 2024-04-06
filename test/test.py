import unittest

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.is_empty():
            value = self.queue[0]
            del self.queue[0]
            return value
        else:
            print("Warning: Trying to pop from an empty queue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

class TestQueue(unittest.TestCase):
    def test_insert_and_pop(self):
        q = Queue()
        q.insert(1)
        q.insert(2)
        q.insert(3)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertIsNone(q.pop())

    def test_insertion(self):
        q = Queue()
        q.insert(1)
        q.insert(2)
        q.insert(3)
        self.assertEqual(q.queue, [1, 2, 3])

    def test_pop_from_empty_queue(self):
        q = Queue()
        self.assertIsNone(q.pop())

        q.insert(1)
        q.pop()
        self.assertIsNone(q.pop())

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.insert(1)
        self.assertFalse(q.is_empty())
        q.pop()
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()
