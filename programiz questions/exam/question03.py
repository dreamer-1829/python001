students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"},
    {"id": 4, "name": "abijith"},
    {"id": 5, "name": "shino"},
    {"id": 6, "name": "deepa"},
    {"id": 7, "name": "renjith"},
    {"id": 8, "name": "aaron"},
    {"id": 9, "name": "ziya"}
]
student_id = int(input("Enter student ID: "))
found = False
for student in students:
    if student["id"] == student_id:
        print("Student name:", student["name"])
        found = True
        break
if not found:
    print("Student not found!")
