# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        leftie = False
        rightie = False

        if root == None:
            return False

        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False

        if root.left != None:
            leftie = self.hasPathSum(root.left, sum - root.val)
            if leftie:
                return True

        if root.right != None:
            rightie = self.hasPathSum(root.right, sum - root.val)
            if rightie:
                return True

        return False
