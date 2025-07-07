import datetime
import datetime as dt
import os.path

import sys
arg = sys.argv
print(arg)

userdate_entry = arg[1]


if len(arg)!=2:
    sys.exit()

else:
    try:
        userdate_entry_dt = dt.datetime.strptime(userdate_entry, "%m-%d-%Y")
        day_of_the_week = userdate_entry_dt.strftime('%A')
        print(f"Day for the date:{userdate_entry} is {day_of_the_week}")

    except ValueError :
        print(f"Usage: python {os.path.basename(__file__)} MM-DD-YYYY")
