"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Time complexity - O(N)
# Space Complexity - O(N) due to queue used


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            previous_node = None
            for _ in range(level_size):
                current_node = q.popleft()
                if previous_node:
                    previous_node.next = current_node
                previous_node = current_node

                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

        return root
