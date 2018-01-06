# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 01:08:56 2018

@author: zeba
"""
""" 
Regexp (Regular expression ) Python supports regular expressions for matching text patterns through
– re module

1) Capture Groups -> Make actual matched text available, groups delimited by ( ) as usual for regular
 expressions 
"""
import re
#getComponent = r"(\D+)(\d+)(\D+)(\d+)"
#inputText = "abcde1234defgh 4567"
#matchResults = re.search(getComponent, inputText)
#captureGroup = matchResults.groups()
#for group in captureGroup:
#    print(group)
""" 
The result of a re.search() operation is actually an object, containing a number of attributes. 
We can test for true/false since if there is no match the return value is null (None) which evaluates as false.
If we look inside the match object we can find the contents of any capture groups that may have been set up with 
the regular expressions using () characters. These can be returned as a list using the groups() method call. 
"""

""" 
2) Splitting Strings -> Divide a string into a list of components – based on RE used as separator.
"""
#p = re.compile(r'\W+')
#s = "210 Kandiwali west"
#print(p.split(s))
#
#res = re.split(r'/',"/user/bin/python")
#print(res)
""" A common task performed using regular expressions is to split a single string that is composed of a number 
of components (e.g.words) separated by some character or sequence of characters, into a list of the components.
For example we may wish to look at the components of a Unix pathname, or a line from a csv file, or a line from 
the Unix password file.
If we define a regular expression to represent the separator, and compile it, we have a method split() that takes 
a string and returns the components as a list.
"""

"""
3) Search and Replace
sub -> Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in 
string by the replacement repl.
subn ->Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made). """
pattern = re.compile("(red|green|blue)")
inputT = "red shirt, blue shorts and green socks"
print(inputT)
print(pattern.sub('white',inputT))
print(pattern.subn('white',inputT))
"""
 We can perform regular expression based search and replace using the sub() method on a compiled regular
 expression, applied to an input string. A new string is returned with the substitutions made.
If required, we can use the subn() method, which returns a tuple containing the new string and an integer 
representing the number of replacements that were made.
"""