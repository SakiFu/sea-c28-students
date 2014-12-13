#!/usr/bin/env python
# -*- coding: UTF-8 -*-
food_prefs = {"name": u"Saki",
              u"city": u"Sapporo",
              u"cake": u"Redvelvet",
              u"fruit": u"Mango",
              u"salad": u"seaweed",
              u"pasta": u"seafood"}

print u"{name} is from {city}, and she likes {cake} cake, {fruit}\
 fruit, {salad} salad,\
 and {pasta} pasta".format(**food_prefs)

#2
list_hex = [(x, hex(int(x))) for x in range(16)]
dict(list_hex)

#3
hex_dict = {x: hex(int(x)) for x in range(16)}

#4
new_dict = food_prefs
for key, val in new_dict.items():
    new_dict[key] = val.count('a')
print new_dict

#5
s2 = {x for x in range(21) if not x % 2}
s3 = {x for x in range(21) if not x % 3}
s4 = {x for x in range(21) if not x % 4}
sx = {x for x in range(21) if not x % 2 or not x % 3 or not x % 4}
