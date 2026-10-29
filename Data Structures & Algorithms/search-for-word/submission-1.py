class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(r, c, index):
            if (r,c) in visited:
                return False
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])):
                return False
            if board[r][c] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True

            visited.add((r, c))
            result = dfs(r+1, c, index +1) or dfs(r, c+1, index +1) or dfs(r-1, c, index + 1) or dfs(r, c-1, index +1)
            visited.remove((r,c))
            return result

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
    


