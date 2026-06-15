print("=== World Cup 2026 Winner Predictor ===")

while True:

    country = input("\nEnter a country (or type EXIT to quit): ")

    # break statement
    if country.upper() == "EXIT":
        print("Program terminated.")
        break

    # continue statement
    if country == "":
        print("Country name cannot be empty!")
        continue

    # pass statement
    if country.upper() == "TBD":
        pass

    # Prediction logic
    if country.lower() == "argentina":
        print("Prediction: Strong chance of winning World Cup 2026.")

    elif country.lower() == "france":
        print("Prediction: Strong chance of winning World Cup 2026.")

    elif country.lower() == "spain":
        print("Prediction: Strong chance of winning World Cup 2026.")

    elif country.lower() == "brazil":
        print("Prediction: Strong chance of winning World Cup 2026.")

    elif country.lower() == "england":
        print("Prediction: Good chance of winning World Cup 2026.")

    else:
        print("Prediction: Low chance based on current football performance.")

print("Thank you for using the predictor.")