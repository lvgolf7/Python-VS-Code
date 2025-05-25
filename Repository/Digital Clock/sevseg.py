# Creates a list with three rows to represent the seven segment digital display
def getSevSeg(number, minWidth=0):
    number = str(number).zfill(minWidth)
    rows = ["", "", ""]
    for i, numeral in enumerate(number):
        match numeral:
            case ".":
                rows[0] += " "
                rows[1] += " "
                rows[2] += "."
                continue
            case "-":
                rows[0] += "   "
                rows[1] += " _ "
                rows[2] += "   "
            case "0":
                rows[0] += " _ "
                rows[1] += "| |"
                rows[2] += "|_|"
            case "1":
                rows[0] += "   "
                rows[1] += "  |"
                rows[2] += "  |"
            case "2":
                rows[0] += " _ "
                rows[1] += " _|"
                rows[2] += "|_ "
            case "3":
                rows[0] += " _ "
                rows[1] += " _|"
                rows[2] += " _|"
            case "4":
                rows[0] += "   "
                rows[1] += "|_|"
                rows[2] += "  |"
            case "5":
                rows[0] += " _ "
                rows[1] += "|_ "
                rows[2] += " _|"
            case "6":
                rows[0] += " _ "
                rows[1] += "|_ "
                rows[2] += "|_|"
            case "7":
                rows[0] += " _ "
                rows[1] += "  |"
                rows[2] += "  |"
            case "8":
                rows[0] += " _ "
                rows[1] += "|_|"
                rows[2] += "|_|"
            case "9":
                rows[0] += " _ "
                rows[1] += "|_|"
                rows[2] += " _|"
            case "A":
                rows[0] += " _ "
                rows[1] += "|_|"
                rows[2] += "| |"
            case "P":
                rows[0] += " _ "
                rows[1] += "|_|"
                rows[2] += "|  "
            case "M":
                rows[0] += "   "
                rows[1] += "|v|"
                rows[2] += "| |"

        if i != len(number) - 1:
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "
    return "\n".join(rows)


if __name__ == "__main__":
    print("This module is meant to be imported rather than ran")
    mynumber = getSevSeg('AM', 2)
    print(mynumber)
