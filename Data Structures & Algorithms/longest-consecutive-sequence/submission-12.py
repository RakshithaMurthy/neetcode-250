class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxlen = 0
        for num in nums:
            if num-1 not in numset:
                count = 1
                candidate = num

                while candidate + 1 in numset:
                    count += 1
                    candidate +=1

                maxlen = max(maxlen, count)
        
        return maxlen
                
        