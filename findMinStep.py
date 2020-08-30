"""
回忆一下祖玛游戏。现在桌上有一串球，颜色有红色(R)，黄色(Y)，蓝色(B)，绿色(G)，还有白色(W)。 现在你手里也有几个球。

每一次，你可以从手里的球选一个，然后把这个球插入到一串球中的某个位置上（包括最左端，最右端）。接着，如果有出现三个或者三个以上颜色相同的球相连的话，就把它们移除掉。重复这一步骤直到桌上所有的球都被移除。

找到插入并可以移除掉桌上所有球所需的最少的球数。如果不能移除桌上所有的球，输出 -1 。

示例:
输入: "WRRBBW", "RB"
输出: -1
解释: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW （翻译者标注：手上球已经用完，桌上还剩两个球无法消除，返回-1）

输入: "WWRRBBWW", "WRBRW"
输出: 2
解释: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

输入:"G", "GGGGG"
输出: 2
解释: G -> G[G] -> GG[G] -> empty

输入: "RBYYBBRRB", "YRBGB"
输出: 3
解释: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

标注:

你可以假设桌上一开始的球中，不会有三个及三个以上颜色相同且连着的球。
桌上的球不会超过20个，输入的数据中代表这些球的字符串的名字是 "board" 。
你手中的球不会超过5个，输入的数据中代表这些球的字符串的名字是 "hand"。
输入的两个字符串均为非空字符串，且只包含字符 'R','Y','B','G','W'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zuma-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def elimination(s, start):
            if start < 0:
                return s
            # 从start开始对s进行消去
            len_s = len(s)
            if len_s <= 2:
                return s
            l = start  # r从右至左记录的是转盘中连续字符的所有位置，最终位置是最靠左的同颜色球的位置
            r = start  # r从左至右记录的是转盘中连续字符的所有位置，最终位置是最靠右的同颜色球的位置
            while l > 0 and s[l - 1] == s[start]:  # 这里每一个循环都表示从start的一个方向进行计数查找所有相同字符
                l -= 1
                if l == 0:
                    break
            while r < len_s - 1 and s[r + 1] == s[start]:  # 与上同
                r += 1
                if r == len_s - 1:
                    break
            if r - l <= 1:  # 判断最右位置与最左位置是否相差2个位置以上
                return s
            else:
                temp = s[:l] + s[r + 1:]  # 去掉相同字符后的拼接
                return elimination(temp, l - 1)  # 拼接之后再做一次消除，解决潜在的三个颜色相同的情况

        # 检查剩余手上的球是否还能消去所有球，如果不能直接返回-1
        board_balls = defaultdict(int)  ## 在每回合中对转盘中每类球进行计数
        hand_balls = defaultdict(int)  ## 在每回合中对手中的没垒球进行计数
        for i in board:
            board_balls[i] += 1
        for i in hand:
            hand_balls[i] += 1
        for i in board_balls:
            if board_balls[i] + hand_balls[i] < 3:  ## 若某类球在手中和转盘中的个数和小于3，则返回-1
                return -1

        played_hand = set()  # 记录本回合打过的球的种类，不重复打，剪枝操作
        n = len(board)  ## n为转盘球总数
        m = len(hand)  ## m手中球总数
        if n == 0:  ## 转盘球总数为0，则需要最少球数也为0
            return 0
        if m == 0:  ## 手中球总数为0，则不能移除桌上所有球，返回-1
            return -1
        ans = 6  # 球只有5种，6相当于无穷大
        flag = 0
        # 如果手牌中有一种球board里面只有一个，那么先打出去，不需要分枝
        for i in range(m):
            if board_balls[hand[i]] == 1:  ## 找到这个球在hand中的位置i
                flag = 1
                for j in range(n):
                    if board[j] == hand[i]:  ## 找到这个球在board中的位置j
                        temp = board[:j] + hand[i] + board[j:]  ## 组成新的board
                        temp = elimination(temp, j)  ## 对board进行消除操作
                        z = self.findMinStep(temp, hand[:i] + hand[i + 1:])  ## 传入消除后的board和打掉该球的hand
                        if z >= 0:
                            ans = min(ans, z)  ## 选取清除所有球的最少球数
                break

        # 通过递归来实现回溯算法
        if flag == 0:  ## 不存在手牌中有一种球board里面只有一个的情况
            for i in range(m):
                if hand[i] in played_hand:
                    continue
                else:
                    played_hand.add(hand[i])
                    for j in range(n):
                        if j > 0 and board[j] == board[j - 1]:
                            continue
                        if j < n - 1 and hand[i] != board[j]:
                            continue
                        temp = board[:j] + hand[i] + board[j:]
                        temp = elimination(temp, j)
                        z = self.findMinStep(temp, hand[:i] + hand[i + 1:])
                        if z >= 0:
                            ans = min(ans, z)

        return ans + 1 if ans != 6 else -1