count=0
invite=input("Who are you going to invite: ")
count=count+1
print(invite,"has now been invited")
invlist=[invite]
ans=input("Do you want to invite someone else: ")
ans=ans.lower()
ans=ans[0]
while ans=="y":
    invite=input("Who are you going to invite: ")
    count=count+1
    invlist.append(invite)
    ans=input("Do you want to invite someone else: ")
    ans=ans.lower()
    ans=ans[0]
print("You invited",count,"people!")
for x in invlist:
    print(x, end=", ")
