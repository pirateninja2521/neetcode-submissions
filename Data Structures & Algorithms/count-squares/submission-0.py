class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        total = 0
        for key, count in self.points.items():
            dx, dy = key[0], key[1]
            if dx == x or dy == y:
                continue
            total += count * self.points[(dx, y)] * self.points[(x, dy)]
        return total