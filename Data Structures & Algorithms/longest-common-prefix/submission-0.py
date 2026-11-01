class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        count = len(strs[0])

        for j in range(1, len(strs)):
            i = 0
            k = 0

            while i < count and k < len(strs[j]):
                if strs[0][i] == strs[j][k]:
                    i += 1
                    k += 1
                else:
                    break

            count = i

            if count == 0:
                return ""

        return strs[0][:count]

        
        return strs[0][:count]
    