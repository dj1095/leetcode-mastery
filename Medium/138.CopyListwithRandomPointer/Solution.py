"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {}
        def dfs(node):
            if not node:
                return node
            if node in mapper:
                return mapper[node]
            copy = Node(node.val)
            mapper[node] = copy
            if node.next:
                copy.next = dfs(node.next)
            if node.random:
                copy.random = dfs(node.random)
            return copy
        return dfs(head)
