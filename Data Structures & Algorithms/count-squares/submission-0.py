from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), freq in self.points.items():
            
            # Must share same x and different y
            if px == x and py != y:
                
                side = py - y

                total += (
                    freq *
                    self.points.get((x + side, y), 0) *
                    self.points.get((x + side, py), 0)
                )

                total += (
                    freq *
                    self.points.get((x - side, y), 0) *
                    self.points.get((x - side, py), 0)
                )

        return total
