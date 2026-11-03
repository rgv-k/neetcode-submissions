import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high):
            p = random.randint(low, high)
            nums[p], nums[high] = nums[high], nums[p]
            pivot = nums[high]
            i = low - 1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[high] = nums[high], nums[i+1]


            return i + 1

        def qsort(nums, low, high):
            if low < high:
                pivot_index = partition(nums, low, high)

                qsort(nums, low, pivot_index - 1)
                qsort(nums, pivot_index + 1, high)

        
        qsort(nums, 0, len(nums) - 1)
        return nums