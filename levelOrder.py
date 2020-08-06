"""
从上到下打印二叉树，给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    / \
   15  7
打印输出为 [3, 9, 20, 15, 7]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 这里使用标准层级遍历的方式
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return res