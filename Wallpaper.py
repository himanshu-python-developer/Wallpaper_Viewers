from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
    global counter
    img_lable.config(image=img_array[counter])
    counter = counter + 1
    
counter  = 1
root = Tk()
root.title("Wallpaper")

root.geometry('400x600')
root.config(background="black")

files = os.listdir('Wallpaper')
print(files)

img_array = []
for file in files:
    img = Image.open(os.path.join('Wallpaper',file))
    resized_img = img.resize((300,500))
    img_array.append(ImageTk.PhotoImage(resized_img))

# print(img_array)
img_lable = Label(root,image=img_array[0])
img_lable.pack(padx=(17,12))

next_btn = Button(root,text='Nezt',bg='White',fg='black',width=25,height=2,command=rotate_image)
next_btn.pack()


root.mainloop()