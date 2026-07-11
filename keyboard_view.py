import json
from pathlib import Path
PRESSED_COLOUR="#66ff66";NORMAL_COLOUR="#d8d8d8";OUTLINE_COLOUR="black"
class Key:
    def __init__(self,canvas,x,y,w,h,data):
        self.canvas=canvas;self.code=data["code"];self.name=data["name"];self.display=data["display"]
        self.rect=canvas.create_rectangle(x,y,x+w,y+h,fill=NORMAL_COLOUR,outline=OUTLINE_COLOUR)
        align=data.get("align","center")
        if align=="left":
            anchor="w"
            tx=x+6
        elif align=="right":
            anchor="e"
            tx=x+w-6
        else:
            anchor="center"
            tx=x+w/2
        self.text=canvas.create_text(tx,y+h/2,text=self.display,anchor=anchor,font=("Helvetica",10))
    def press(self):self.canvas.itemconfig(self.rect,fill=PRESSED_COLOUR)
    def release(self):self.canvas.itemconfig(self.rect,fill=NORMAL_COLOUR)
class KeyboardView:
    def __init__(self,canvas,layout_file="assets/keyboard.json"):
        self.canvas=canvas;self.keys={};BASE_DIR=Path(__file__).resolve().parent;path=BASE_DIR/layout_file
        with path.open(encoding="utf-8") as f:layout=json.load(f)
        defaults=layout["defaults"]
        key_width=defaults["width"];key_height=defaults["height"]
        gap=defaults["gap"];left=defaults["left"];top=defaults["top"];y=top
        for row in layout["rows"]:
            x=left
            for key in row:
                width=key.get("width",key_width)
                k = Key(canvas=self.canvas,x=x,y=y,w=width,h=key_height,data=key)
                self.keys[k.code]=k
                x+=width+gap
            y+=key_height+gap
    def press(self,keycode):
        key=self.keys.get(keycode)
        if key is not None:key.press()
    def release(self,keycode):
        key=self.keys.get(keycode)
        if key is not None:key.release()
    def clear(self):
        for key in self.keys.values():key.release()
