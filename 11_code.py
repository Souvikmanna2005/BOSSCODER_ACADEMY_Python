'''Given a list of numbers, find the sum and average'''

numbers = [1, 2, 3, 4]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

#loop

numbers = [1, 2, 3, 4]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)