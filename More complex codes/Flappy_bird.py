from tkinter import *
from random import randint

global x_block_vals, bird_y, game_over, score
x_block_vals=500
bird_y=200
game_over=False
score=0

#creates the main images and background
root=Tk()
root.geometry("400x600")
root.config(bg="light Blue")

block_b=Label(root, text="", height=50, width=12, bg="Green", anchor="sw")
block_t=Label(root, text="", height=50, width=12, bg="Green", anchor="sw")

rand_y=randint(100, 600)

block_t.place(y=rand_y-1000)
block_b.place(y=rand_y)

score_label=Label(root, text="Score: "+str(score), font=("", 30), bg="Black", fg="White")
score_label.place(x=0, y=0)

bird=Label(root, width=4, height=2, bg="Red")
bird.place(x=20, y=bird_y)


#the different functions

def blocks_move():
    global x_block_vals, bird_y, rand_y, game_over, score
    
    if bird_y>=rand_y-35 and -70<=x_block_vals<=50:
        game_over=True
        try_again.place(x=200, y=200)
    elif bird_y<=rand_y-250 and -70<=x_block_vals<=50:
        game_over=True
        try_again.place(x=200, y=200)
    else:
        if x_block_vals>-100:
            x_block_vals-=0.3
            block_b.place_configure(x=x_block_vals)
            block_t.place_configure(x=x_block_vals)
            root.after(1, blocks_move)
        elif x_block_vals<=-100:
            score+=1
            score_label.configure(text="Score: "+str(score))
            x_block_vals=500
            rand_y=randint(100, 600)
            block_b.place(x=x_block_vals, y=rand_y)
            block_t.place(x=x_block_vals, y=rand_y-1000)
            blocks_move()

def bird_fall():
    global bird_y, gameover
    if game_over==False:
        if bird_y<=565:
            bird_y +=0.3
            bird.place_configure(y=bird_y)
            root.after(1, bird_fall)

def jump(event):
    global bird_y, game_over
    if game_over==False:
        bird_y=bird_y-60
        bird.place_configure(x=20, y=bird_y)

def reset():
    global bird_y, game_over, x_block_vals, score, rand_y
    score=0
    score_label.configure(text="Score: "+str(score))
    game_over=False
    x_block_vals=500
    bird_y=200
    bird.place(x=20, y=bird_y)
    rand_y=randint(100, 600)
    block_t.place_configure(x=x_block_vals, y=rand_y-1000)
    block_b.place_configure(x=x_block_vals, y=rand_y)
    try_again.place_forget()
    blocks_move()
    bird_fall()

try_again=Button(root, text="Try again!", font=("", 30), bg="Red", fg="White", command=reset)

blocks_move()
bird_fall()

root.bind("<Up>", jump)

root.mainloop()
