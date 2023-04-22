num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
total=num1+num2
ans=input("Do you want to add another number: ")
ans=ans.lower()
ans=ans[0]
while ans == "y":
    extra=int(input("Enter a number: "))
    total=total+extra
    ans=input("Do you want to add another number (enter 'y' for yes): ")
print("The total is",total)
