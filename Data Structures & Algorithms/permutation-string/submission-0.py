class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        s1_dict = dict()
        s2_dict = dict()

        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1

        left = 0
        right = len(s1) - 1

        for i in range(left, right + 1):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
        while True:
            if s1_dict == s2_dict: return True
            if right == len(s2) - 1: break
            

            s2_dict[s2[left]] = s2_dict.get(s2[left], 0) - 1
            if s2_dict[s2[left]] == 0: del s2_dict[s2[left]]
            left += 1
            right += 1
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1


        return False
        