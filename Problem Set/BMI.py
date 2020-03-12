# Olga Rozhdestvina
# This program calculates your Body Mass Index (BMI)

height = float (input("Enter your height in cm:  "))
weight = float (input("Enter your weight in kg:  "))

squareOfHeight = height ** 2 / 10000 # convert cm to m

BMI = weight / squareOfHeight
print("Your BMI is {:.2f}".format(BMI)) 

# Rounding to two decimal places found here https://stackoverflow.com/questions/5202233/how-to-change-39-54484700000000-to-39-54-and-using-python