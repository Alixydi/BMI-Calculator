#BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / height **2
if bmi < 18.5:
  print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
  print(f"your bmi is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
  print("you are obese")
else:
  print("you are clinically obese")
