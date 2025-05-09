class Solution:
    def __init__(self):
        self.moves = 0
    
    def distributeCoins(self, root):
        self.post_order_traversal(root)
        return self.moves
    
    def post_order_traversal(self, node):
        if node is None:
            return 0
        
        left = self.post_order_traversal(node.left)
        right = self.post_order_traversal(node.right)
        
        self.moves += abs(left) + abs(right)
        return node.val - 1 + left + right