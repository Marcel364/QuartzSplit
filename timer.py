import time
class Timer:
    def __init__(self):
        self.reset()
    def start(self):
        self._start=time.perf_counter()
        self._paused_time=0
        self._pause_start=None
        self.running=True
        self.paused=False
    def pause(self):
        if self.running and not self.paused:
            self._pause_start=time.perf_counter()
            self.paused=True
    def resume(self):
        if self.running and self.paused:
            self._paused_time+=time.perf_counter()-self._pause_start
            self.paused=False
    def stop(self):
        self.running=False
        self.paused=False
    def reset(self):
        self.running=False
        self.paused=False
        self._start=None
        self._pause_start=None
        self._paused_time=0
    @property
    def elapsed(self):
        if not self.running:return 0
        now=self._pause_start if self.paused else time.perf_counter()
        return now-self._start-self._paused_time
    @property
    def formatted(self):
        e=self.elapsed
        h=int(e//3600)
        m=int(e//60%60)
        s=int(e%60)
        ms=int((e%1)*1000)
        return f"{h:02}:{m:02}:{s:02}.{ms:03}"