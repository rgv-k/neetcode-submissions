class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        li = [0] * (2 * ln)
        for i in range(ln):
            li[i] = nums[i]
            li[i + ln] = nums[i]

        return li