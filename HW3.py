#!/usr/bin/env python
# coding: utf-8

# In[ ]:



            


# In[13]:


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        
        print (rows)
        print (cols)
        for row in range(rows):
            A[row] = A[row][::-1]
            for col in range(cols):
                A[row][col] ^= 1
        return A


# In[ ]:




