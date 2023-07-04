from tkinter import *
from tkinter import ttk
from random import *

root = Tk()

root.geometry("500x500")

root.title("Rock-Paper-Scissors Game")

list = ["rock","paper","scissors"]

computer_choice = randint(0,2)

dialogue_selector = randint(0, 5)

computer_label = Label(root, text = "Computer's choice will go here ", width = 22, height = 3, font = ("algerian", 10))
computer_label.pack()

player_label = Label(root, text = "Your choice will go here ", width = 20, height = 3, font = ("algerian", 10))
player_label.pack()

win_responses = ["damn, you're good", "ARGH!", "you got lucky", "impressive", "how are you better", "how'd you beat me!?"]
lose_responses = ["take that!", "order up, humble pie", "i've been doing this forever", "HAH!", "I am simply better", "you cannot beat me"]
tie_responses = ["hmmm", "tough game", "good show", ".....", "a worthy opponent", "next time for"]


def spin():
    if player_select.get() == "Rock":
        player_choice = 0
    elif player_select.get() == "Paper":
        player_choice = 1
    elif player_select.get() == "Scissors":
        player_choice = 2
    computer_choice = randint(0,2)
    dialogue_selector = randint(0, 5)
    computer_label.config(text = "Computer chose " + list[computer_choice])
    player_label.config(text = "You chose " + list[player_choice])

    if player_choice == computer_choice:
        wl_label.config(text = "Tied! - Computer says: " + tie_responses[dialogue_selector])

    elif (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1) or (player_choice == 0 and computer_choice == 2):
        wl_label.config(text = "You win! - Computer says: " + win_responses[dialogue_selector])

    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
        wl_label.config(text = "You lose! - Computer says: " + lose_responses[dialogue_selector])




player_select = ttk.Combobox(root,value=["Rock","Paper","Scissors"])
player_select.current(0)
player_select.pack()

wl_label = Label(root,text="",font=("arial",10),width=50,height=4)
wl_label.pack()

button = Button(root,text="Spin!",font=("bell mt",10),command=spin)
button.pack()

root.mainloop()