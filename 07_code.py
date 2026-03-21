"""Write a program that converts a given number of days
into years, weeks, and days"""

def convert_days(total_days):
    years = total_days // 365
    remaining_days = total_days % 365

    weeks = remaining_days // 7
    days = remaining_days % 7

    return years, weeks, days

days_input = int(input("Enter number of days: "))

y, w, d = convert_days(days_input)

print("Years:", y)
print("Weeks:", w)
print("Days:", d)