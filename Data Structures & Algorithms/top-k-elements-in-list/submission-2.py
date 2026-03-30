class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the array
        freq_map = Counter(nums)
        print("Frequency Map:", freq_map)
 
        # Sort the elements based on their frequency in descending order
        sorted_freq = sorted(freq_map, key=freq_map.get, reverse=True)
        print("Sorted Frequency:", sorted_freq)
 
        # Return the first k elements from the sorted list
        return sorted_freq[:k]