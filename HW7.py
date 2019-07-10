#961. N-Repeated Element in Size 2N Array

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        num =set()
        for i in A:
            if i not in num:
                num.add(i)
            else:
                return i

