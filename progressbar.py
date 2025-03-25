class progressbar:
    def __init__(self, filled:str = "#", empty_char:str = " ", total:int = 100, size:int = 50, start:int = 0, display_mode:str= "full"):
        """
        Initialize a customizable progress bar instance.
        
        Parameters:
            filled (str): Character used to represent completed progress (default: "#")
            empty_char (str): Character used to represent remaining progress (default: " ")
            total (int): Total number of steps for completion (default: 100)
            size (int): Width of the progress bar in characters (default: 50)
            start (int): Starting progress value (default: 0)
            display_mode (str): Display format option (default: "full")
                Available modes:
                - "full": Shows both progress bar and percentage (e.g., "[####    ] 50%")
                - "bar": Shows only the progress bar (e.g., "[####    ]")
                - "percent": Shows only the percentage (e.g., "50%")
        
        Raises:
            ValueError: If any of the following occur:
                - start value exceeds total
                - filled or empty_char are longer than 1 character
                - invalid display_mode is specified
                - type mismatches in parameters
        """
        
        
        
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

            if display_mode.lower() == "full":
                self._pb, self._pc = 1, 1
            elif display_mode.lower() == "bar":
                self._pb, self._pc = 1, 0
            elif display_mode.lower() == "percent":
                self._pb, self._pc = 0, 1
            else:
                raise ValueError

        except:
            raise ValueError("Type mismatch in initial values")
        self.reset()
        
    def reset(self):
        self._isStop = False
        percent = round(self._start/self._total * 100, 1)
        progress = int(percent // self._scale)
        self._progress_bar = f"\r{f"[{self._filled * progress}{self._emptyChar * (self._size - progress)}]" * (self._pb)}{f" {percent}%" * self._pc}"

    def update(self, value:int):
        if not self._isStop:
            try:
                self._spent += int(value)
                percent = round(self._spent/self._total * 100, 1)
                progress = int(percent // self._scale)
                self._progress_bar = f"\r{f"[{self._filled * progress}{self._emptyChar * (self._size - progress)}]" * (self._pb)}{f"{percent}%" * self._pc}"
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

    # Create a progress bar with "=" as the filled character and "." as the empty character
    tpb = progressbar(filled="=", empty_char=".", total=100, size=50)

    # Simulate a task that takes 100 steps
    for i in range(100):
        tpb.update(1)
        tpb.show()
        sleep(0.05)  # Simulate a shorter delay

    tpb.stop()



    # Create a smaller progress bar with a size of 20
    tpb = progressbar(filled="#", empty_char=" ", total=100, size=20)

    # Simulate a task that takes 100 steps
    for i in range(100):
        tpb.update(1)
        tpb.show()
        sleep(0.1)

    tpb.stop()



    tpb = progressbar(filled="#", empty_char=" ", total=100, size=50, start=30)

    # Simulate a task that takes 70 steps (to reach 100)
    for i in range(70):
        tpb.update(1)
        tpb.show()
        sleep(0.1)

    tpb.stop()



    # Create a progress bar for a task with only 10 steps
    tpb = progressbar(filled="#", empty_char=" ", total=10, size=20)

    # Simulate a task that takes 10 steps
    for i in range(10):
        tpb.update(1)
        tpb.show()
        sleep(0.5)  # Simulate a longer delay

    tpb.stop()



    # Create a progress bar with a block character (█) as the filled character
    tpb = progressbar(filled="█", empty_char="░", total=100, size=40)

    # Simulate a task that takes 100 steps
    for i in range(100):
        tpb.update(1)
        tpb.show()
        sleep(0.05)

    tpb.stop()


    # Simulate downloading a 10 MB file in 1 MB chunks
    file_size_mb = 10
    chunk_size_mb = 1

    # Create a progress bar with a total of 10 steps (1 step per MB)
    tpb = progressbar(filled="#", empty_char=" ", total=file_size_mb, size=30)

    print("Downloading file...")
    for i in range(file_size_mb):
        tpb.update(chunk_size_mb)
        tpb.show()
        sleep(1)  # Simulate download time

    tpb.stop()
    print("Download complete!")



    # Simulate downloading 3 files
    num_files = 3
    file_size_mb = 10
    chunk_size_mb = 1

    for file_num in range(1, num_files + 1):
        print(f"Downloading file {file_num}...")
        tpb = progressbar(filled="#", empty_char=" ", total=file_size_mb, size=30)

        for i in range(file_size_mb):
            tpb.update(chunk_size_mb)
            tpb.show()
            sleep(0.5)  # Simulate download time

        tpb.stop()
        print(f"File {file_num} downloaded!\n")

    print("All files downloaded!")