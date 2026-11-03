class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1: return [strs]

        strs = [["".join(sorted(x)), x] for x in strs]

        table = defaultdict(list)

        for i, j in strs:
            table[i].append(j)

        return list(table.values())


