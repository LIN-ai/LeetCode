#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        last = 0
        for s in S:
            width = widths[ord(s) - ord('a')]
            last += width
            if last > 100:
                lines += 1
                last = width
        return [lines, last]
        

