
products=["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
                    
                    #To calculate total price average for all products
avg_total_price = sum(prices)/len(products)
print(f" Average Total Price is: %.2f" % avg_total_price)
                    # To calculate new prices that reduces old prices by 5%
new_price = [ price -5 for price in prices]
print(" New price : ", new_price)

                    # Calculate the total revenue generated from the products
total_revenue = sum([price * quantity for price, quantity in zip(new_price, last_week)])
print("Total revenue generated:", total_revenue)

                    # Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / 7
print("Average daily revenue generated:", average_daily_revenue)

                    # Based on the new prices, which products are less than $ 30
less_than_30 = [product for product, price in zip(products, new_price) if price < 30]
print("Products less than $30:", less_than_30)

