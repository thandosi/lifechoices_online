from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x600")
root.title("Lifechoices")
root.config(bg="black")
load = Image.open("RobinSprong_Wallpaper_Forest_French_Way_Insitus-600x600.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)


heading_label = Label(text="Welcome to Life Choices")
heading_label.place(x=50, y=100)


login_button = Button(text="Login")
login_button.place(x=150, y=200)

register_button = Button(text="Register", )
register_button.place(x=50, y=200)
admin_button = Button(text="Admin user")
admin_button.place(x=250, y=200)

def register():
    import register



root.mainloop()
