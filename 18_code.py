'''Implement a program that converts a given number of 
minutes into hours and minutes'''

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Minutes:", remaining_minutes)