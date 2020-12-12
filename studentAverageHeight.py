# Calculating average using for loops

#taking user inputs
student_height = input("Input a list of student heights ").split()

#converting datatype into int
for n in range(0,len(student_height)):
  student_height[n] = int(student_height[n])
  
#calculating student height average
students_height_average = 0
for i in student_height:
  students_height_average += i
  
#rounding the average height total
total_average = round(students_height_average/len(student_height))
print(total_average)

#Calculating average height using sum method
print(round(sum(student_height)/len(student_height)))
