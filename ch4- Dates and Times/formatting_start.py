


from datetime import datetime

def main():

    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()
    #### Date Formatting ####
    #%y/%y - Year, %a/%A - weekday, %b/%B - month, %d - data of month

    print(now.strftime("The current year is : %Y"))
    print(now.strftime("The current weekday is : %a, %d, %B,%y"))

    # %c- locale's date and time, %x - locale's date, %X- locale's time
    print(now.strftime("locale date and time : %c"))
    print(now.strftime("locale date and time : %x"))
    print(now.strftime("locale date : %X"))

    #  Time Formatting  ##
    #  %I/%H - 12/24 Hour, %M - mintes, %S - seconf, %p -locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S%p"))
    print(now.strftime("24-hour time: %H %M"))

if __name__ == '__main__':
         main()
    
