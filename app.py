from tkinter import Tk, Frame, Button, Canvas, NW, N, S, E, W, PhotoImage, TOP, BOTTOM, LEFT, RIGHT
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image

class ImageEncApp:
    def __init__(self, master):
        self.master = master
        master.title("Encryption")
        self.create_basic_layout()

    def create_basic_layout(self):
        self.menuFrame = Frame(self.master)
        self.menuFrame.pack(side=LEFT)

        self.canvasFrame = Frame(self.master)
        self.canvasFrame.pack(side=RIGHT)

        self.canvas = Canvas(self.canvasFrame,width = 500, height = 500, bg="white")
        self.canvas.pack(side=LEFT)

        self.uploadButton = Button(self.menuFrame, text="Upload", command=self.openImage)
        self.uploadButton.pack(side=TOP)

    def openImage(self):
        self.filePath = askopenfile()#"1.jpeg"
        
        self.img = ImageTk.PhotoImage(Image.open(self.filePath.name))
        self.canvas['width']=self.img.width()+20
        self.canvas['height']=self.img.height()+20    

        self.canvas.create_image(15, 15, image=self.img, anchor=NW)
                

root=Tk()
# root.state('zoomed')
win = ImageEncApp(root)
root.mainloop()