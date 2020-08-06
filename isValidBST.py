# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.comparing(root, -(2**32), 2**32)

    def comparing(self, node, min_v, max_v):
        if node is None:
            return True
        if node.left is not None:
            if node.left.val >= node.val or node.left.val <= min_v:
                return False
        if node.right is not None:
            if node.right.val <= node.val or node.right.val >= max_v:
                return False
        return self.comparing(node.left, min_v, node.val) and self.comparing(node.right, node.val, max_v)


# 中序遍历，一次得到结果
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.search(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def search(self, root, res):
        if root:
            self.search(root.left, res)
            res.append(root.val)
            self.search(root.right, res)