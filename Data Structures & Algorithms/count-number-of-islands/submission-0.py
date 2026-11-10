class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1)
                ]

                for nr, nc in directions:
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    bfs(r, c)

        return island_count
