class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        f = strs[0]
        l = strs[-1]

        count = 0
        while count < len(f) and count < len(l) and f[count] == l[count]:
            count+=1

        return f[:count]
    