my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

start_range = 30
end_range = 70

filtered_list = []

for item in my_list:
    if not (start_range <= item <= end_range):
        filtered_list.append(item)

print("List after removing elements in the range:", filtered_list)
