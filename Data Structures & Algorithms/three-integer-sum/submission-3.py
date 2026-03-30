class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Stop early if the current number is positive
            if nums[i] > 0:
                break
            
            # Skip duplicate values for the `i` position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Move both pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values at the `l` pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # Skip duplicate values at the `r` pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
