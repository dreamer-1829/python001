# Create sets for each course
frontend = {"Alice", "Bob", "Charlie", "David"}
backend = {"Charlie", "Eve", "Frank"}

# Add a new student to Backend
backend.add("Grace")

# Remove a student from Frontend
frontend.remove("David")

# Students enrolled in both courses
both_courses = frontend & backend
print("Students in both courses:", both_courses)

# Students only in Backend, not in Frontend
only_backend = backend - frontend
print("Students only in Backend:", only_backend)

# Total number of unique students
unique_students = frontend | backend
print("Total unique students:", len(unique_students))

# Create dictionary for course counts
course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

# Print each course with the number of students
for course, count in course_counts.items():
    print(f"{course}: {count} students")

# Create a new dictionary with "Fullstack" course (combined)
fullstack_dict = {
    course: count for course, count in course_counts.items()
}
fullstack_dict["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]

print("\nUpdated dictionary with Fullstack course:")
print(fullstack_dict)