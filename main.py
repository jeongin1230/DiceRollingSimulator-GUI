# Source: https://data-flair.training/blogs/dice-rolling-simulator-python/

from tkinter import *
from PIL import Image, ImageTk
import random

main_window = Tk()
main_window.geometry('400x400')
main_window.title('Roll the Dice')


BlankLine = Label(main_window, text='')
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = Label(main_window, text='Roll the Dice!', fg="white", bg="black", font="arial 20 bold")
HeadingLabel.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 and 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = Label(main_window, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)

# function activated by button
def rolling_dice():
        DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        # update image
        ImageLabel.configure(image=DiceImage)
        # keep a reference
        ImageLabel.image = DiceImage


# adding button, and command will use rolling_dice function
button = Button(main_window, text='Roll', fg='blue', command=rolling_dice, font='arial 15 bold')

# pack a widget in the parent widget
button.pack(expand=True)

main_window.mainloop()

