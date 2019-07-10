#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        return sum(a != b for a, b in zip(sorted(heights), heights))

