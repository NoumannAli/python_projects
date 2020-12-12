#taking user inputs
student_scores = input("Enter student scores ").split()

#coverting data type to int
for n in range(0,len(student_scores)):
  student_scores[n] = int(student_scores[n])

#finding the max score
max_score = 0
for i in student_scores:
  if i > max_score:
    max_score = i
print(max_score)

#finding max score using max method

print(max(student_scores))
