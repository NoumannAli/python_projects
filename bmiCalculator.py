#Requirements
#Write your code below this line 👇
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

#User Inputs
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#calculating Bmi
bmiValue = weight / (height * height)
yourBmi_Value = round(bmiValue , 2)
print(yourBmi_Value)

#checking weight categaroy
if yourBmi_Value < 18.5:
  print(f" Your Bmi is {yourBmi_Value}, You are underweight")
elif yourBmi_Value < 25:
  print(f" Your Bmi is {yourBmi_Value}, You are normal weight")
elif yourBmi_Value < 30:
  print(f" Your Bmi is {yourBmi_Value}, You are slightly overweight")
elif yourBmi_Value < 35:
  print(f" Your Bmi is {yourBmi_Value}, You are obese")
else:
  print(f" Your Bmi {yourBmi_Value}, You are clinically obese")
