# Creating two arrays (one with duplicates and the other without duplicates)
array_with_duplicates = [1, 2, 2, 3, 4, 4, 5,6]
array_without_duplicates = [1, 2, 3, 4, 5]

# Converting both arrays to sets
set_with_duplicates = set(array_with_duplicates)
set_without_duplicates = set(array_without_duplicates)

# Finding the lost element (difference between sets)
lost_elements = set_with_duplicates.difference(set_without_duplicates)

# Printing the lost elements
print("Lost elements from the duplicated array:", lost_elements)
