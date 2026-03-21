"""Create a Python function to check if a given string is a
palindrome """

def is_palindrome(s):
    return s == s[::-1]
text = "madam"
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")