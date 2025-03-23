class progressbar:
    def __init__(self, filled:str = "#", empty_char:str = " ", total:int = 100, size:int = 50, start:int = 0):
        try:
            if start > total or len(filled) > 1 or len(empty_char) > 1:
                raise ValueError
            self._filled = str(filled)
            self._emptyChar = str(empty_char)
            self._total = int(total)
            self._start = int(start)
            self._spent = 0
            self._size = int(size)
            self._progress_bar = ""
            self._scale = round(100 / self._size, 3)
            self._isStop = False
            self.reset()
        except:
            raise ValueError("Type mismatch in initial values")
        
    def reset(self):
        self._isStop = False
        percent = round(self._start/self._total * 100, 1)
        progress = int(percent // self._scale)
        self._progress_bar = f"\r[{self._filled * progress}{self._emptyChar * (self._size - progress)}] {percent}%"

    def update(self, value:int):
        if not self._isStop:
            try:
                self._spent += int(value)
                percent = round(self._spent/self._total * 100, 1)
                progress = int(percent // self._scale)
                self._progress_bar = f"\r[{self._filled * progress}{self._emptyChar * (self._size - progress)}] {percent}%"
            except:
                raise ValueError(f"Type mismatch for Value parameter, int expected but {type(value)} given")
        else:
            print("This progress bar has stopped")

    def show(self):
        print(self._progress_bar, end="")
        
    def stop(self):
        self._isStop = True
        print(end="\n")


if __name__ == "__main__":
    from time import sleep
    tpb = progressbar()
    for i in range(100):
        tpb.update(1)
        tpb.show()

        sleep(0.1)
    tpb.stop()

    tpb = progressbar("-", total=100, size=63)
    for i in range(100):
        tpb.update(1)
        tpb.show()

        sleep(0.1)
    tpb.stop()

    tpb = progressbar("-", total=10)
    for i in range(10):
        tpb.update(1)
        tpb.show()

        sleep(0.1)
    tpb.stop()

    tpb = progressbar(filled="=", empty_char="-", total=50)
    for i in range(50):
        tpb.update(1)
        tpb.show()

        sleep(0.1)
    tpb.stop()
        