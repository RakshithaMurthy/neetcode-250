class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j =n-1
        k =m+n-1

        while i>=0 and j>=0:
            if nums1[i]> nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        
'''
import heapq

def mergeKArrays(arrays):
    heap = []
    result = []

    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    while heap:
        value, i, j = heapq.heappop(heap)
        result.append(value)

        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

    return result

    '''