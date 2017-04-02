class MyGameState:

    def __init__(self, position):
        self.position = position

    def __eq__(self, other):
        if other is None:
            return False

        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __str__(self):
        return str(self.position)
