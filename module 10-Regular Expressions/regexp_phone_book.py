# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:11:54 2018

@author: zeba
"""
import re
print("**********Making a Phonebook**********")
"""split() splits a string into a list delimited by the passed pattern. The method is invaluable 
 for converting textual data into data structures that can be easily read and modified by Python as
 demonstrated in the following example that creates a phonebook. First, here is the input. Normally 
 it may come from a file, here we are using triple-quoted string syntax:
"""
text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue

Frank Burger: 925.541.7625 662 South Dogwood Way 

Heather Albrecht: 548.326.4584 919 Park Place"""
 
"""
The entries are separated by one or more newlines. 
Now we convert the string into a list with each nonempty line having its own entry:
"""
entries = re.split("\n+",text)
print(entries)

"""
Finally, split each entry into a list with first name, last name, telephone number, 
and address. We use the maxsplit parameter of split() because the address has spaces, 
our splitting pattern, in it
"""

[re.split(":? ", entry, 3) for entry in entries]

"""
The :? pattern matches the colon after the last name, so that it does not occur in the result list.
With a maxsplit of 4, we could separate the house number from the street name:
"""
[re.split(":? ", entry, 4) for entry in entries]