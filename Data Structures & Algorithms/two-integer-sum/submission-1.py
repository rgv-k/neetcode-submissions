class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}

        for i, n in enumerate(nums):
            c = target - n
            if c in req:
                return [req[c], i]

            req[n] = i

            