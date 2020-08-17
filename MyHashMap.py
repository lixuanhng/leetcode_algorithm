"""
不使用任何内建的哈希表库设计一个哈希映射

具体地说，你的设计应该包含以下的功能

put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
remove(key)：如果映射中存在这个键，删除这个数值对。

示例：

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);        
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashmap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MyHashMap:
    # 使用拉链法完成一个哈希表的映射
    # 在哈希表中的每个位置上，用一个链表来存储所有映射到该位置的元素。
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[] for _ in range(20011)]
        # 开辟一个大数组，长度为质数，注意这里不能用 [[]] * 20011
        # 一般定义成离2的整次幂比较远的质数，这样取模之后冲突的概率比较低。

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        t = key % 20011
        for item in self.hash[t]:  # 遍历哈希链表，查找key，找到后进行更新
            if item[0] == key:
                item[1] = value
                return  # 找到后直接返回
        self.hash[t].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        t = key % 20011
        for item in self.hash[t]:
            if item[0] == key:
                return item[1]
        return -1  # 可能哈希的位置，所对应的链表不为空，但是不存在该值

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        t = key % 20011
        delete = []
        for item in self.hash[t]:
            if item[0] == key:
                delete = item
        if delete:
            self.hash[t].remove(delete)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)