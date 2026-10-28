class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -(heapq.heappop(heap))
            y = -(heapq.heappop(heap))
            x -= y
            if x  > 0:
                heapq.heappush(heap, -x)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]