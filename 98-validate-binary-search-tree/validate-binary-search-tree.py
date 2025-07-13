# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        node = root.left
        while node:
            if node.val >= root.val:
                return False
            node = node.right

        node = root.right
        while node:
            if node.val <= root.val:
                return False
            node = node.left

        return self.isValidBST(root.left) and self.isValidBST(root.right)
