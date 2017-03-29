"""
Node
"""

class Node:
    """
      Node
    """

    def __init__(self, value):
        self.value = value
        self.cost = 0
        self.action = ''
        self.parent = ''

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def add_cost(self, cost):
        self.cost += cost

    def get_state(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def path(self):
        path = []
        tmp_node = self

        while tmp_node and tmp_node.get_action():
            path.insert(0, tmp_node.get_action())
            tmp_node = tmp_node.get_parent()

        return path

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
