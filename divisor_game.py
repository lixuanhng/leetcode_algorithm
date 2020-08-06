"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game

示例1：
输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

示例2：
输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        factor_a = []  # A可取的值组成的除数列表
        factor_b = []  # B可取的值组成的除数列表
        for i in range(1, N):
            if N % i == 0 and i != N:
                factor_a.append(i)
        a = factor_a[-1]