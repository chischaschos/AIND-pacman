import unittest
from node import *
from sets import *

class NodeTest(unittest.TestCase):

    def test_node_in_list(self):
        n1 = Node(4)
        l = [n1]

        self.assertTrue(n1 in l)
        self.assertTrue(Node(5) not in l)

    def test_node_in_set(self):
        n1 = Node(4)
        s = Set()
        s.add(n1)

        self.assertTrue(n1 in s)
        self.assertTrue(Node(5) not in s)


if __name__ == '__main__':
    unittest.main()
