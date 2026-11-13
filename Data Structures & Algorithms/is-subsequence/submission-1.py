class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(s) > len(t): return False

        m = 0
        n = 0

        while m < len(s) and n < len(t):
            if s[m] == t[n]:
                m += 1
                n += 1

            else:
                n += 1

        if m == len(s): return True

        return False