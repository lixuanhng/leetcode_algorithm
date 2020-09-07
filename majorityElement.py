"""
169. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 依旧使用hash
        if len(nums) < 2: return nums[0]
        ht = {}
        for item in nums:
            if item in ht.keys():
                ht[item] += 1
                if ht[item] > len(nums) / 2:
                    return item
            else:
                ht[item] = 1



class Solution1:
    def majorityElement1(self, nums: List[int]) -> int:
        # 当必然有一个数出现的次数要超过数组长度的一般
        # 则这个数出现一次，就消掉一个别的数，遍历之后可以发现，最后剩下的一定是这个数
        result = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if nums[i] != result:
                times -= 1
            else:
                times += 1
            if times == -1:
                times = 1
                result = nums[i]
        return result