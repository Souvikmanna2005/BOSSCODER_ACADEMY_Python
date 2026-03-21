"""Given a list of integers, find the sum of all positive
numbers"""

numbers = [10, -5, 20, -3, 7]

sum_positive = 0

for num in numbers:
    if num > 0:
        sum_positive += num

print("Sum of positive numbers:", sum_positive)