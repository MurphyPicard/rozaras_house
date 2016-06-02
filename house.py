print
print
print "ROZARA\'S HOUSE"
print
print "It has to have 3+ bedrooms and 2+ bathrooms"
print "and it must be in a wonderful neighborhood."
print
print "A house payment calculator... please use the examples as a guide."
print
house_price = float(raw_input("What is the house price? (example 200000): "))
interest_rate = float(raw_input("What is the interest rate (example .035): "))
down_payment = float(raw_input("What is the down payment (example 25000): "))
mortgage = float(house_price) - float(down_payment)

principal_monthly = mortgage/600
interest_monthly = mortgage * interest_rate / 12
taxes_monthly = house_price/1000 
insurance_monthly = house_price/2000
if mortgage <= house_price * .8:
    monthly_payment = principal_monthly + interest_monthly + taxes_monthly + insurance_monthly
else:
    monthly_payment = principal_monthly + interest_monthly + taxes_monthly + insurance_monthly + 75
print
print "Monthly printcipal: ", principal_monthly
print "Monthly interest: ", interest_monthly
print "Monthly taxes: ", taxes_monthly
print "Monthly insurance: ", insurance_monthly
print "This is how much the house sold for: $", house_price
print "This is how much we will owe initially: $", mortgage
print
print "This is the estimated monthly payment: $",monthly_payment
print
if monthly_payment >= 1700:
    print "That is way too expensive!" 
elif monthly_payment >= 1500:        
    print "That might be too expensive to afford."
else:
    print "I think we can afford this." 
if mortgage <= (house_price * .8) and monthly_payment < 1500 :
    print "Let\'s make an offer"
else:
    print "Maybe we should consider putting more money down to avoid the PMI payment."         
print
print