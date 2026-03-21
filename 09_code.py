"""Create a program that takes a sentence as input and
counts the number of words in it"""

sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)