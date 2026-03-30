class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
            else:
                res.append(0)
        return res