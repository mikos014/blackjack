from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from deck import Deck
from game import Game
from player import Player
from dealer import Dealer

# Start frame
root = Tk()
root.title("Blackjack")
root.geometry("960x640")
deal_button_layout = [300, 560]
hit_button_layout = [420, 560]
stand_button_layout = [540, 560]
split_button_layout = [660, 560]

card_size = (102, 150)
card_background = 'green'
player_card_layout = [[300, 330], [420, 330], [540, 330], [660, 330], [780, 330]]
dealer_card_layout = [[300, 30], [420, 30], [540, 30], [660, 30], [780, 30]]


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
def show_player_cards():
    print("laal")
    #     get card
    #     show in player's area
    pass


def show_dealer_cards():
    #   get card
    #   show in dealer's area
    pass


def empty_func():
    pass


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

card_back_path = "assets/back.png"

#       player's cards
# player = Player()
# player_card = deck_of_cards.get_card()
# player.set_card(player_card)

card_back_i = Image.open(card_back_path).resize(card_size, Image.ANTIALIAS)
card_back_iTK = ImageTk.PhotoImage(card_back_i)
player_card_l1 = Label(image=card_back_iTK, bg=card_background).place(x=player_card_layout[0][0], y=player_card_layout[0][1])
player_card_l2 = Label(image=card_back_iTK, bg=card_background).place(x=player_card_layout[1][0], y=player_card_layout[1][1])
player_card_l3 = Label(image=card_back_iTK, bg=card_background).place(x=player_card_layout[2][0], y=player_card_layout[2][1])
player_card_l4 = Label(image=card_back_iTK, bg=card_background).place(x=player_card_layout[3][0], y=player_card_layout[3][1])
player_card_l5 = Label(image=card_back_iTK, bg=card_background).place(x=player_card_layout[4][0], y=player_card_layout[4][1])


#       dealer's card1
# dealer = Dealer()
# dealer_card = deck_of_cards.get_card()
# dealer.set_card(dealer_card)

dealer_card_l1 = Label(image=card_back_iTK, bg=card_background).place(x=dealer_card_layout[0][0], y=dealer_card_layout[0][1])
dealer_card_l2 = Label(image=card_back_iTK, bg=card_background).place(x=dealer_card_layout[1][0], y=dealer_card_layout[1][1])
dealer_card_l3 = Label(image=card_back_iTK, bg=card_background).place(x=dealer_card_layout[2][0], y=dealer_card_layout[2][1])
dealer_card_l4 = Label(image=card_back_iTK, bg=card_background).place(x=dealer_card_layout[3][0], y=dealer_card_layout[3][1])
dealer_card_l5 = Label(image=card_back_iTK, bg=card_background).place(x=dealer_card_layout[4][0], y=dealer_card_layout[4][1])

#   dealer score
dealer_score_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="Dealer = ")
dealer_score_label.place(x=200, y=205)

#   score info
text_score_label = Label(root, height=2, width=10, bg="yellow", fg="black", text="Points:")
text_score_label.place(x=200, y=240)

#   player score
player_score_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="You = ")
player_score_label.place(x=200, y=270)

#   instructions
instruction_label = Label(root, height=2, width=30, bg="darkgreen", text="Place your bets")
instruction_label.place(x=350, y=240)


def start_playing():
    game = Game(player_card_l1, player_card_l2, player_card_l3, player_card_l4, player_card_l5,
                dealer_card_l1, dealer_card_l2, dealer_card_l3, dealer_card_l4, dealer_card_l5,
                player_score_label, dealer_score_label)

    b_deal.place_forget()
    show_button(b_hit)
    show_button(b_stand)
    print("in")


print("out")
b_deal.bind('<Button-1>', lambda event: start_playing())
root.mainloop()
