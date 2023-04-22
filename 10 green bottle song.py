from time import sleep
num=10
while num!=1:
    print("There are",num,"green bottles hanging on the wall, ")
    sleep(1.5)
    print(num,"green bottles hanging on the wall, ")
    sleep(1.5)
    print("and if 1 green bottle should accidentally fall")
    sleep(1.5)
    bottle=int(input("How many bottles will be hanging on the wall? "))
    num=num-1
    while bottle!=num:
        print()
        print("No,try again")
        bottle=int(input("How many bottles will be hanging on the wall? "))
    print()

while num!=0:
    print("There is",num,"green bottle hanging on the wall, ")
    sleep(1.5)
    print(num,"green bottle hanging on the wall, ")
    sleep(1.5)
    print("and if 1 green bottle should accidentally fall")
    sleep(1.5)
    bottle=int(input("How many bottles will be hanging on the wall? "))
    num=num-1
    while bottle!=num:
        print()
        print("No,try again")
        bottle=int(input("How many bottles will be hanging on the wall? "))
    print()
print("There are no more green bottles hanging on the wall")
