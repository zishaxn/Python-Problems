# Implement a function that takes a list of strings as input and returns a new list with the strings
# sorted alphabetically in descending order.

strs = []
for i in range(0, 5):
    string = input(f"Enter {i + 1} String : ")
    strs.append(string)


print(strs)
strs = sorted(strs, reverse=True)
print(strs)