class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        index = 0
        xor_sum = 0

        def dfs(index, path):
            if index == len(nums):
                summ = 0
                for i in path:
                    summ ^= i
                return summ

            
            path.append(nums[index])
            include = dfs(index + 1, path)
            path.pop()

            exclude = dfs(index +  1, path)

            return include + exclude
        
        return dfs(0, [])

            