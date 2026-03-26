'''Create a function to count the number of vowels in a 
given string'''

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))