"""
26. 删除排序数组中的重复项

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        # 数据有序，采用一次循环嵌套查找完成
        tmp = nums[0]  # 定义去重数组的最大值
        length = 1  # 定义去重数组的长度
        # 每次循环，判断当前值是否等于tmp，若不等于，则len加1，等于则继续
        for n in nums:
            if tmp != n:
                nums[length] = n
                tmp = n
                length += 1
        return length