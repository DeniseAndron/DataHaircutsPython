hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price = total_price + price
#average price for the cuts
average_price = total_price / len(prices)

print("This is the average price for the cuts: " + str(average_price))
#cut the average price by 5 dollars
new_prices = [new - 5 for new in prices ]

print("Here are the new prices: " + str(new_prices))

total_revenue = 0
#the total revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("The total revenue is: " + str(total_revenue))
#revenue by week
average_daily_revenue = total_revenue / 7

print("Last week revenue is: " + str(average_daily_revenue))
# cuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print("These are the cuts under 30 dollars: " + str(cuts_under_30))