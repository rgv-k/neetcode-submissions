class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        table = set()
        table.add(nums[0])


        for j in range(1, len(nums)):
            while abs(i - j) > k:
                table.remove(nums[i])
                i += 1


            if nums[j] in table:
                return True

            table.add(nums[j])


        return False
                