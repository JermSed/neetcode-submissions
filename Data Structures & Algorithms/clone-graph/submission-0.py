
class Solution:
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = defaultdict(Node)

        def visit(n):
            if n in visited:
                return visited[n]
            
            ans = Node(n.val)
            visited[n] = ans
            for i in n.neighbors:
                ans.neighbors.append(visit(i))
            
            return ans

        return visit(node)
