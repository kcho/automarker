import cv2


imgLoc = '/Users/admin/Dropbox/Knowledges/python/opencv/orig.jpg'
img = cv2.imread(imgLoc)

yesBlank = img[1500:1600, 2085:2270]
yesFilled=img[1900:2000, 2085:2270]
noFilled = img[1500:1600, 1900:2085]
noBlank=img[1900:2000, 1900:2085]


for i in [yesBlank, yesFilled, noFilled, noBlank]:
    print i.mean()





import Tkinter
from PIL import Image, ImageTk
from sys import argv

window = Tkinter.Tk(className="bla")

image = Image.open(argv[1] if len(argv) >= 2 else imgLoc)

canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    print "clicked at: ", event.x, event.y

canvas.bind("<Button-1>", callback)
Tkinter.mainloop()
