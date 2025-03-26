student = {
    "name": "Alice",
    "age": 20,
    "contact": {
        "phone": "123-456-7890",
        "email": "alice@example.com"
    },
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

print("name",student.get('name'))
print('address',student["address"]["city"])
print('age',student['age'])

student["university"]="XYZ University"
student['grade']='A'

student.update({'girl':'sravani','married':'yes'})
print(student)
