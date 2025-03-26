tuple_list = [(1, 3), (2, 1), (4, 2), (3, 5)]
n=len(tuple_list)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if tuple_list[j][1]<tuple_list[min_index][1]:
            min_index=j
    tuple_list[i],tuple_list[min_index]=tuple_list[min_index],tuple_list[i]

print(tuple_list)

#if tuple_list[j][-1] < tuple_list[min_index][-1]:  # Compare last elements #if we want sort by using the last element