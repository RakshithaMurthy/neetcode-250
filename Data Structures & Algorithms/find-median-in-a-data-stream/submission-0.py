class MedianFinder:

    def __init__(self):
        # max-heap for the lower half (store negatives)
        self.left = []
        # min-heap for the upper half
        self.right = []

    def addNum(self, num: int) -> None:
        # 1. push into left (max-heap)
        heapq.heappush(self.left, -num)

        # 2. move largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # 3. rebalance sizes (left must be >= right)
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2