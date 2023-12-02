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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)

        while q:
            levle_size = len(q)
            current_level_nodes = []
            for _ in range(levle_size):
                current_node = q.popleft()
                current_level_nodes.append(current_node.val)

                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.append(current_level_nodes)
        return result[::-1]
