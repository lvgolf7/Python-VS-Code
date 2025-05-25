The sevseg.py file is meant to be imported by other programs to 
use for digital type display.
The function requires two inputs, the number and the width.  
If you enter sevseg.getSevSeg(73,3), you will get 073 in seven segment.
The display is padded with zeros.
The return is a list with three rows.
Uses match/case instead of if/elif for cleaner code.
See Digital Clock file to see how the three rows can be manipulated. 
