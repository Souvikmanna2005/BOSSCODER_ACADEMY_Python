'''Given a list of names, concatenate them into a single 
string separated by spaces'''

#join()
names = ["Souvik", "Rahul", "Amit"]
result = " ".join(names)
print(result)

#loop
names = ["Souvik", "Rahul", "Amit"]
result = ""

for name in names:
    result += name + " "
print(result.strip())