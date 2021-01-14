from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from game import Game
from config import *

# Start frame
root = Tk()
root.title(window_title)
root.geometry(window_geometry)

# controllers
# def b_deal_on_click():
#     messagebox.showinfo('Message', 'You clicked the Submit button!')
#
#
# def b_hit_on_click():
#     messagebox.showinfo('Message', 'You clicked the Submit button!')
#
#
# def b_stand_on_click():
#     messagebox.showinfo('Message', 'You clicked the Submit button!')


# UI

def show_button(button):
    if button["text"] == "DEAL":
        button.place(x=deal_button_layout[0], y=deal_button_layout[1])
    elif button["text"] == "HIT":
        button.place(x=hit_button_layout[0], y=hit_button_layout[1])
    elif button["text"] == "STAND":
        button.place(x=stand_button_layout[0], y=stand_button_layout[1])
    elif button["text"] == "SPLIT":
        button.place(x=split_button_layout[0], y=split_button_layout[1])


# UX
#   set buttons
bg_image = ImageTk.PhotoImage(Image.open("assets/background.jpg"))
bg_label = Label(image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

b_deal = Button(text="DEAL", width=12, height=2)
show_button(b_deal)
b_hit = Button(text="HIT", width=12, height=2)
# show_button(b_hit)
b_stand = Button(text="STAND", width=12, height=2)
# show_button(b_stand)

#   cards_layout
card_back_i = Image.open(card_path + "back.png").resize(card_size, Image.ANTIALIAS)
card_back_iTK = ImageTk.PhotoImage(card_back_i)

player_card_l1 = Label(image=card_back_iTK, bg=card_background)
player_card_l2 = Label(image=card_back_iTK, bg=card_background)
player_card_l3 = Label(image=card_back_iTK, bg=card_background)
player_card_l4 = Label(image=card_back_iTK, bg=card_background)
player_card_l5 = Label(image=card_back_iTK, bg=card_background)

player_card_labels = [player_card_l1, player_card_l2, player_card_l3, player_card_l4, player_card_l5]
player_card_labels[0].place(x=player_card_layout[0][0], y=player_card_layout[0][1])
player_card_labels[1].place(x=player_card_layout[1][0], y=player_card_layout[1][1])

dealer_card_l1 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l2 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l3 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l4 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l5 = Label(image=card_back_iTK, bg=card_background)

dealer_card_labels = [dealer_card_l1, dealer_card_l2, dealer_card_l3, dealer_card_l4, dealer_card_l5]
dealer_card_labels[0].place(x=dealer_card_layout[0][0], y=dealer_card_layout[0][1])
dealer_card_labels[1].place(x=dealer_card_layout[1][0], y=dealer_card_layout[1][1])

#   dealer score
dealer_score_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="Dealer = ")
dealer_score_label.place(x=dealer_score_layout[0], y=dealer_score_layout[1])

#   score info
text_score_label = Label(root, height=2, width=10, bg="yellow", fg="black", text="Points:")
text_score_label.place(x=text_score_layout[0], y=text_score_layout[1])

#   player score
player_score_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="You = ")
player_score_label.place(x=player_score_layout[0], y=player_score_layout[1])

#   instructions
instruction_label = Label(root, height=2, width=30, bg="darkgreen", fg="white", text="Place your bets")
instruction_label.config(width=40, font=("Courier", 15))
instruction_label.place(x=instruction_layout[0], y=instruction_layout[1])


def start_playing():
    game = Game(player_card_labels, dealer_card_labels, player_score_label, dealer_score_label, instruction_label,
                b_deal, b_hit, b_stand)

    # b_deal.place_forget()
    show_button(b_hit)
    show_button(b_stand)
    game.init_game()
    print("in")


print("out")
b_deal.bind('<Button-1>', lambda event: start_playing())
root.mainloop()
