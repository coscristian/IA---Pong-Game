import tkinter as tk

class Window(tk.Tk):
    def __init__(self, *args):
        if len(args) == 2:    
            super().__init__()
            self.geometry(args[0])
            self.title(args[1])
            self.resizable(False, False)
            self.__canvas = tk.Canvas(self, bg= 'black', height=600, width=600)
            self.__canvas.pack()
    
    def getCanvas(self):
        return self.__canvas

    def start_execution(self):
        self.mainloop()
        
        