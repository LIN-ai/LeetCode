{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution(object):\n",
    "    def numberOfLines(self, widths, S):\n",
    "        \"\"\"\n",
    "        :type widths: List[int]\n",
    "        :type S: str\n",
    "        :rtype: List[int]\n",
    "        \"\"\"\n",
    "        lines = 1\n",
    "        last = 0\n",
    "        for s in S:\n",
    "            width = widths[ord(s) - ord('a')]\n",
    "            last += width\n",
    "            if last > 100:\n",
    "                lines += 1\n",
    "                last = width\n",
    "        return [lines, last]\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pythonai] *",
   "language": "python",
   "name": "conda-env-pythonai-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
