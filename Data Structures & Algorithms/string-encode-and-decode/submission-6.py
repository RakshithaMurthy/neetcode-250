class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) +"#" + word

        return s


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find '#'
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])   # get number
            word = s[j+1 : j+1+length]  # extract string

            res.append(word)

            # move i to next segment
            i = j + 1 + length

        return res

