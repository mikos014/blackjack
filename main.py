from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from deck import Deck
from player import Player
from dealer import Dealer

# Start frame
root = Tk()
root.title("Blackjack")
root.geometry("960x640")


# controllers
def b_deal_on_click():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


def b_hit_on_click():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


def b_stand_on_click():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


# UI
def show_player_cards():
    #     get card
    #     show in player's area
    pass


def show_dealer_cards():
    #   get card
    #   show in dealer's area
    pass


# UX
#   set buttons
bg_image = ImageTk.PhotoImage(Image.open("assets/background.jpg"))
bg_label = Label(image=bg_image)
bg_label.place(x=0, y=0)
b_deal = Button(text="DEAL", command=b_deal_on_click, width=12, height=2)
b_deal.place(x=300, y=560)
b_hit = Button(text="HIT", command=b_hit_on_click, width=12, height=2)
b_hit.place(x=420, y=560)
b_stand = Button(text="STAND", command=b_stand_on_click, width=12, height=2)
b_stand.place(x=540, y=560)


#   cards
deck_of_cards = Deck()
deck_of_cards.shuffle()

#       player's card1
player = Player()
player_card = deck_of_cards.get_card()
player.set_card(player_card)

i_card1 = Image.open(player_card.get_path()).resize((102, 150), Image.ANTIALIAS)
iTK_card1 = ImageTk.PhotoImage(i_card1)
l_card1 = Label(image=iTK_card1).place(x=300, y=330)

#       dealer's card1
dealer = Dealer()
dealer_card = deck_of_cards.get_card()
dealer.set_card(dealer_card)

i_card2 = Image.open(dealer_card.get_path()).resize((102, 150), Image.ANTIALIAS)
iTK_card2 = ImageTk.PhotoImage(i_card2)
l_card2 = Label(image=iTK_card2).place(x=300, y=30)

#       player's card2
player_card = deck_of_cards.get_card()
player.set_card(player_card)

i_card3 = Image.open(player_card.get_path()).resize((102, 150), Image.ANTIALIAS)
iTK_card3 = ImageTk.PhotoImage(i_card3)
l_card3 = Label(image=iTK_card3).place(x=420, y=330)

#       dealer's card2
dealer_card = deck_of_cards.get_card()
dealer.set_card(dealer_card)

i_card4 = Image.open(dealer_card.get_path()).resize((102, 150), Image.ANTIALIAS)
iTK_card4 = ImageTk.PhotoImage(i_card4)
l_card4 = Label(image=iTK_card4).place(x=420, y=30)

#   dealer score
dealer_score = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="Dealer = " + str(dealer.count_points()))
dealer_score.place(x=200, y=205)

#   score info
text_score = Label(root, height=2, width=10, bg="yellow", fg="black", text="Points:")
text_score.place(x=200, y=240)

#   player score
player_score = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="You = " + str(player.count_points()))
player_score.place(x=200, y=270)

# TODO next cards for player
# i_spadesK = Image.open("assets/spades/king.png").resize((102, 150), Image.ANTIALIAS)
# iTK_spadesK = ImageTk.PhotoImage(i_spadesK)
# spadesK = Label(image=iTK_spadesK).place(x=540, y=330)
#
# i_spadesAce = Image.open("assets/spades/ace.png").resize((102, 150), Image.ANTIALIAS)
# iTK_spadesAce = ImageTk.PhotoImage(i_spadesAce)
# spadesAce = Label(image=iTK_spadesAce).place(x=660, y=330)

root.mainloop()
