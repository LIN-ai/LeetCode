#509. Fibonacci Number

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        F = [i for i in range(N+1)]
        for i in range(2,N+1):
            F[i] = F[i-1]+F[i-2]
        return F[-1]
        

