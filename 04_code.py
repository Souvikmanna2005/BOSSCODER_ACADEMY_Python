"""Given a list of numbers, find the maximum and minimum
values"""

numbers=[20,15,35,10]

max_value=numbers[0]
min_value=numbers[0]

for num in numbers:
    if num>max_value:
        max_value=num
    if num<min_value:
        min_value=num
print('Maximum Value=',max_value)
print('Minimum Value=',min_value)