"""Write a program to check if a number is even or odd"""

number=int(input('Enter a number:'))
even_or_odd= f"{number} is even number" if number%2==0 else f"{number} is odd number"
print(even_or_odd)