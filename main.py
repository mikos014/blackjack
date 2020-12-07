from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

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


bg_image = ImageTk.PhotoImage(Image.open("assets/background.jpg"))
bg_label = Label(image=bg_image)
bg_label.place(x=0, y=0)
b_deal = Button(text="DEAL", command=b_deal_on_click, width=12, height=2)
b_deal.place(x=300, y=560)
b_hit = Button(text="HIT", command=b_hit_on_click, width=12, height=2)
b_hit.place(x=420, y=560)
b_stand = Button(text="STAND", command=b_stand_on_click, width=12, height=2)
b_stand.place(x=540, y=560)

image = Image.open("assets/spades/7.png")
image = image.resize((102, 150), Image.ANTIALIAS)
card_image = ImageTk.PhotoImage(image)
image_label = Label(image=card_image)
image_label.place(x=500, y=30)

player_score = Text(root, height=2, width=20, bg='black', fg='yellow')
player_score.place(x=20, y=20)
player_score.insert(END, "asdasdasd")

root.mainloop()
