from timer import Timer
from ui import UI
class QuartzSplitApp:
    def __init__(self):
        self.timer=Timer()
        self.ui=UI(self.timer)
    def run(self):self.ui.run()