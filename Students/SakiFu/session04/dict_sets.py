#!/usr/bin/env python
# -*- coding: UTF-8 -*-
person = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
del person["cake"]
print person
#Add an entry for “fruit” with “Mango” and display the dictionary.
person["fruits"] = "Mango"
print person
person.keys()
person.values()
#Display whether or not “cake” is a key in the dictionary.
"cake" in person
#Display whether or not “Mango” is a value in the dictionary.
"Mango" in person

#2
a = range(16)
b = [hex(int(x)) for x in range(16)]
z = zip(a, b)
dic_hex = dict(z)

#3

for key, val in person.items():
    person[key] = val.count('a')
print person

#4
s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([3, 6, 9, 12, 15, 18])
s4 = set([4, 8, 12, 16, 20])
print s2
print s3
print s4
#Display if s3 is a subset of s2 (False)
s3 <= s2
#Desplay if s4 is a subset of s2 (True)
s4 <= s2


