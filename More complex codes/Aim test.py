from tkinter import *
from time import sleep
from random import randint

#final output section
def enterage():

    age=age_text.get(1.0, END)
    reply="Your age is "+str(age)+" ."
    ans=Tk()
    ans.title("Age")
    ans.geometry("220x50")
    ans.configure(bg="Black")
    ans1_label=Label(ans, text=str(reply), font=("", 20))
    ans1_label.configure(fg="White", bg="Black")
    ans1_label.place(x=0, y=0)



#section coding for the click the button game
def load():

    def update():
        nonlocal times
        red_button.place(x=randint(1, 285), y=randint(70, 365))
        times=times-1
        click_text.config(text="Click the button "+str(times)+" times!")
        if times==1:
             click_text.configure(text="Click it one last time!")
        elif times==0:
             click_text.configure(text="Successful!")
             sleep(0.7)
             loading.destroy()
             enterage()

    loading=Tk()
    loading.geometry("320x400")
    loading.configure(bg="Black")
    loading.title("Click slowly")
    times=20
    click_text=Label(loading, text="Click the button "+str(times)+" times!", font=("", 20))
    click_text.configure(fg="White", bg="Black")
    click_text.place(x=0, y=0)
    img=PhotoImage(master=loading, height=30, width=30)
    red_button=Button(loading, text="" ,height=1, width=2,  command=update, borderwidth=10)
    red_button.config(bg="Red")
    red_button.place(x=randint(1, 285), y=randint(70, 365))
    



root=Tk()
root.geometry("185x100")
root.title("Age Calculator")
root.configure(bg="Black")
age_label=Label(root, text="Age Calculator", font=("", 20))
age_label.configure(bg="Blue", fg="White")
age_label.place(x=0, y=0)
age_text=Text(root, width=8, height=1, font=("", 10))
age_text.place(x=100, y=66)
age_button=Button(root, text="Enter Age", font=("", 12), command=load)
age_button.configure(bg="Blue", fg="White")
age_button.place(x=10, y=60)

root.mainloop()
