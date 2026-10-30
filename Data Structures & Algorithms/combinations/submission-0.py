class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(path, start):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                dfs(path, i+1)
                path.pop()


        dfs([], 1)
        return result