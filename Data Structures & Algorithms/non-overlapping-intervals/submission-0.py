class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[1], x[0]))

        removal = 0
        end = intervals[0][1]

        for start, ending in intervals[1:]:
            if end > start:
                removal += 1
                continue
            end = ending

        return removal