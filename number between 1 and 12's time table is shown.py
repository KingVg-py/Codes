num=float(input("Enter any number between 1 and 12: "))
count=0

if 1<=num<=12:
    for i in range(1,11):
        count=count+1
        print(num*count)
else:
    print("error")
