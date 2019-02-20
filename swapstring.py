#! /usr/bin/python3
# Program to swap two string variables

var1 = "Hello"
var2 = "World"

print("Before swapping values are :",var1, "and",var2)
var1 = var1 + var2
var2 = var1[0: (len(var1) - len(var2))]
var1 = var1[len(var2):]

print("After swapping values are:", var1,"and", var2)

