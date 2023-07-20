# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        self.findPathSum(root, 0,[] ,targetSum, allPaths)
        return allPaths

    def findPathSum(self,root:Optional[TreeNode], currentSum:int, path:List[int],targetSum:int, allPaths:List[List[int]]):
        if not root:
            return allPaths
        
        currentSum += root.val
        newPath = path + [root.val]
        if root and not root.left and not root.right and currentSum == targetSum:
            allPaths.append(newPath)
        self.findPathSum(root.left, currentSum, newPath ,targetSum,allPaths)
        self.findPathSum(root.right, currentSum, newPath,targetSum,allPaths)
        return allPaths
