'''Write a Python program to check if a given string is a 
pangram (contains all letters of the alphabet)'''

#set()
text = input("Enter a string: ").lower()

alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(set(text)):
    print("Pangram")
else:
    print("Not a Pangram")


#loop
text = input("Enter a string: ").lower()

count = 0

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch in text:
        count += 1

if count == 26:
    print("Pangram")
else:
    print("Not a Pangram")