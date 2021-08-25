# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above

# Write your code below this row
student_total = 0
student_height_total = 0
for student_height in student_heights:
  student_height_total += student_height
  student_total += 1

height_average = round(student_height_total/student_total)
print(height_average)