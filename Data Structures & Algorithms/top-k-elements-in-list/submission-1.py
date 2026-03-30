class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #print(freq)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #print(count.items())
        for n, c in count.items():
            freq[c].append(n)
            #print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            #print(i)
            for n in freq[i]:
                #print(n)
                res.append(n)
                #print(res)
                if len(res) == k:
                    return res