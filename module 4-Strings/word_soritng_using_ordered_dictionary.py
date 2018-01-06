# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:32:04 2017

@author: zeba
"""

from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
counts = Counter(words)

print(len(counts))

for word in words:
    derp = counts.pop(word, None)
    if derp == None:
        continue
    else:
        print (derp)