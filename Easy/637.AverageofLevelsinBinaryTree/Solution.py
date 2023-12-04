# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity - O(N)
# Space Complexity - O(N) because of Q. In worst case there will be N/2 nodes at the deepest level
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            local_sum = 0
            for _ in range(level_size):
                currentNode = q.popleft()
                local_sum += currentNode.val
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
            result.append(local_sum / level_size)
        return result
