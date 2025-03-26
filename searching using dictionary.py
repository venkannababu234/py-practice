students = {
    101: {"name": "Alice", "age": 20, "course": "Computer Science"},
    102: {"name": "Bob", "age": 22, "course": "Mechanical Engineering"},
    103: {"name": "Charlie", "age": 21, "course": "Electrical Engineering"}
}

students_id=int(input('enter any id'))

if students_id in students:
    print('id is found')
    print(f"name:{students[students_id]["name"]}")
    print(f"age:{students[students_id]["age"]}")
    print(f'course:{students[students_id]["course"]}')
else:
    print('id not found')