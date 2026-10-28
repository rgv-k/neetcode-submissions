class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        heap = [-n for n in freq.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            while q and q[0][0] <= time:
                rem_time, rem_freq = q.popleft()
                heapq.heappush(heap, rem_freq)

            
            if heap:
                
                freq = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    q.append((time + n + 1, freq))

        return time