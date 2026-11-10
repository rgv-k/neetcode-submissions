class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_array = [0] * (n + 1)
        out_array = [0] * (n + 1)
        for i, j in trust:
            in_array[j] += 1
            out_array[i] += 1

        for i in range(1, n+1):
            if in_array[i] == n-1 and out_array[i] == 0:
                return i

        return -1
