# testing weekly task 5
# Author : Michelle O'Connor

# Yes, unfortunately today is a weekday.
# It is the weekend, yay!

import datetime
# import calendar - not needed

# define weekday
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

now = datetime.datetime.today().strftime("%A")
if now in weekday:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")


# https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html


