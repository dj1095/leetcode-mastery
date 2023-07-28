"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNewMapper = {}
        def dfs(oldNode):
            if not oldNode:
                return oldNode
            if oldNode in oldToNewMapper:
                return oldToNewMapper[oldNode]
            copy = Node(oldNode.val)
            oldToNewMapper[oldNode] = copy
            for neighbor in oldNode.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)


        
