class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        min_ = max(piles)
        while left <= right:
            k = (left + right)//2
            summ = 0
            for i in range(len(piles)):
                summ += (piles[i] + k - 1 )// k

            if summ <= h:
                    min_ = min(min_, k)
                    right = k - 1
            else:
                    left = k + 1
        
        return min_
                

        