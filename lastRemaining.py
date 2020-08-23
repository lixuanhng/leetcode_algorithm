"""
剑指 Offer 62. 圆圈中最后剩下的数字

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 
示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
"""


class Solution1:
    """
    使用循环列表的方式进行处理，会出现超时的情况
    """
    def lastRemaining(self, n: int, m: int) -> int:
        q = []
        for i in range(n):
            q.append(i)
        j = 1
        while len(q) > 1:
            if j < m:
                q.append(q.pop(0))
                j += 1
            else:
                j = 1
                q.pop(0)
        return q[0]


class Solution:
    """
    这个游戏里叫击鼓传花，西方也有叫热土豆。可通过严格的数学推导直接计算得出。但我们用程序来全真模拟才更真实。

    生成一个0、1、…、n-1的列表，初始索引i=0
    传递m次，意味着从i开始偏移m得到新索引i=i+m-1，考虑m可能大于当前列表长度，所以要对列表长度求模余
    从列表中pop出一个值后，实际上下一次偏移的初始索引仍然是当前pop掉的那个（因为后边的值都前移了一位），所以继续用i=i+m-1迭代新的索引，当然也要用新的列表长度求模余
    直至列表长度为1，返回最后剩下的数字。
    由于列表要执行pop操作 n-1次，而每次pop(i)是平均O(n)复杂度，所以总的时间复杂度是O(n^2)
    """
    def lastRemaining(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)
        return a[0]