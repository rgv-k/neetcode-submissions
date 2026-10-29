class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        index = 0
        def dfs(index, path, target):       
            if target == 0:
                result.append(path[:])
                return

            if index == len(nums):
                return

            if target > 0 and nums[index] <= target:
                path.append(nums[index])
                dfs(index, path, target - nums[index])
                path.pop()

            dfs(index + 1, path, target)
            

        dfs(0, [], target)
        return result