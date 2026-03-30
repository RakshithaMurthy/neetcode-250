class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list = Counter(nums)

        sorted_list = sorted(dict_list, key = dict_list.get, reverse = True)
        
        return sorted_list[:k]
        