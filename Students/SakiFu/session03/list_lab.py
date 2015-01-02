#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
# #Display the list.
print fruits
# #Ask the user for another fruit and add it to the end of the list.
fruit = raw_input("What is your favorite fruit? ")
fruits.append(fruit)
print fruits
#Ask the user for a number
num = int(raw_input("What is your favorite number? "))
#Display the number and the fruit corresponding to that number.
print fruits[int(num - 1)]
print fruits
#Add another fruit to the beginning of the list using “+”.
fruits = ["Kiwis"] + fruits
print fruits
#Add another fruit to the beginning of the list using insert().
fruits.insert(0, "Mangos")
print fruits
#Display all the fruits that begin with “P”, using a for loop.
for i in fruits:
    if i[0].lower() == "p":
        print i
    else:
        pass

print fruits
#Remove the last fruit from the list.
del fruits[-1]
print fruits
#Ask the user for a fruit to delete and find it and delete it.
dislike = raw_input("Which fruits you don't like?")
while dislike in fruits:
    fruits.remove(dislike)

print fruits

for i in fruits[:]:
    answer = raw_input("Do you like %s ? " % i)
    if answer.lower() == "no":
        while i in fruits:
            fruits.remove(i)
    elif answer.lower() == "yes":
        pass
    else:
        print "Yes or No"

#Make a copy of the list and reverse the letters in each fruit.
copy_fruits = []
for i in fruits:
    copy_fruits.append(i[::-1])

print fruits
print copy_fruits
