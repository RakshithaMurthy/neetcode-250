class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictstr=defaultdict(list)
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in dictstr:
                dictstr[sorted_str].append(i)
            else:
                dictstr[sorted_str] = [i]
        return dictstr.values()
        