# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0  # height = 0
            
            left_height = check(node.left)
            if left_height == -1:
                return -1  # left subtree unbalanced
            
            right_height = check(node.right)
            if right_height == -1:
                return -1  # right subtree unbalanced
            
            if abs(left_height - right_height) > 1:
                return -1  # current node unbalanced
            
            return max(left_height, right_height) + 1  # return height
        
        return check(root) != -1
        
        