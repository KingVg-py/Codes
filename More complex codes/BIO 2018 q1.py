debt = 100
interest=int(input("Enter the interest value: "))
repayment=int(input("Enter the repayment value: "))
repay_multi=repayment/100
interest_multi=interest/100
repay_val=0
money_paid=0
while debt!=0:
    debt=debt+(interest_multi*debt)
    repay_val=debt*repay_multi
    if debt>=50:
        if repay_val>=50:
            debt=debt-repay_val
            money_paid=money_paid+repay_val
        elif repay_val<50:
            debt=debt-50
            money_paid=money_paid+50
    elif debt<50:
        money_paid=money_paid+debt
        debt=debt-debt

print (str(format(money_paid, ".2f")))
    
