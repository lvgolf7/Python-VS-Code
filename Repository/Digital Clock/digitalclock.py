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
        hours = str(currentTime.tm_hour % 12)
        if hours == "0":
            hours = "12"
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)
        am_pm = strftime("%p")

        hDigits = sevseg.getSevSeg(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSeg(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSeg(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        apDigits = sevseg.getSevSeg(am_pm[0], 1)
        apTopRow, apMiddleRow, apBottomRow = apDigits.splitlines()

        print(hTopRow + "   " + mTopRow + "   " + sTopRow + "  " + apTopRow)
        print(hMiddleRow + " * " + mMiddleRow + " * " + sMiddleRow + "  " + apMiddleRow)
        print(hBottomRow + " * " + mBottomRow + " * " + sBottomRow + "  " + apBottomRow)
        print()
        print("Press Ctrl+C to quit")

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print("Digital Clock")
    sys.exit()
