class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        #print(ans)
        for s in strs:
            count = [0] * 26
            #print(count)
            for c in s:
                #print(c)
                count[ord(c) - ord("a")] += 1
                #print(count[ord(c) - ord("a")])
            ans[tuple(count)].append(s)
            #print(ans)
        return ans.values()