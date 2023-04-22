alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
encrypt=[]
remove_alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n=int(input("Enter the number: "))
n=n-1
w=input("Enter word to be encrypted: ")
encrypt_word=""
letters=""
n_extra=n
for x in range(26):
    if 25-x==0:
        n_extra=0
    elif n_extra>(25-x):
        if n_extra%25-x==0:
            n_extra=0
        elif (n_extra%(25-x))-1<0:
            n_extra=n%(25-x)
        else:
            n_extra=(n%(25-x))-1
        
    encrypt.append(remove_alphabet[n_extra])
    remove_alphabet.pop(n_extra)
    n_extra=n_extra+n
start=-1
for y in w:
    start=start+1
    index_alphabet=alphabet.index(y)+start
    encrypt_word=str(encrypt_word+encrypt[index_alphabet])

for z in range(6):
    letters=str(letters+encrypt[z])
print (letters)
    
print(encrypt_word)
    

    
        
        
