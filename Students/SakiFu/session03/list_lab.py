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
num = raw_input("What is your favorite number? ")
#Display the number and the fruit corresponding to that number.
print fruits[int(num)]
print fruits
#Add another fruit to the beginning of the list using “+”.
fruits = ["Kiwis"] + fruits
print fruits
#Add another fruit to the beginning of the list using insert().
fruits.insert(0, "Mangos")
print fruits
#Display all the fruits that begin with “P”, using a for loop.
for i in fruits:
    if i[0] == "P":
        print i
    else:
        pass

print fruits
#Remove the last fruit from the list.
del fruits[-1]
print fruits
#Ask the user for a fruit to delete and find it and delete it.
dislike = raw_input("Which fruits you don't like?")
fruits.remove(dislike)

for i in fruits[:]:
    answer = raw_input("Do you like %s ? " % i.lower())
    while (answer != "No") and (answer != "Yes"):
        answer == raw_input("Yes or No")
    if answer == "No":
        fruits.remove(i)
    elif answer == "Yes":
        continue

fruits_copy = fruits[:]
fruits_copy = fruits_copy[::-1]
del fruits[-1]
print fruits
print fruits_copy
