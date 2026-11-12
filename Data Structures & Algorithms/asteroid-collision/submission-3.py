class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for i in asteroids:
            if not res:
                res.append(i)
                continue
            while res and res[-1] > 0 and i < 0:
                if abs(res[-1]) < abs(i):
                    res.pop()
                    continue
                elif res[-1] == abs(i):
                    res.pop()
                    break
                else:
                    break
            
            else:
                res.append(i)


        return res