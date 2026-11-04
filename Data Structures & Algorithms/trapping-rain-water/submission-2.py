class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        if n < 3: return 0
        prefix = [0] * n
        prefix[0] = height[0]
        
        suffix = [0] * n
        suffix[n-1] = height[n-1]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(1, n):
            suffix[n-i-1] = max(height[n-1-i], suffix[n-i])


        water = 0

        for i in range(1, n-1):
            water += min(prefix[i], suffix[i]) - height[i]


        return water