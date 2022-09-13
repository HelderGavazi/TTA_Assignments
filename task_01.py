# TechTalentAcademy
# Author: Helder Paixao
# Week Three: 25th May 2022
# Python Fundamentals - Extension_Tasks
# Task_01

# Ask for the total price of a bill, then ask how many dinners there are.
# Divide the total bill by the number of diners and show how much each person should pay

total_price = int(input("Please insert the total price of the bill: £"))
diners = int(input("How many people are sharing the bill! "))
print('Etch person has to pay: £', int(total_price / diners))