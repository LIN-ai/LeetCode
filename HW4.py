#771.Jewels and Stones 

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j = set(list(J))
        s = list(S)
        count = 0
        for stone in s:
            if stone in j:
                count += 1
        return count

