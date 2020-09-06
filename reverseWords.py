"""
151. 翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        tmp_str = ''
        for i in range(len(s)):
            if s[i] == ' ' and tmp_str:
                stack.append(tmp_str)
                tmp_str = ''
            elif s[i] != ' ':
                tmp_str += s[i]
            else:
                continue
            if i == len(s) - 1:
                stack.append(tmp_str)
        result = ''
        while stack:
            result += stack.pop() + ' '
        return result.strip()