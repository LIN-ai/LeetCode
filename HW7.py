#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

