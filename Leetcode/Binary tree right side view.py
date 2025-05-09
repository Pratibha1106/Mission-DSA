# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        if root==None:

            return[]

        result=[]
        queue=[root]

        while queue:

            level=len(queue)
            node_temp=[]

            for i in range(level):

                node=queue.pop(0)
                node_temp.append(node.val)

                if node.left!=None:

                    queue.append(node.left)

                if node.right!=None:

                    queue.append(node.right)

            
            result.append(node_temp[-1])

        return result