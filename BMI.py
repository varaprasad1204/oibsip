def calbmi(weight, height):
    bmi = weight / ((height/100) ** 2)
    return bmi
def catbmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def get_valid_input(prompt, datatype=float, min_val=None, max_val=None):
    while True:
        try:
            user_input = datatype(input(prompt))
            if (min_val is None or user_input >= min_val) and (max_val is None or user_input <= max_val):
                return user_input
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid value.")
def main():
    print("Welcome to the BMI Calculator")
    weight = get_valid_input("Enter your weight in kilograms: ", min_val=0.1, max_val=500)
    height = get_valid_input("Enter your height in centi meters: ", min_val=1, max_val=300)
    bmi = calbmi(weight, height)
    category = catbmi(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")
if __name__ == "__main__":
    main()
