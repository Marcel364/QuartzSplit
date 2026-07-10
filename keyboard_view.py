class Key:
    def __init__(self,canvas,label,x,y,width,height):
        self.canvas=canvas;self.label=label
        self.rect=canvas.create_rectangle(x,y,x+width,y+height,fill="#d8d8d8",outline="black")
        self.text=canvas.create_text(x+width/2,y+height/2,text=label,font=("Helvetica",10))
    def press(self):self.canvas.itemconfig(self.rect,fill="#66ff66")
    def release(self):self.canvas.itemconfig(self.rect,fill="#d8d8d8")
class KeyboardView:
    def __init__(self,canvas):
        self.canvas=canvas;self.keys={};self._build()
    def _add(self,label,x,y,width=40,height=40):
        self.keys[label]=Key(self.canvas,label,x,y,width,height)
    def _build(self):
        x=20;y=20
        for key in ["Esc","1","2","3","4","5","6","7","8","9","0","-","=","Back"]:
            w=40
            if key=="Back":w=70
            self._add(key,x,y,w);x+=w+5
        x=20;y+=50
        for key in ["Tab","Q","W","E","R","T","Y","U","I","O","P","[","]","\\"]:
            w=40
            if key=="Tab":w=60
            self._add(key,x,y,w);x+=w+5
        x=20
        y+=50
        for key in ["Caps","A","S","D","F","G","H","J","K","L",";","'","Return"]:
            w=40
            if key=="Caps":w=70
            elif key=="Return":w=75
            self._add(key,x,y,w);x+=w+5
        x=20;y+=50
        for key in ["Shift","Z","X","C","V","B","N","M",",",".","/","Shift"]:
            for i,key in enumerate(_:=["ShiftL","Z","X","C","V","B","N","M",",",".","/","ShiftR"]):pass
        x=20;y+=50
        row=[("Ctrl",60),("⌥L",60),("⌘L",60),
            ("Space",220),("⌘R",60),("⌥R",60),
            ("←",40),("↑",40),("↓",40),("→",40)]
        for label,width in row:
            self._add(label,x,y,width)
            x+=width+5
    def press(self, key):
        if key in self.keys:self.keys[key].press()
    def release(self,key):
        if key in self.keys:self.keys[key].release()
