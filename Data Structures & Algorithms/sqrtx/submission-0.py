class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        l, h = 1, x//2
        res = 1

        while l <= h:
            m = (l + h) // 2

            if m*m == x:
                return m

            elif m*m > x:
                h = m - 1
            
            else:
                
                res = max(res, m)
                l = m + 1

        return res