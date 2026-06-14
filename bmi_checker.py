

weight = float(input("Enter the weight :: "))
height = float(input("Enter the Height :: "))

# height = height / 100 # convert cm to meter

if height <= 0:
    print("Height is greater than 0")

else:
    bmi = weight / (height * height)
    print("Your BMI is :", bmi) # bmi(Body Mass Index)

    if bmi < 18.5:
        print("Underweight")

    elif bmi <= 24.9:
        print("Normal Weight")

    elif bmi <= 29.9:
        print("Overweight")
  
    else:
        print("obese")
