class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        index = 0

        def dfs(index, path, target):
            if target == 0:
                result.append(path[:])
                return

            if index == len(candidates):
                return

            

            if target > 0 and candidates[index] <= target:
                    path.append(candidates[index])
                    dfs(index + 1, path, target - candidates[index])
                    path.pop()


            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1
                
            dfs(index+1, path, target)

        candidates.sort()
        dfs(0, [], target)

        return result

            
