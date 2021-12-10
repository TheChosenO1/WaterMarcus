from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
window = Tk()
window.title("WaterMarcus")

def OpenFile():
    global E1
    global E2
    
    f_types = [('JPG Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    image = Image.open(filename)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    text = E1.get()
    font = ImageFont.truetype("arial.ttf", 36)
    textwidth, textheight = draw.textsize(text, font)

    margin =10
    x = width-textwidth-margin
    y= height-textheight-margin
    draw.text((x, y), text, font=font, fill=(0,0,0,2))
    image.show()
    image.save((E2.get()).strip()+ ".png")


    


canvas = Canvas(window, width=600, height=100)
canvas.grid(columnspan=5, rowspan=4)


watermark = StringVar()
filename1 = StringVar()
label1 = Label(window, text="Enter The Watermark: ", anchor="e")
label1.grid(row=0, column=1, padx= 0)
E1 = Entry(window ,textvariable = watermark, width=20)
E1.grid(row=0, column=2)
label2 = Label(window, text="Enter the filename: ", anchor="w")
label2.grid(row=1, column=1)
E2 = Entry(window, textvariable=filename1, width=20)
E2.grid(column = 2 , row=1)
upload_button = Button(window, text="Upload Image", command=OpenFile, width=20)
upload_button.grid(row=2, column=1)




window.mainloop()
