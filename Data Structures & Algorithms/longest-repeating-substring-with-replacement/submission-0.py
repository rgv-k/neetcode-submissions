class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        left = 0
        freq = {}
        max_freq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            if not ((right-left + 1) - max_freq <= k):
                freq[s[left]] = freq.get(s[left]) - 1
                left += 1

        return right - left + 1
            
        