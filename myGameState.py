class MyGameState:

    def __init__(self, position):
        self.position = position
        self.corners = None

    def updateCorners(self, corners):
        self.corners = tuple([t for t in corners if t != self.position])

    def areCornersCovered(self):
        return len(self.corners) <= 0

    def __eq__(self, other):
        if other is None:
            return False

        return self.position == other.position and self.corners == other.corners

    def __hash__(self):
        return hash(self.position) + hash(self.corners)

    def __str__(self):
        return str(self.position) + str(self.corners)
