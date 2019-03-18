temperature_1 = float(input("Please enter the first temperature value."))
temperature_2 = float(input("Please enter the second temperature value."))
temperature_3 = float(input("Please enter the third temperature value."))
temperature_4 = float(input("Please enter the fourth temperature value."))

temperature_list = (temperature_1, temperature_2, temperature_3,  temperature_4)
average_temperature = sum(temperature_list) / len(temperature_list)
max_value = max(temperature_list)
min_value = min(temperature_list)

print("The highest temperature is " + str(max_value) + ". The lowest temperature is " + str(min_value) +". The average temperature is " + str(average_temperature) + ".")
