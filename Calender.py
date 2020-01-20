# Basic Calendar Made With Python

import calendar
import time


def cal():
    year = int(input("Enter a year: "))
    
    def month_():
        month = int(input("Enter a month: "))
        print("\n")
        if month > 12:
            print("\nInvalid month\n")
            month_()
        else:
            c = calendar.TextCalendar(calendar.MONDAY)
            str = c.formatmonth(year, month)
            print(str)
            time.sleep(2)
            cal()


    month_()

cal()
