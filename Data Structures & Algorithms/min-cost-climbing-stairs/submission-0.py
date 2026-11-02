class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minc = [0]*len(cost)

        minc[0] = cost[0]
        minc[1] = cost[1]

        for i in range(2, len(cost)):
            minc[i] = min(minc[i-1], minc[i-2]) + cost[i]


        return min(minc[-1], minc[-2])