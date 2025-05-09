# List of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def display_students(student_list):
    """Display student records"""
    print("\nStudent Records:")
    for sid, name, major in student_list:
        print(f"ID: {sid} | Name: {name} | Major: {major}")

display_students(students)