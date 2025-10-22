# Create sets for each course
python_students = {"Alice", "Bob", "Charlie"}
data_science_students = {"Charlie", "David", "Eve"}

# Add a new student to Python
python_students.add("Frank")

# Remove one student from Data Science
data_science_students.remove("David")

# Students enrolled in both courses
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)

# Students only in Python but not in Data Science
only_python = python_students - data_science_students
print("Students only in Python:", only_python)

# Combined list of all students (no duplicates)
all_students = python_students | data_science_students
print("All students:", all_students)

# Dictionary with course names and number of students
course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

# Print course name and number of students
for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

# Dictionary comprehension to double the student counts
expected_growth = {course: count*2 for course, count in course_counts.items()}
print("Expected growth (doubled):", expected_growth)
