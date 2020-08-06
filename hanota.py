"""
汉诺塔问题，递归问题
"""

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self, n, A, B, C):
        if n == 1:
            # 当A中只有一个盘子时，将该盘子直接移到C中
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n-1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.move(n-1, B, A, C)