'''Implement a program that checks if a given string is a 
palindrome'''

#slicing
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


#loop
text = input("Enter a string: ")

is_palindrome = True
n = len(text)

for i in range(n // 2):
    if text[i] != text[n - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
