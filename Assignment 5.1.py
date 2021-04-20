# Amy Schaeffer
# Calculating time it takes for an investment to double
while True:
    print("How long will it take your investment to double?")
    origional_investment = input('Original Investment: $')
    ori_inv = float(origional_investment)
    interest = input('Yearly Interest Rate: % ')
    intr = float(interest) / 100
    doubled_investment = (ori_inv * 2)
    total_funds = ori_inv
    years = 0
    while total_funds < doubled_investment:
        total_funds = total_funds + (total_funds * intr)   
        years += 1
    message = f"Your investment will double in {years} years"
    print(message)
    stay = input('Type "done" to exit, or type anything to return to prompt : ' )
    if stay == "done":
        break

