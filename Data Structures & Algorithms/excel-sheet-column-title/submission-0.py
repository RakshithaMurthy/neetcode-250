class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1  # adjust to 0-based
            res.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return "".join(reversed(res))
        