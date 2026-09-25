def foodSuggestions(category):

    print("\n--- FOOD SUGGESTIONS ---")

    if category == "Below the usual adult BMI range":

        print("Suggested balanced meals:")
        print("• Breakfast: Poha with vegetables and fruit")
        print("• Lunch: Dal, rice/roti and vegetables")
        print("• Snack: Fruit, curd or nuts")
        print("• Dinner: Roti, vegetables and paneer/dal")

    elif category == "Usual adult BMI range":

        print("Suggested balanced meals:")
        print("• Breakfast: Idli with sambar or oats with fruit")
        print("• Lunch: Roti, dal and vegetables")
        print("• Snack: Fruit or roasted chana")
        print("• Dinner: Roti, vegetables and dal")

    elif category == "Above the usual adult BMI range":

        print("Suggested balanced meals:")
        print("• Breakfast: Vegetable poha or oats with fruit")
        print("• Lunch: Roti, dal and plenty of vegetables")
        print("• Snack: Fruit, curd or roasted chana")
        print("• Dinner: Roti, vegetables and dal/paneer")

    else:

        print("Suggested balanced meals:")
        print("• Breakfast: Oats or vegetable poha with fruit")
        print("• Lunch: Dal, roti and plenty of vegetables")
        print("• Snack: Fruit or roasted chana")
        print("• Dinner: Vegetables, roti and dal/paneer")

    print("\nThese are general educational suggestions.")