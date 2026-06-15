from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            # window not valid
            #current window size = (r - l + 1)
            #replacements needed = window size - count of most frequent character
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

#Longest substring with at most K distinct characters
# from collections import defaultdict

# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         if k == 0:
#             return 0

#         count = defaultdict(int)
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             count[s[r]] += 1

#             while len(count) > k:
#                 count[s[l]] -= 1
#                 if count[s[l]] == 0:
#                     del count[s[l]]
#                 l += 1

#             res = max(res, r - l + 1)

#         return res

# #Longest substring with exactly K distinct characters

# from collections import defaultdict

# class Solution:
#     def longestKDistinct(self, s: str, k: int) -> int:
#         count = defaultdict(int)
#         l = 0
#         res = -1 #no valid substring

#         for r in range(len(s)):
#             count[s[r]] += 1

#             while len(count) > k:
#                 count[s[l]] -= 1
#                 if count[s[l]] == 0:
#                     del count[s[l]]
#                 l += 1

#             if len(count) == k:
#                 res = max(res, r - l + 1)

#         return res
'''
| Problem   | Condition                                       |
| --------- | ----------------------------------------------- |
| At most K | keep `≤ k`                                      |
| Exactly K | shrink if `> k`, update answer only when `== k` |

'''