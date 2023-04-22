from tkinter import *

def print_menu():
    def add_print(): 
        with open(file_name, "a") as f:
            f.writelines("\nprint('"+str(print_text.get("1.0", "end-1c"))+"')")
        print_text.delete("1.0", END)

    print_label=Label(root, text="Write here what you want to print?", font=("", 20))
    print_label.place(x=10, y=10)

    print_add_btn=Button(root, text="Add", font=("", 30), command=add_print)
    print_add_btn.place(x=200, y=400)

    print_text=Text(root, height=1, width=30, font=("", 30))
    print_text.place(x=0, y=150)

    print_choice.place_forget()

def input_menu():
    def add_input(): 
        with open(file_name, "a") as f:
            f.writelines("\nprint('"+str(print_text.get("1.0", "end-1c"))+"')")

    print_label=Label(root, text="Write here what you want to print?", font=("", 20))
    print_label.place(x=10, y=10)

    print_add_btn=Button(root, text="Add", font=("", 30), command=add_print)
    print_add_btn.place(x=200, y=400)

    print_text=Text(root, height=1, width=30, font=("", 30))
    print_text.place(x=0, y=150)

    print_back_btn.place(x=10, y=200)

def print_back():

    print_label.place_forget()
    print_add_btn.place_forget()
    print_text.place_forget()
    print_back_btn.place_forget()

    print_choice.place(x=10, y=10)

def add_tkinter():
    with open(file_name, "a") as f:
        f.writelines("\nfrom tkinter import *")
    tkinter_choice_btn.place_forget()


def add_sleep_header():
    with open(file_name, "a") as f:
        f.writelines("\nfrom time import sleep")
    sleep_choice_btn.place_forget()

def add_randint_header():
    with open(file_name, "a") as f:
        f.writelines("\nfrom random import randint")
    randint_choice_btn.place_forget()

def adding_header():
    modules_include_label_ask.place(x=10, y=10)
    tkinter_choice_btn.place(x=10, y=70)
    randint_choice_btn.place(x=10, y=140)
    sleep_choice_btn.place(x=10, y=210)
    after_header_btn.place(x=100, y=300)
    
def after_headers():
    modules_include_label_ask.place_forget()
    tkinter_choice_btn.place_forget()
    randint_choice_btn.place_forget()
    sleep_choice_btn.place_forget()
    after_header_btn.place_forget()

    print_choice.place(x=10, y=10)

def submit_file_name():
    global file_name
    file_name=(file_name_text.get(1.0, END).strip())+".txt"
    project_file=open(file_name, "w")
    project_file.close()
    ask_name_for_file.place_forget()
    file_name_text.place_forget()
    file_name_submit_btn.place_forget()

    adding_header()


root=Tk()
root.geometry("700x600")
root.config(bg="Light Blue")

ask_name_for_file=Label(root, text="What should the file name be?", font=("", 30))
ask_name_for_file.place(x=10, y=10)

file_name_text=Text(root, height=5, width=30, font=("", 30))
file_name_text.place(x=10, y=70)

file_name_submit_btn=Button(root, text="Submit", font=("", 30), command=submit_file_name)
file_name_submit_btn.place(x=300, y=500)

modules_include_label_ask=Label(root, text="What modules do you want to include?", font=("", 30))


tkinter_choice_btn=Button(root, text="Add tkinter library",  font=("", 20), command=add_tkinter)
randint_choice_btn=Button(root, text="Add random integer library",  font=("", 20), command=add_randint_header)
sleep_choice_btn=Button(root, text="Add sleep library",  font=("", 20), command=add_sleep_header)

after_header_btn=Button(root, text="next", command=after_headers, font=("", 30))

#print labels
print_choice=Button(root, text="Print", font=("", 20), command=print_menu)
print_back_btn=Button(root, text="Back", font=("", 30), command=print_back)


root.mainloop()
