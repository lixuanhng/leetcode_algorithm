"""
520. 检测大写字母

给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

链接：https://leetcode-cn.com/problems/detect-capital
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        思路：
        只有一个字符时，一定是合法的
        首先判断字符串中第一个字符是否为大写，
        如果为大写，则判断剩下的字符是否全为大写或全为小写，是则合法，不是则非法
        如果为小写，则判断剩下的字符是否全为小写，是则合法，不是则非法
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:  # 只有一个字母时，直接返回True
            return True

        letter_one = ord(word[0])  # 返回一个字符的ASCII码
        # letter_two = word[1]
        if 65 <= letter_one <= 90:
            return self.letter_all_capital_or_lower(word[1:])

        return self.letter_all_lower(word[1:])
        # for i in word:

    def letter_all_capital_or_lower(self, word):
        #
        lower = False
        capital = False

        # A-Z
        left = 65
        right = 90

        # 通过检查传入字符串的第二个字符来确定左右数值
        # 因为只要不满足全小写或是全大写，就是非法
        if 97 <= ord(word[0]) <= 122:
            left = 97
            right = 122

        for i in word:
            if not left <= ord(i) <= right:
                return False
        return True

    def letter_all_lower(self, word):
        for i in word:
            if not 97 <= ord(i) <= 122:
                return False
        return True