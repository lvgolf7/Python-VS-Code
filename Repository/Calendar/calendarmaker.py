import datetime
import sys

try:
    import holidays
except ImportError:
    print("This program requires the holiday library, which you")
    print("can install by following the instructions at")
    print("https://pypi.org/project/holidays/")
    sys.exit()


MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

print("Calendar Maker")

while True:
    print("Enter the year for the calendar: ")
    response = input(">")
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print("Please enter a numeric year, like 2025.")
    continue
while True:
    print("Enter the month for the calendar (1-12): ")
    response = input(">")

    if not response.isdecimal():
        print("Please enter a numeric month, like 5 for May.")
        continue
    month = int(response)
    if 1 <= month <= 12:
        break
    print("Please enter a number from 1 to 12.")


def getCalendarFor(year, month):
    calText = ""
    holidayList = []
    holidayCounter = 0
    calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"
    calText += "...Sunday.....Monday....Tuesday....Wednesday...Thursday...Friday....Saturday..\n"
    weekSeparator = ("+----------" * 7) + "+\n"
    blankRow = ("|          " * 7) + "|\n"
    currentDate = datetime.date(year, month, 1)
    # Get the last Sunday from previous month if needed
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    # create each week
    while True:
        calText += weekSeparator
        dayNumberRow = ""
        holidayRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            if currentDate in holidays.US():
                holidayRow += "| Holiday  "
                holidayList.append(
                    str(currentDate.month)
                    + "-"
                    + str(currentDate.day)
                    + " \t"
                    + holidays.US().get(currentDate)
                )
                holidayCounter += 1
            else:
                holidayRow += "|          "
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += "|\n"
        holidayRow += "|\n"
        calText += dayNumberRow
        calText += holidayRow
        for i in range(3):
            calText += blankRow
        if currentDate.month != month:
            break
    calText += weekSeparator
    calText += "Holidays:\n"
    if len(holidayList) == 0:
        calText += "NO Holidays\n"
    else:
        calText += "Date \tHoliday Name\n"
        for i in range(len(holidayList)):
            calText += str(holidayList[i]) + "\n"
    return calText


calText = getCalendarFor(year, month)
print(calText)
