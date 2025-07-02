h_in_meter = input("Enter height in meters: ")
w_in_kg = input("Enter weight in kilograms: ")
h = float(h_in_meter)
w = float(w_in_kg)
BMI = (w) / (h**2)
if BMI>=30:
    print("Obesity")
elif BMI>25 and BMI<29:
    print("Overweight")
elif BMI>18.5 and BMI<25:
    print("Normal")
elif BMI>0 and BMI<18.5:
    print("Underweight")
else:
    print("Invalid Input")