from tkinter import *

class Ball:
    def __init__(self):
        self.vx = 0
        self.vy = 0

        
        
    
    def start(self):
        self.v = Tk()
        self.cv = Canvas(self.v, width=600, height=600)
        self.cv.pack()
        self.ball = self.cv.create_oval(0,0,40,40,fill="black")
        self.cv.move(self.ball,280,280)
        self.cv.mainloop()

    

    def push(self,power):
        self.cv.move(self.ball,0,-int(power*10))

    def pull(self,power):
        self.cv.move(self.ball,0,int(power*10))

    def left(self,power):
        self.cv.move(self.ball,-int(power*10),0)

    def right(self,power):
        self.cv.move(self.ball,int(power*10),0)


b = Ball()
b.start()
