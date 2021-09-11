student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def student_grade(score):
  if score >= 91:
    return "Outstanding"
  elif score >= 81:
    return "Exceed Expectations"
  elif score >= 71:
    return "Acceptable"
  else:
    return "Fail"

for student in student_scores:
  score = int((student_scores[student]))

  final_grade = student_grade(score)
  student_grades[student] = final_grade

# 🚨 Don't change the code below 👇
print(student_grades)