from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
    # freq now maps number -> count

    # Step 2: Create buckets where index = frequency
    # Max possible frequency is len(nums)
        max_freq = max(freq.values())  # highest frequency
        buckets = [[] for _ in range(max_freq + 1)]
    # buckets[i] will hold list of numbers that appear i times
    
    # Step 3: Fill the buckets
        for num, count in freq.items():
            buckets[count].append(num)
    
    # Step 4: Gather results from highest frequency bucket down
        result = []
        for freq_count in range(max_freq, 0, -1):  # from max freq down to 1
            for num in buckets[freq_count]:
                result.append(num)
                if len(result) == k:  # Once we have k elements, stop
                    return result


        