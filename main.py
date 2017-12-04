try:
    import tkinter as tk 
except ImportError:
    import Tkinter as tk 
import random
from os import listdir
from os.path import isfile, join

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.master.title("GameOfLife")
        self.master.resizable(width=False, height=False)
        self.master.bind("<Escape>",self.closeWindow)

        self.examplesPath = "examples"
        self.exampleToLoad = None

        self.inputPanelHeight = 30
        self.inputPanel = tk.Frame(self.master,width=w,height=self.inputPanelHeight,bg="white")
        self.inputPanel.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

        self.loadExamplesListButton = tk.Button(self.inputPanel,text="Load")
        self.loadExamplesListButton.bind("<Button-1>",self.loadExamplesList)
        self.loadExamplesListButton.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.master,bg="gray",width=w,height=h-self.inputPanelHeight,borderwidth=5)
        self.canvas.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        self.rows = 50
        self.columns = 50
        self.cellwidth = 20
        self.cellheight = 20

        self.step = 0

        #item_id of each cell
        self.cells = {}
        for column in range(self.rows):
            for row in range(self.columns):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.cells[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="light grey", tags="rect")

        #cells that are alive at time t.
        self.alive = {}

    def loadExamplesList(self,event):
        tlwidth = 200
        bheight = 30
        topLevel = tk.Toplevel()
        topLevel.title("Load Examples")
        topLevel.resizable(0,0)
        padx = 10
        topLevel.geometry('%dx%d+%d+%d' % (tlwidth,h,x-tlwidth-padx,y))
        
        tk.Label(topLevel,text="Choose an example to load:").pack(side=tk.TOP,anchor="w")

        exlist = [f for f in listdir(self.examplesPath) if isfile(join(self.examplesPath,f))]
        listBox = tk.Listbox(topLevel,width=tlwidth,height=37)
        for ex in exlist:
            listBox.insert(tk.END,ex)
        listBox.selection_set(0,0)
        listBox.pack(side=tk.TOP,fill=tk.BOTH)
        def choose(event):
            try:
                self.exampleToLoad = listBox.get(listBox.curselection())
            except: 
                print("coucou")
            print(self.exampleToLoad)
        listBox.bind("<Double-Button-1>",choose)

        chooseButton = tk.Button(topLevel,text="Choose",width=tlwidth,height=8)
        chooseButton.bind("<Button-1>",choose)
        def closeTopLevel(event):
            topLevel.destroy()
        cancelButton = tk.Button(topLevel,text="Cancel",width=tlwidth,height=bheight)
        cancelButton.bind("<Button-1>",closeTopLevel)

        chooseButton.pack(side=tk.TOP)
        #cancelButton.pack(side=tk.TOP,fill=tk.BOTH)



    """
    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="blue")
        self.canvas.itemconfig("oval", fill="blue")
        for i in range(10):
            row = random.randint(0,19)
            col = random.randint(0,19)
            item_id = self.oval[row,col]
            self.canvas.itemconfig(item_id, fill="green")
        self.canvas.after(delay, lambda: self.redraw(delay))
    """

    def closeWindow(self,event):
        self.master.destroy()



root = tk.Tk()
w = 800
h = 650
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
gameoflife = GameOfLife(root)
root.mainloop()