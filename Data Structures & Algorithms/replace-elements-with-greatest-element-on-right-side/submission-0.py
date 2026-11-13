class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        for i in range(n-1):   
            res[i] = max(arr[i+1:])

        res[n-1] = -1

        return res