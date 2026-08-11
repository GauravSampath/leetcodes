class Solution(object):
    def fib(self, n):
     fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

     return fib(n)
        