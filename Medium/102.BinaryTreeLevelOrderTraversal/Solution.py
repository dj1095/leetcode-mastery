# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity - O(N) Since it iterated over all the nodes in the tree only once
# Space Complexity - O(N) since in the worst the q has to hold (N/2) nodes in the last level
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        # Using Outer loop to iterate  each level
        while q:
            level_size = len(q)
            current_level_nodes = []
            # Using Inner loop to collect all nodes at that level
            for _ in range(level_size):
                currentNode = q.popleft()
                current_level_nodes.append(currentNode.val)
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
            result.append(current_level_nodes)
        return result
