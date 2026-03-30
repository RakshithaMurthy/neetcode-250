class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        reverse = filtered_s[::-1]
        return filtered_s == reverse