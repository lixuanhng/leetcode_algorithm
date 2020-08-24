"""
124. 二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxNum = float('-inf')  # 用来存储（root+left+right的最大值）
        def dfs(r):
            # 每次首先检查root是否为空，空则返回0
            if not r: return 0
            # 使用后序遍历
            left = dfs(r.left)  # 比较当前节点的左子树上所有值与0谁大，取大
            right = dfs(r.right)  # 比较当前节点的右子树上所有值与0谁大，取大
            self.maxNum = max(self.maxNum, left + right + r.val)
            return max(0, max(left, right) + r.val)
        dfs(root)
        return self.maxNum