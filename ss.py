# Student Result Analyzer
students = [
    {"roll": 1, "name": "Amit", "marks": 78},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Rohan", "marks": 65}
]
# Function for sorting key
def get_marks(student):
    return student["marks"]
# Sorting by marks (descending)
sorted_students = sorted(students, key=get_marks, reverse=True)
print("Sorted Results (High to Low):")
for s in sorted_students:
    print(s["roll"], s["name"], s["marks"])
# Searching by name
search_name = input("\nEnter student name to search: ")
found = False
for s in students:
    if s["name"].lower() == search_name.lower():
        print("Found:", s["roll"], s["name"], s["marks"])
        found = True
        break
if not found:
    print("Student not found.")
