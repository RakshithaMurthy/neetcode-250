class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictstr=defaultdict(list)
        for i in strs:
            sorted_str = ''.join(sorted(i))
            dictstr[sorted_str].append(i)
        return list(dictstr.values())