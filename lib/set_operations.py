# Dictionary storing student data with ID as key
student_dict = {
    101: {"name": "Alice Johnson", "major": "Computer Science", "courses": {"CS101", "CS102"}},
    102: {"name": "Bob Smith", "major": "Mathematics", "courses": {"MATH101", "MATH102"}},
    103: {"name": "Charlie Davis", "major": "Physics", "courses": {"PHYS101", "PHYS102"}},
}

def display_student_details(student_db):
    """Display student details from a dictionary"""
    print("\nStudent Details:")
    for sid, details in student_db.items():
        print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

display_student_details(student_dict)

def add_course(student_db, student_id, new_course):
    """Add a new course to a student's course set"""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")

add_course(student_dict, 101, "CS201")

# Display updated student data
display_student_details(student_dict)