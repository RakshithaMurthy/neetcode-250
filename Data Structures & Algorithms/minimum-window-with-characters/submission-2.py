class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Build need map manually
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Check if this character just satisfied its requirement
            if c in need and window[c] == need[c]:
                formed += 1

            # Try shrinking the window
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result

        