class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6, TreeNode(5), TreeNode(7))

result = inorder_traversal(root)
print(result)
