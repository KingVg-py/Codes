from tkinter import *

root=Tk()

class mainWindow():

    class mainButtons():
        def __init__(btns, buttons_frame, button_label, pos1, pos2, text_out):
            btns.button_text=button_label
            btns.text_out=text_out
            btns.btn=Button(buttons_frame, text=button_label, width=5, font=("", 30), command=btns.display_num)
            btns.btn.grid(column=pos2, row=pos1)

        def display_num(btns):
            btns.text_out.config(state=NORMAL)
            btns.operators=["/", "*", "-", "+"]
            btns.equation=btns.text_out.get("1.0", "end-1c")
            btns.allow_it=True

            if len(btns.equation)==0:
                for x in btns.operators:
                    if btns.button_text==x:
                        btns.allow_it=False
                        break

            elif len(btns.equation)>0 and (btns.button_text=="/" or btns.button_text=="*" or btns.button_text=="+" or btns.button_text=="-"):
                for x in btns.operators:
                    if btns.equation[len(btns.equation)-1] == x:
                        btns.allow_it=False

            elif btns.button_text=="C":
                btns.allow_it=False
                btns.text_out.delete(1.0, END)
                        

            if btns.allow_it==True:
                btns.text_out.insert(END, btns.button_text)
                
            btns.text_out.config(state=DISABLED)
            

    def equals(self):
        self.text_out.config(state=NORMAL)
        self.equation=self.text_out.get("1.0", "end-1c")
        self.operators=["/", "*", "-", "+"]
        self.no_end_operator=True

        if len(self.equation)>0:
            for x in self.operators:
                if self.equation[len(self.equation)-1] == x:
                    self.no_end_operator=False
                    break

        if self.no_end_operator and len(self.equation)>0:
            self.text_out.delete(1.0, END)
            self.text_out.insert(END, eval(self.equation))
        self.text_out.config(state=DISABLED)

    def __init__(self, mainFrame):
        mainFrame.geometry("600x600")
        self.btn_list=[["7", "8", "9", "+"],
                       ["4", "5", "6", "-"],
                       ["1", "2", "3", "*"],
                       [".", "0", "C", "/"]]
        
        self.text_out=Text(mainFrame, font=("", 30), width=27, height=3, state=DISABLED)
        self.text_out.grid(column=0, row=0)
        self.buttons_frame=Frame(mainFrame, width=600, height=400)
        self.buttons_frame.grid(column=0, row=1)
        for x in range(4):
            for y in range(4):
                self.mainButtons(self.buttons_frame, self.btn_list[x][y], x, y, self.text_out)

        self.equal_sign=Button(self.buttons_frame, text="=", width=5, font=("", 30), command=self.equals)
        self.equal_sign.grid(column=3, row=4)

mainWindow(root)

root.mainloop()

