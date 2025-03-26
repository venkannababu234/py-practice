tuple_list = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'), (1, 'f')]
group={}
for tup in tuple_list:
    key=tup[0]
    value=tup[1:]

    if key in group:
        group[key]+=value
    else:
        group[key]=value

result=[]
for key in group:
    result.append((key,)+group[key])

print(result)