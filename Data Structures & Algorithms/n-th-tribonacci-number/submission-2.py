class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        if n==1 or n==2: return 1
        s = [0] * (n+1)
        s[1]  = 1
        s[2] = 1

        for i in range(3, n+1):
            s[i] = s[i-1] + s[i-2] + s[i-3]


        return s[n]