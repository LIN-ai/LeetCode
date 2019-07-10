#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - min(A) - 2 * K, 0)

