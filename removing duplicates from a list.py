# Declaring a list with duplicates
my_list = [10, 20, 30, 40, 20, 30, 50, 10, 60]

# Removing duplicates while maintaining the original order
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# Printing the list after removing duplicates
print("List after removing duplicates (order maintained):", unique_list)
