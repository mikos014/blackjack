from tkinter import *
from PIL import ImageTk, Image

from game import Game
from config import *

# Start frame
root = Tk()
root.title(window_title)
root.geometry(window_geometry)

# frame = Frame(root)
# frame.pack()
#
# canvas = Canvas(frame, bg="black", width=960, height=640)
# canvas.pack()


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
player_card_l6 = Label(image=card_back_iTK, bg=card_background)
player_card_l7 = Label(image=card_back_iTK, bg=card_background)
player_card_l8 = Label(image=card_back_iTK, bg=card_background)

player_card_labels = [player_card_l1, player_card_l2, player_card_l3, player_card_l4,
                      player_card_l5, player_card_l6, player_card_l7, player_card_l8]
player_card_labels[0].place(x=player_card_layout[0][0], y=player_card_layout[0][1])
player_card_labels[1].place(x=player_card_layout[1][0], y=player_card_layout[1][1])

dealer_card_l1 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l2 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l3 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l4 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l5 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l6 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l7 = Label(image=card_back_iTK, bg=card_background)
dealer_card_l8 = Label(image=card_back_iTK, bg=card_background)

dealer_card_labels = [dealer_card_l1, dealer_card_l2, dealer_card_l3, dealer_card_l4,
                      dealer_card_l5, dealer_card_l6, dealer_card_l7, dealer_card_l8]
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
instruction_label.config(width=50, font=("Courier", 15))
instruction_label.place(x=instruction_layout[0], y=instruction_layout[1])

#   bets info
text_bets_label = Label(root, height=2, width=10, bg="yellow", fg="black", text="Bets:")
text_bets_label.place(x=text_bets_layout[0], y=text_bets_layout[1])

#   player bets
bets_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="$1")
bets_label.place(x=bets_layout[0], y=bets_layout[1])

#   dealer money
dealer_money_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="Dealer = $100")
dealer_money_label.place(x=dealer_money_layout[0], y=dealer_money_layout[1])

#   money info
text_money_label = Label(root, height=2, width=10, bg="yellow", fg="black", text="Money:")
text_money_label.place(x=text_money_layout[0], y=text_money_layout[1])

#   player money
player_money_label = Label(root, height=2, width=10, bg="darkgreen", fg="yellow", text="You = $100")
player_money_label.place(x=player_money_layout[0], y=player_money_layout[1])

#   chips
red_chip_i = Image.open(chip_path + "red.png").resize(chip_size, Image.ANTIALIAS)
red_chip_iTK = ImageTk.PhotoImage(red_chip_i)
red_chip_label = Label(image=red_chip_iTK, bg=chip_background)
red_chip_label.place(x=chip_layout[0][0], y=chip_layout[0][1])

blue_chip_i = Image.open(chip_path + "blue.png").resize(chip_size, Image.ANTIALIAS)
blue_chip_iTK = ImageTk.PhotoImage(blue_chip_i)
blue_chip_label = Label(image=blue_chip_iTK, bg=chip_background)
blue_chip_label.place(x=chip_layout[1][0], y=chip_layout[1][1])

green_chip_i = Image.open(chip_path + "green.png").resize(chip_size, Image.CUBIC)
green_chip_iTK = ImageTk.PhotoImage(green_chip_i)
green_chip_label = Label(image=green_chip_iTK, bg=chip_background)
green_chip_label.place(x=chip_layout[2][0], y=chip_layout[2][1])

bets = 1

red_chip_label.bind('<Button-1>', lambda event: set_bets(1))
blue_chip_label.bind('<Button-1>', lambda event: set_bets(2))
green_chip_label.bind('<Button-1>', lambda event: set_bets(5))


def set_bets(chosen_bets):
    bets_label.config(text="$" + str(chosen_bets))


def start_playing():
    game = Game(player_card_labels, dealer_card_labels, player_score_label, dealer_score_label, instruction_label,
                b_deal, b_hit, b_stand, player_money_label, dealer_money_label, bets_label,
                red_chip_label, blue_chip_label, green_chip_label)

    show_button(b_hit)
    show_button(b_stand)
    game.init_game()
    print("in")


print("out")
b_deal.bind('<Button-1>', lambda event: start_playing())
root.mainloop()
