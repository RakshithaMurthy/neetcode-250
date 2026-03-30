class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list ={}
        output =[]
        for i in nums:
            dict_list[i] = dict_list.get(i,0) + 1

        sorted_list = [key for key,value in sorted(dict_list.items(), key=lambda item: item[1],reverse = True)]
        
        return sorted_list[:k]
        