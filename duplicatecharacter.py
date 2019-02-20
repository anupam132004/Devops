#! /usr/bin/python3
from collections import Counter

string = ("RAMAYAN")
print(string)

new = []
char = Counter(string)
print(char)

#finding Duplicate value
for key in char:
    if char.get(key)>1:
        print("Duplicate value is :",key)



