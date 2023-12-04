# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity - O(N)
# Space Complexity - O(N) beacause of Queue
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level = 1
        while q:
            level_size = len(q)
            for _ in range(level_size):
                current_node = q.popleft()
                if current_node.left is None and current_node.right is None:
                    return level
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            level += 1
        return level
