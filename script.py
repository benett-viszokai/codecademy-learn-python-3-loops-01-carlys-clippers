hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Summing the total price
total_price = 0

for price in prices:
  total_price += price

# Calculating the average price (total price / price count)
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# List comprehension - make a list with each price 5 dollars lower
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculating the total revenue
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

# Calculating the daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Creating a list with cuts under 30 dollars - with list comprehension
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]

print(cuts_under_30)
