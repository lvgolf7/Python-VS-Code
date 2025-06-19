# Text calendar
This is a text output calendar.  Used string functions to build calendar and one big string.
You can output that string to file or printer.

Uses the holiday library to get the list of holidays.  Need to pip install the holiday library, there is an error catch at beginning if not installed.
https://pypi.org/project/holidays/

There is not enough space in the calendar cell for holiday name.
I made a list to hold holiday date and name for printing after the calendar printed.  