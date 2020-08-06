"""
有效括号的使用
"""
class Solution:
    def isValid(self, s: str) -> bool:
        valid = ['()', '{}', '[]']
        left = ['(', '{', '[']
        stack = []
        if len(s) % 2 == 0:
            for i in range(len(s)):
                if i == 0 and s[i] not in left:
                    return False
                    break
                elif s[i] in left:
                    stack.append(s[i])
                else:
                    pair = stack[-1] + s[i]
                    if pair in valid:
                        stack.pop(-1)
                    else:
                        return False
                        break
            if not stack:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    test1 = '()'
    print(Solution().isValid(test1))

    test2 = '()[]{}'
    print(Solution().isValid(test2))

    test3 = '(]'
    print(Solution().isValid(test3))

    test4 = '([)]'
    print(Solution().isValid(test4))

    test5 = '{[]}'
    print(Solution().isValid(test5))

    test6 = ']'
    print(Solution().isValid(test6))

    test7 = '['
    print(Solution().isValid(test7))

    test8 = '[]]'
    print(Solution().isValid(test8))

    test9 = '[[][]{}]'
    print(Solution().isValid(test9))

    test10 = '}]'
    print(Solution().isValid(test10))