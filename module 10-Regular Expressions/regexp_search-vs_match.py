# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:55:15 2018

@author: zeba
"""

"""
Python offers two different primitive operations based on regular expressions: 
re.match() checks for a match only at the beginning of the string, while
re.search() checks for a match anywhere in the string (this is what Perl does by default).
"""
import re
print("match 'c' in abcdef: ")
match_result=re.match("c", "abcdef") #not match
print(match_result)
print("search 'c' in abcdef: ")
search_result=re.search("c", "abcdef") #match
print(search_result)

"""
Regular expressions beginning with '^' can be used with search() to restrict
the match at the beginning of the string:
"""
print("match '^c' in abcdef: ")
match_result=re.match("^c", "abcdef") #not match
print(match_result)
print("search '^a' in abcdef: ")
search_result=re.search("^a", "abcdef") #match
print(search_result)

"""
Note however that in MULTILINE mode match() only matches at the beginning of the string, whereas
using search() with a regular expression beginning with '^' will match at the beginning of each line.
"""

print("match 'X' in 'A\nB\nX': ")
match_result=re.match('X', 'A\nB\nX', re.MULTILINE) #not match
print(match_result)
print("search '^X' in 'A\nB\nX': ")
search_result=re.search('^X', 'A\nB\nX', re.MULTILINE) #match
print(search_result)
