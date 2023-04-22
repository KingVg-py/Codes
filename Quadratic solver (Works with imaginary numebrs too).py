import math

loop="y"

while loop!="n":

    a=float(input("Enter value of a: "))
    b=float(input("Enter value of b: "))
    c=float(input("Enter value of c: "))
    d=float(input("Enter value of d: "))
    c=c-d
    min_point_x= (-b)/(2*a)
    min_point_y= (a*(min_point_x**2))+(b*min_point_x)+c


    if (b**2-(4*a*c)) == 0:

        print("The quadratic only has one solution: x =", str((-b +(math.sqrt(b**2-(4*a*c))))/(2*a)))

        if a<0:
            print("Coordinate of maximum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))
        else:
            print("Coordinate of minimum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))



    elif (b**2-(4*a*c)) > 0:

        ans1 = (-b +(math.sqrt(b**2-(4*a*c))))/(2*a)
        ans2 = (-b -(math.sqrt(b**2-(4*a*c))))/(2*a)
        print ("Determinant > 0, x =", str(ans1), "or",  str(ans2))

        if a<0:
            print("Coordinate of maximum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))
        else:
            print("Coordinate of minimum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))
        


    else:
        determinant= int((b**2-(4*a*c)))
        root= determinant*-1
        test= math.sqrt(root) ** 2 == root
        root= math.sqrt(root)

        


        if test!=357757:
            if -b % (2*a) == 0:
                if root % (2*a)== 0:
                    print ("Determinant = negative, so a complex/not real answers =", str((-b/(2*a))),"+", str(root/(2*a))+"i ,", str((-b/(2*a))),"-",str(root/(2*a))+"i")

                elif root % (2*a)!=0:
                    
                    print ("Determinant = negative, so a complex/not real answers =", str((-b/(2*a))),"+", str(root)+"i/"+str(2*a) ,",", str((-b/(2*a)),"-", str(root))+"i/"+str(2*a))
            else:
                if root % (2*a)== 0:
                    print ("Determinant = negative, so a complex/not real answers =", str(-b)+"/"+str(2*a),"+", str(root/(2*a))+"i ,", str(-b)+"/"+str(2*a),"-",str(root/(2*a))+"i")
                else:
                    print ("Determinant = negative, so a complex/not real answers =", "("+str(-b),"+",str(root)+"i)/"+str(2*a) ,",", "("+str(-b),"-",str(root)+"i)/"+str(2*a))

            
            
            
        if test==1:
            
            if -b % (2*a) == 0:
                if root % (2*a)== 0:
                    print ("Determinant = negative, so a complex/not real answers =", str((-b/(2*a))),"+", str(root/(2*a))+"i ,", str((-b/(2*a))),"-",str(root/(2*a))+"i")

                elif root % (2*a)!=0:
                    
                    print ("Determinant = negative, so a complex/not real answers =", str((-b/(2*a))),"+", str(root)+"i/"+str(2*a) ,",", str((-b/(2*a)),"-", str(root))+"i/"+str(2*a))
            else:
                if root % (2*a)== 0:
                    print ("Determinant = negative, so a complex/not real answers =", str(-b)+"/"+str(2*a),"+", str(root/(2*a))+"i ,", str(-b)+"/"+str(2*a),"-",str(root/(2*a))+"i")
                else:
                    print ("Determinant = negative, so a complex/not real answers =", "("+str(-b),"+",str(root)+"i)/"+str(2*a) ,",", "("+str(-b),"-",str(root)+"i)/"+str(2*a))



        if a<0:
            print("Coordinate of maximum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))
        else:
            print("Coordinate of minimum/turning point of the graph =", str(min_point_x)+",", str(min_point_y))
        



    loop=input("Do you want to solve another one? Y/N: ")

    loop=loop.lower()
