#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        directs = {'L':-1, 'R':1, 'U':1j, 'D':-1j}
        
        x =sum(directs[move] for move in moves)
        
        return 0==x

