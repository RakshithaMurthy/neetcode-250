class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
         return False
     
     # Create dictionaries to store the frequency of characters in the strings
        dictS, dictT = {}, {}
     
     # Count the occurrences of each character in string s
        for char in s:
            dictS[char] = dictS.get(char, 0) + 1
     
     # Count the occurrences of each character in string t
        for char in t:
            dictT[char] = dictT.get(char, 0) + 1
     
     # Compare the dictionaries
        return dictS == dictT