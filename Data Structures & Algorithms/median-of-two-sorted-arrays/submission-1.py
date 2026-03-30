class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m,n = len(nums1), len(nums2)
        l,r = 0, m

        while l <=r:
            partition1 = (l+r) // 2
            partition2 = (m+n+1)//2 - partition1

            maxleft1 = float("-inf") if partition1 ==0 else nums1[partition1 - 1]
            minright1 = float("inf") if partition1 == m else nums1[partition1]

            maxleft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minright2 = float("inf") if partition2 == n else nums2[partition2]

            if maxleft1 <=minright2 and maxleft2<=minright1:
                if (m+n) % 2 == 0:
                    return (max(maxleft1,maxleft2) + min(minright1, minright2)) / 2
                else:
                    return max(maxleft1, maxleft2)
                
            elif maxleft1 > minright2:
                r = partition1 -1
            else:
                l = partition1 + 1
