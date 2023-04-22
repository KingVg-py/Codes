from tkinter import *

def SignUp_button1():

    def SignUp():
        details=open("Login Deatils.txt", "a+")
        details.writelines(text_user.get(1.0, END))
        details.writelines(text_pass.get(1.0, END))
        text_user.delete(1.0, END)
        text_pass.delete(1.0, END)
        details.close()

        success= Tk()
        success.geometry("350x100")
        label_success1=Label(success, text="Account created!", font=("", 30))
        label_success1.place(x=0, y=0)
        label_success2=Label(success, text="You can now log in.", font=("", 30))
        label_success2.place(x=0, y=50)


    signup = Tk()

    signup.geometry("780x300")

    label_signup=Label(signup, text="Sign up here, enter details below!", font=("", 40))
    label_signup.place(x=0,y=0)
    label_signup.configure(bg="black", fg="white")

    label_user=Label(signup, text="Username", font=("", 25))
    label_user.place(x=110,y=100)

    label_pass=Label(signup, text="Password", font=("", 25))
    label_pass.place(x=110,y=150)

    text_user=Text(signup, width=20, height=1, font=("", 20))
    text_user.place(x=270, y=110)

    text_pass=Text(signup, width=20, height=1, font=("", 20))
    text_pass.place(x=270, y=160)    

    button_signup=Button(signup, text="Sign Up", font=("", 20), command=SignUp)
    button_signup.place(x=300, y=230)


def Login_button1():

    def LogIn():

        user_1=str(text_user1.get(1.0, END))
        pass_2=str(text_pass1.get(1.0, END))
        details=[]
        details.append(user_1)
        details.append(pass_2)
        text_user1.delete(1.0, END)
        text_pass1.delete(1.0, END)

        content=open("Login Deatils.txt", "r")
        if details[0] in content:
            if details[1] in content:
                success=Tk()
                success.geometry("414x85")
                label_1=Label(success, text="Successfully Logged in!", font=("", 30))
                label_1.place(x=0, y=0)
                label_2=Label(success, text="Login Success!", font=("", 30))
                label_2.place(x=0, y=40)

            else:
                Fail=Tk()
                Fail.geometry("380x100")
                label_1=Label(Fail, text="Log in failed!", font=("", 30))
                label_1.place(x=0, y=0)
                label_2=Label(Fail, text="Wrong Password!", font=("", 30))
                label_2.place(x=0, y=47)
        else:
            Fail=Tk()
            Fail.geometry("400x85")
            label_1=Label(Fail, text="Log in failed!", font=("", 30))
            label_1.place(x=0, y=0)
            label_2=Label(Fail, text="Wrong Username or password!", font=("", 20))
            label_2.place(x=0, y=48)
            
            
               

    login = Tk()

    login.geometry("730x300")

    label_login=Label(login, text="Login here, enter details below!", font=("", 40))
    label_login.place(x=0,y=0)
    label_login.configure(bg="black", fg="white")

    label_user1=Label(login, text="Username", font=("", 25))
    label_user1.place(x=110,y=100)

    label_pass1=Label(login, text="Password", font=("", 25))
    label_pass1.place(x=110,y=150)

    text_user1=Text(login, width=20, height=1, font=("", 20))
    text_user1.place(x=270, y=110)

    text_pass1=Text(login, width=20, height=1, font=("", 20))
    text_pass1.place(x=270, y=160)

    button_login=Button(login, text="Login", font=("", 20), command=LogIn)
    button_login.place(x=300, y=230)


    


root = Tk()

root.geometry("1150x200")

label1=Label(root, text="Create account or Log in", font=("", 50))
label1.configure(bg="black", fg="white")
label1.place(x=220, y=0)

button_add=Button(root, text="Sign up", font=("", 30), command=SignUp_button1)
button_add.place(x=550, y=100)

button_login=Button(root, text="Login", font=("", 30), command=Login_button1)
button_login.place(x=400, y=100)



root.mainloop()

