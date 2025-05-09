class Solution:
    def lowestCommonAncestor(self, node, p, q):
        if not node or p == node or q == node:
            return node
        left  = self.lowestCommonAncestor( node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)
        if left and right:
            return node
        return left or right