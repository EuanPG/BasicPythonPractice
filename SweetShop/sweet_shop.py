price1 = int(input("Enter the price of the first sweet: "))
price2 = int(input("Enter the price of the second sweet: "))
price3 = int(input("Enter the price of the third sweet: "))
price4 = int(input("Enter the price of the fourth sweet: "))
price5 = int(input("Enter the price of the fifth sweet: "))


prices = (price1, price2, price3, price4, price5)
total_price = int(sum(prices))
price_average = float(sum(prices) / len(prices))
max_price = max(prices)
min_price = min(prices)

print("Total Price: " + str(total_price) + "p")
print("Average Price: " + str(price_average) + "p")
print("Highest Price: " + str(max_price) + "p")
print("Lowest Price: " + str(min_price) + "p")
