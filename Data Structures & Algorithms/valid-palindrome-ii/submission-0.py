class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            
            return True

        

        low = 0
        high = len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return ispali(s, low + 1, high) or ispali(s, low, high - 1)

            low += 1
            high -= 1

        return True