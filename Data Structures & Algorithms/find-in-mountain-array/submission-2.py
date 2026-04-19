class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        n = mountainArr.length()

        # 1️⃣ Find peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # 2️⃣ Binary search on left (ascending)
        def binary_search_left(l, r):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        res = binary_search_left(0, peak)
        if res != -1:
            return res

        # 3️⃣ Binary search on right (descending)
        def binary_search_right(l, r):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:   # reverse condition
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        return binary_search_right(peak + 1, n - 1)
