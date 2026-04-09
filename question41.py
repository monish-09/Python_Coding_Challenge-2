# Input dictionary of student marks
marks = {"A": 80, "B": 95, "C": 78}

# Find the student with highest marks
top_student = max(marks, key=marks.get)
highest_marks = marks[top_student]

# Display the result
print(f"Top student: {top_student} with marks: {highest_marks}")