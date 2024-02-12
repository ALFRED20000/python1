print("Welcome to Asanka Hotel")

                                    # To ask users to enter the amount charge for food
try:
    totalfoodpurchased = float(input(" Enter the amount of your food charge: "))
except ValueError:
    print("Invalid Input: Please Input Amount in numeric values")
    exit()
                                    # To calculate 18 percent tip on food charge
tip = round(float(totalfoodpurchased * 0.18))
print(f" Tip $: {tip}")
                                    # To calculate 7 percent sales tax on food charge
tax =  round(float(int(totalfoodpurchased)/100*7))
print(f" Sales Tax $: {tax}")
                                    # To add together and dispaly  
totalPurchased = (totalfoodpurchased+ tip + tax)
print(f" Total Amount to Pay $: { totalPurchased}")