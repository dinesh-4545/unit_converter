# Unit converter: temperature, distance, weight

METERS_PER_KILOMETER = 1000
GRAMS_PER_KILOGRAM = 1000
ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_FAHRENHEIT = -459.67

print("Unit Converter")
print("1. Temperature")
print("2. Distance")
print("3. Weight")

choice = input("Choose an option: ")

if choice == "1":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    new_choice = input("Choose an option: ")

    if new_choice == "1":
        user_celsius = input("Enter temperature in Celsius: ")
        celsius = None

        try:
            celsius = float(user_celsius)
        except ValueError:
            print(f"Invalid number: '{user_celsius}'. Example: 12 or -3.5.")

        if celsius is None:
            print("No conversion done.")
        elif celsius != celsius:
            print("Invalid temperature: NaN is not allowed.")
        elif celsius == float("inf") or celsius == float("-inf"):
            print("Invalid temperature: Infinity is not allowed.")
        elif celsius < ABSOLUTE_ZERO_CELSIUS:
            print("Invalid temperature: Below absolute zero.")
        else:
            fahrenheit = celsius * 9 / 5 + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif new_choice == "2":
        user_fahrenheit = input("Enter temperature in Fahrenheit: ")
        fahrenheit = None

        try:
            fahrenheit = float(user_fahrenheit)
        except ValueError:
            print(f"Invalid number: '{user_fahrenheit}'. Example: 12 or -3.5.")

        if fahrenheit is None:
            print("No conversion done.")
        elif fahrenheit != fahrenheit:
            print("Invalid temperature: NaN is not allowed.")
        elif fahrenheit == float("inf") or fahrenheit == float("-inf"):
            print("Invalid temperature: Infinity is not allowed.")
        elif fahrenheit < ABSOLUTE_ZERO_FAHRENHEIT:
            print("Invalid temperature: Below absolute zero.")
        else:
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")

    else:
        print(f"Invalid option: {new_choice}. Choose between 1 and 2.")

elif choice == "2":
    print("Distance Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")

    new_choice = input("Choose an option: ")

    if new_choice == "1":
        user_meter = input("Enter distance in meters: ")
        meter = None

        try:
            meter = float(user_meter)
        except ValueError:
            print(f"Invalid number: '{user_meter}'. Example: 12 or 3.5.")

        if meter is None:
            print("No conversion done.")
        elif meter != meter:
            print("Invalid distance: NaN is not allowed.")
        elif meter == float("inf") or meter == float("-inf"):
            print("Invalid distance: Infinity is not allowed.")
        elif meter < 0:
            print("Invalid distance: Cannot be negative.")
        else:
            kilo_meter = meter / METERS_PER_KILOMETER
            print(f"{meter}m = {kilo_meter:.10g}km")

    elif new_choice == "2":
        user_kilo_meter = input("Enter distance in kilometers: ")
        kilo_meter = None

        try:
            kilo_meter = float(user_kilo_meter)
        except ValueError:
            print(f"Invalid number: '{user_kilo_meter}'. Example: 12 or 3.5.")

        if kilo_meter is None:
            print("No conversion done.")
        elif kilo_meter != kilo_meter:
            print("Invalid distance: NaN is not allowed.")
        elif kilo_meter == float("inf") or kilo_meter == float("-inf"):
            print("Invalid distance: Infinity is not allowed.")
        elif kilo_meter < 0:
            print("Invalid distance: Cannot be negative.")
        else:
            meter = kilo_meter * METERS_PER_KILOMETER
            print(f"{kilo_meter}km = {meter:.10g}m")

    else:
        print(f"Invalid option: {new_choice}. Choose between 1 and 2.")

elif choice == "3":
    print("Weight Converter")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")

    new_choice = input("Choose an option: ")

    if new_choice == "1":
        user_gram = input("Enter weight in grams: ")
        gram = None

        try:
            gram = float(user_gram)
        except ValueError:
            print(f"Invalid number: '{user_gram}'. Example: 12 or 3.5.")

        if gram is None:
            print("No conversion done.")
        elif gram != gram:
            print("Invalid weight: NaN is not allowed.")
        elif gram == float("inf") or gram == float("-inf"):
            print("Invalid weight: Infinity is not allowed.")
        elif gram < 0:
            print("Invalid weight: Cannot be negative.")
        else:
            kilo_gram = gram / GRAMS_PER_KILOGRAM
            print(f"{gram}g = {kilo_gram:.10g}kg")

    elif new_choice == "2":
        user_kilogram = input("Enter weight in kilograms: ")
        kilo_gram = None

        try:
            kilo_gram = float(user_kilogram)
        except ValueError:
            print(f"Invalid number: '{user_kilogram}'. Example: 12 or 3.5.")

        if kilo_gram is None:
            print("No conversion done.")
        elif kilo_gram != kilo_gram:
            print("Invalid weight: NaN is not allowed.")
        elif kilo_gram == float("inf") or kilo_gram == float("-inf"):
            print("Invalid weight: Infinity is not allowed.")
        elif kilo_gram < 0:
            print("Invalid weight: Cannot be negative.")
        else:
            gram = kilo_gram * GRAMS_PER_KILOGRAM
            print(f"{kilo_gram}kg = {gram:.10g}g")

    else:
        print(f"Invalid option: {new_choice}. Choose between 1 and 2.")

else:
    print(f"Invalid option: {choice}. Choose between 1 and 3.")
