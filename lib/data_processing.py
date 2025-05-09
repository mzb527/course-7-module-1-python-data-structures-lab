from student_data import students

def student_generator(student_list, major):
    """Generate student records lazily for memory efficiency"""
    return (student for student in student_list if student[2] == major)

# Creating a generator for Mathematics students
math_students = student_generator(students, "Mathematics")

# Retrieving student records lazily
print(next(math_students))  # Output: (102, "Bob Smith", "Mathematics")
print(next(math_students))  # Output: (105, "Eve Lewis", "Mathematics")