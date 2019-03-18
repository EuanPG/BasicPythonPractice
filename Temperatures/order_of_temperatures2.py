print ("Enter either 1 or 2 to determine temperature units.")
print ("1. Celsius.")
print ("2. Fahrenheit")

units_choice = input("Enter your choice[1-2]")
units_choice = int(units_choice)

temperature_1 = float(input("Please enter the first temperature value."))
temperature_2 = float(input("Please enter the second temperature value."))
temperature_3 = float(input("Please enter the third temperature value."))
temperature_4 = float(input("Please enter the fourth temperature value."))

temperature_list = (temperature_1, temperature_2, temperature_3, temperature_4)
average_temperature = sum(temperature_list) / len(temperature_list)
max_value = max(temperature_list)
min_value = min(temperature_list)


if units_choice == 1:

    print("The highest temperature is " + str(max_value) + '\xb0' + "C. The lowest temperature is " + str(
        min_value) + '\xb0' + "C. The average temperature is " + str(average_temperature) + '\xb0' + "C.")

else:
        print("The highest temperature is " + str(max_value) + '\xb0' + "F. The lowest temperature is " + str(
        min_value) + '\xb0' + "F. The average temperature is " + str(average_temperature) + '\xb0' + "F.")