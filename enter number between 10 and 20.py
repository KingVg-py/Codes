num=int(input("Enter a value between 10 and 20"))
while num<10 and num>20:
    if num>20:
        print("Too high")
    elif num<10:
        print("Too low")
    print("try again")
    num=int(input("Enter a value between 10 and 20"))
print("Thank You")
