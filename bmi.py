def calculateBMI():

    print("\n--- BMI CALCULATOR ---")

    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in cm: "))

        if weight <= 0 or height <= 0:
            print("\nPlease enter positive values.")
            return None

        heightMetres = height / 100

        bmi = weight / (heightMetres * heightMetres)

        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            category = "Below the usual adult BMI range"
            feedback = "Needs attention"

        elif bmi < 25:
            category = "Usual adult BMI range"
            feedback = "Good result"

        elif bmi < 30:
            category = "Above the usual adult BMI range"
            feedback = "Needs some attention"

        else:
            category = "High BMI range"
            feedback = "Needs attention"

        print("Category:", category)
        print("Feedback:", feedback)

        return category

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        return None