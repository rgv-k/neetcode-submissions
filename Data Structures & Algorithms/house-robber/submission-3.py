class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums)
        p = [0] * n
        p[0], p[1] = nums[0], max(nums[0], nums[1])


        for i in range(2,n):
            p[i] = max(p[i-1], nums[i]+p[i-2])


        return p[n-1]