# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        level = 0

        while q:
            levle_size = len(q)
            # solution with deque for current level nodes
            current_level_nodes = deque()
            for _ in range(levle_size):
                current_node = q.popleft()
                if level % 2 == 1:
                    current_level_nodes.appendleft(current_node.val)
                else:
                    current_level_nodes.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.append(list(current_level_nodes))
            level += 1
        return result
