class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)

        if lens1 > lens2:
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] +=1
        
        for char in s2[:lens1]:
            s2_count[ord(char) - ord('a')] +=1

        if s1_count == s2_count:
            return True

        for i in range(lens1, lens2):
            s2_count[ord(s2[i]) - ord('a')] +=1

            s2_count[ord(s2[i- lens1]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True
        return False


        