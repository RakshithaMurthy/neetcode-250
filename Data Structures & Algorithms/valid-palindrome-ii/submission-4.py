class Solution:
    def validPalindrome(self, s : str) -> bool:
        l = 0
        r = len(s) - 1

        def isPalindrome(l,r):
            while l< r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        while l<r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l,r-1)

            l+=1
            r-=1

        return True