class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        heap = []
        for i in freq.values():
            heapq.heappush(heap, -i)
        q = deque()
        time = 0
        while heap or q:
            while q and q[0][0] <= time:
                rem_time, rem_freq = q.popleft()
                heapq.heappush(heap, rem_freq)

            
            if heap:
                
                freq = heapq.heappop(heap)
                freq += 1
                rem_time = time + n + 1

                if freq < 0:
                    q.append((rem_time, freq))

            time += 1
            
        return time