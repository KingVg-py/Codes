print("Welcome to book input!")
print("Answer some simple questions to create the code for the book!")
author=input("First question, what is the name of the author: ")
title=input("Second question, what is the name of the book: ")
year=input("Third question, what year was the book published in: ")
genre=input("Lastly, what is the genre of the book: ")
code=author[0]+author[1]+author[2]+year+title[0]+title[1]+title[2]+"-"+genre[0]
print("All done! here is the code: "+code)
