class MouseButton:
    def __init__(self, canvas,x1,y1,x2,y2,colour="#d8d8d8"):
        self.canvas=canvas
        self.normal=colour
        self.rect=canvas.create_rectangle(x1,y1,x2,y2,fill=colour,outline="black")
    def press(self):self.canvas.itemconfig(self.rect,fill="#66ff66")
    def release(self):self.canvas.itemconfig(self.rect,fill=self.normal)
class MouseView:
    def __init__(self,canvas,x=720,y=40):
        self.canvas=canvas
        self.left=MouseButton(canvas,x,y,x+30,y+60)
        self.right=MouseButton(canvas,x+30,y,x+60,y+60)
        self.middle=MouseButton(canvas,x+25,y,x+35,y+20,"#808080")
        canvas.create_text(x+30,y+75,text="Mouse")
    def press(self,button):
        if button=="left":self.left.press()
        elif button=="right":self.right.press()
        elif button=="middle":self.middle.press()
    def release(self,button):
        if button=="left":self.left.release()
        elif button=="right":self.right.release()
        elif button=="middle":self.middle.release()
