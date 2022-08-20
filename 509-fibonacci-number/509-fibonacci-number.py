class Solution:
    def fib(self, n: int) -> int:
        def fiba(n):
            if n==0 or n==1:
                return n
            else:
                return fiba((n-1)) + fiba((n-2))
        return fiba(n)