# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        self.summ=0
        def traversal(root):
            
            if root==None:

                return 0

            
            traversal(root.left)
            if root.val>=low and root.val<=high:

                self.summ+=root.val

            traversal(root.right)

        traversal(root)
        return self.summ

            

        
        
