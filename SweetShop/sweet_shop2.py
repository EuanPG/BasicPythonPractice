price1 = input("Enter the price of the first sweet: ")
price2 = input("Enter the price of the second sweet: ")
price3 = input("Enter the price of the third sweet: ")
price4 = input("Enter the price of the fourth sweet: ")
price5 = input("Enter the price of the fifth sweet: ")


prices = (int(price1[:-1]), int(price2[:-1]), int(price3[:-1]), int(price4[:-1]), int(price5[:-1]))
total_price = sum(prices)
price_average = float(sum(prices) / len(prices))
max_price = max(prices)
min_price = min(prices)

print("Total Price: " + str(total_price) + "p")
print("Average Price: " + str(price_average) + "p")
print("Highest Price: " + str(max_price) + "p")
print("Lowest Price: " + str(min_price) + "p")