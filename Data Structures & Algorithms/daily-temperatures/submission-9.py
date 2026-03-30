class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, num in enumerate(temperatures):
            while stack and num > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index

            stack.append((i, num))

        return res
