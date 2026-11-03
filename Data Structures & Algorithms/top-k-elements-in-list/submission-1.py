class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)

        heap = [(-count, element) for element, count in map.items()]

        heapq.heapify(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result