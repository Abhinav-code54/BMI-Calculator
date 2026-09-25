from bmi import calculateBMI
from food import foodSuggestions
from routine import healthyRoutine
from information import bmiInformation


def mainMenu():

    while True:

        print("\n" + "=" * 50)
        print("       SMART BMI & HEALTHY ROUTINE ASSISTANT")
        print("=" * 50)

        print("1. Calculate BMI")
        print("2. Food Suggestions")
        print("3. Healthy Daily Routine")
        print("4. Learn About BMI")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            category = calculateBMI()

            print("\nWould you like to see food suggestions?")
            answer = input("Enter yes or no: ").lower()

            if answer == "yes":
                foodSuggestions(category)

        elif choice == "2":

            print("\nPlease calculate your BMI first using option 1.")

        elif choice == "3":

            healthyRoutine()

        elif choice == "4":

            bmiInformation()

        elif choice == "5":

            print("\nThank you for using Smart BMI Assistant!")
            break

        else:

            print("\nInvalid choice. Please try again.")


mainMenu()