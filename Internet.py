from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

int= CTk()

int.geometry("793x500")

int.resizable(0,0)
int.title("Speed Test")

canvas = CTkCanvas(master=int, width=793, height=500)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/ımage/HD1-2.png")
canvas.create_image(0, 0, image=background_image, anchor="nw",)

intbutton = CTkButton(master=int, width=150, height=60, corner_radius=16, border_color="white", border_width=2,
                      bg_color="#383839",fg_color="#FFA102",
                      hover_color="grey",
                      text=" Start 🚀",
                      text_color="white",
                    )
intbutton.place(rely=0.7, relx=0.5, anchor="center")
int1_button= CTkButton(master=int,
                       width=40, height=40, corner_radius=20, border_color="white", border_width=2,
                      bg_color="#383839",fg_color="#FFA102",
                      hover_color="grey",
                      text="İ",
                      text_color="white")





int1_button.place(anchor="center", rely=0.9, relx=0.5)
int.mainloop()