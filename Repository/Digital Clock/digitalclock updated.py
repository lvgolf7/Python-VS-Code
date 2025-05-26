import sys
import time
from time import strftime
from os import system, name

try:
    import sevseg
except ImportError:
    print("You must have the sevseg.py file available for import")
    sys.exit()

try:
    while True:
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")
        currentTime = time.localtime()
        current_time_str = (
            strftime("%I")
            + ":"
            + strftime("%M")
            + ":"
            + strftime("%S")
            + " "
            + strftime("%p")
        )
        current_time_sev_seg = sevseg.getSevSeg(current_time_str)
        print(current_time_sev_seg)
        print()
        print("Press Ctrl+C to quit")

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print("Digital Clock")
    sys.exit()
