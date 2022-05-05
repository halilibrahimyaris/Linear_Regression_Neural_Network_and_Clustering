class Point:

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def str(self):
        return f"(x: {self.x}, y: {self.y})"

    def to_tuple(self):
        return self.x, self.y
