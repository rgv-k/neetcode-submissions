class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n == 0:
            return

        k %= n
        if k == 0:
            return 

            
        def reverse(nums, left, right):
            i = left
            j = right

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n -1)
        