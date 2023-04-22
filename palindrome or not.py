word=""

while word!="n":
    word=input("Enter a word, and I will determine if it is a palindrome or not: ")

    reverse=""

    for x in range(len(word)-1, -1, -1):
        reverse+=word[x]

    print(f"In reverse it is {reverse}")

    if reverse==word:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")
    
    print("Enter 'n' to stop")
