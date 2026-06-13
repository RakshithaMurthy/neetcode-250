class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)) + '#' + i)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Manually find the next '#' instead of using s.index()
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # Move past '#'
            res.append(s[j : j + length])
            i = j + length
        return res
