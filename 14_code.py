'''Create a function to reverse a given string'''

#slicing
def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))


#loop
def reverse_string(text):
    rev = ""
    for char in text:
        rev = char + rev
    return rev
print(reverse_string("hello"))