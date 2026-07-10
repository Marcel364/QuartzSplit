from tkinter import *
from constants import *
from keyboard_view import KeyboardView
from mouse_view import MouseView
class UI:
    def __init__(self,timer):
        self.timer=timer
        self.root=Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BACKGROUND)
        self.root.resizable(False,False)
        self.time_label=Label(self.root,text="00:00:00.000",font=TIMER_FONT,fg=TIMER_COLOUR,bg=BACKGROUND)
        self.time_label.pack(pady=(15,10))
        button_frame=Frame(self.root,bg=BACKGROUND);button_frame.pack()
        Button(button_frame,text="Start",width=10,command=self.start).pack(side=LEFT,padx=5)
        self.pause_button=Button(button_frame,text="Pause",width=10,command=self.pause)
        self.pause_button.pack(side=LEFT,padx=5)
        Button(button_frame,text="Stop",width=10,command=self.stop).pack(side=LEFT,padx=5)
        self.canvas=Canvas(self.root,width=WINDOW_WIDTH-20,height=250,bg="white",highlightthickness=1)
        self.canvas.pack(pady=15)
        self.keyboard=KeyboardView(self.canvas)
        self.mouse=MouseView(self.canvas)
        self.update()
    def start(self):
        self.timer.start()
        self.pause_button.config(text="Pause")
    def pause(self):
        if not self.timer.running:return
        if self.timer.paused:
            self.timer.resume()
            self.pause_button.config(text="Pause")
        else:
            self.timer.pause()
            self.pause_button.config(text="Resume")
    def stop(self):
        self.timer.stop()
        self.pause_button.config(text="Pause")
    def update(self):
        self.time_label.config(text=self.timer.formatted)
        self.root.after(int(1000/FPS),self.update)
    def run(self):self.root.mainloop()
