# Declare a tuple
my_tuple = (6,9,3,5,2,8,4,1,7)

# Specify the number of elements (K)
K = 3

# Sort the tuple and find the maximum and minimum K elements
sorted_tuple = sorted(my_tuple)

# Maximum K elements (last K elements in the sorted tuple)
max_k_elements = sorted_tuple[-K:]

# Minimum K elements (first K elements in the sorted tuple)
min_k_elements = sorted_tuple[:K]

# Print the results
print(f"The {K} maximum elements in the tuple are:", max_k_elements)
print(f"The {K} minimum elements in the tuple are:", min_k_elements)
