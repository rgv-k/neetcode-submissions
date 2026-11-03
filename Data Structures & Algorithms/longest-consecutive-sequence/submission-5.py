class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        lseq = 0
        for i in nums:
            if i - 1 not in hset:
                curr = i
                cseq = 1


                while curr + 1 in hset:
                    curr += 1
                    cseq += 1

                
                lseq = max(lseq, cseq)

        return lseq