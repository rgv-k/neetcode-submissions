class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        o = len(nums)
        
        if o < 4: return []
        
        nums.sort()
        res = []


        for m in range(0, o - 3):
            if m > 0 and nums[m] == nums[m-1]:
                continue
            for n in range(m + 1, o - 2):
                if n > m + 1 and nums[n] == nums[n-1]:
                    continue

                i = n + 1
                j = o - 1

                while i < j:
                    summ = nums[m] + nums[n] + nums[i] + nums[j]

                    if summ < target:
                        i += 1

                    elif summ > target:
                        j -= 1

                    else:
                        res.append([nums[m], nums[n], nums[i], nums[j]])
                        i += 1
                        j -= 1

                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1


        return res

