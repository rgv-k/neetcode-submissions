class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path, state):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if state[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not state[i-1]:
                    continue

                path.append(nums[i])
                state[i] = True
                dfs(path, state)
                path.pop()
                state[i] = False


        nums.sort() 
        dfs([], [False]*len(nums))
        return result
