class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        index = 0
        xor_sum = 0

        def dfs(index, x):
            if index == len(nums):
                return x

            include = dfs(index + 1, x^nums[index])
            exclude = dfs(index +  1, x)

            return include + exclude
        
        return dfs(0, 0)

            