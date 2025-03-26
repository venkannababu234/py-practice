# Declaring two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 80]

# Finding the difference between two lists (elements in list1 but not in list2)
difference1 = []
for item in list1:
    if item not in list2:
        difference1.append(item)

# Finding the difference between two lists (elements in list2 but not in list1)
difference2 = []
for item in list2:
    if item not in list1:
        difference2.append(item)

# Printing the differences
print("Elements in list1 but not in list2:", difference1)
print("Elements in list2 but not in list1:", difference2)
