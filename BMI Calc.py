print("Welcome to BMI Calculator")

height = float(input("Enter Your Height: "))
weight = int(input("Enter Your Weight: "))

BMI = weight / (height ** 2)

print(f"Your BMI is {int(BMI)}.")
