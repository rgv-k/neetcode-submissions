class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        state = [False] * len(nums)
        def dfs(path, state):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not state[i]:
                    path.append(nums[i])
                    state[i] = True
                    dfs(path, state)
                    path.pop()
                    state[i] = False

        
        dfs([], state)
        return result
