class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <=high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1

            elif nums[mid] == 1:
                mid +=1
            
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -=1
                

    '''
    [0 ... low-1]      → all 0s
    [low ... mid-1]    → all 1s
    [mid ... high]     → unknown (not processed yet)
    [high+1 ... end]   → all 2s
    Why the loop is while mid <= high
    Because: everything beyond high is already sorted (2s)
    '''