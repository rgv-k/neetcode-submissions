class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(oc, cc, path):
            if oc == n and cc == n:
                result.append(''.join(path))
                return

            
            if oc < n:
                path.append('(')
                dfs(oc + 1, cc, path)
                path.pop()

            if cc < oc:
                path.append(')')
                dfs(oc, cc+1, path)
                path.pop()

        
        dfs(0,0,[])
        return result