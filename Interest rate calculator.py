def interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
    si = (principal * time * rate)/100
    print('The Simple Interest is', si)
    monthly_interest_rate = rate/1200
    amount_of_months = time*12
    monthly_payment = principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months))
    
    print(" The monthly payment for this loan is: %.2f " % monthly_payment)
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))

    
interest(principal,rate,time)

