class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       n = len(nums)
       output = [1] * n
       left_product = 1
       right_product = 1
 
 # Calculate the product of all elements to the left of each element
       for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]
 
 # Calculate the product of all elements to the right of each element and multiply with the left product
       for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
 
       return output
        