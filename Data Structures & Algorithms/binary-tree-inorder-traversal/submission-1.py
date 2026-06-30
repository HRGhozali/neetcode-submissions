# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, point, traversal):
        if not point: return
        self.traverse(point.left, traversal)
        traversal.append(point.val)
        self.traverse(point.right, traversal)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse = []
        self.traverse(root, traverse)
        return traverse