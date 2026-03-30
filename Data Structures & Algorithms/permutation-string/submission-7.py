class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        m, n = len(s1), len(s2)

        freq_s1 = [0] * 26
        window = [0] *26

        for i in range(m):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if freq_s1 == window:
            return True
        
        for i in range(m, n):
            #Add new char
            window[ord(s2[i]) - ord('a')] += 1
            #Remove leftmost char
            window[ord(s2[i-m]) - ord('a')] -= 1

            if freq_s1 == window:
                return True

        return False

        