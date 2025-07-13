import datetime  # imports the datetime module (not needed since you're aliasing it below)
import datetime as dt  # aliasing datetime module as 'dt' for cleaner access like dt.datetime
import os.path  # used to get current filename for usage/help message
import sys  # gives access to command-line arguments via sys.argv

arg = sys.argv  # captures command-line arguments as a list
print(arg)  # prints the list of arguments for debugging

userdate_entry = arg[1]  # takes the first argument after script name (expected to be a date)

# check if exactly 1 argument is passed (excluding script name). If not, exit silently.
if len(arg) != 2:
    sys.exit()

else:
    try:
        # try converting the input string into a datetime object using the specified format
        userdate_entry_dt = dt.datetime.strptime(userdate_entry, "%m-%d-%Y")

        # extract the full weekday name (e.g., Monday) from the datetime object
        day_of_the_week = userdate_entry_dt.strftime('%A')

        # print the result
        print(f"Day for the date: {userdate_entry} is {day_of_the_week}")

    except ValueError:
        # if parsing fails (e.g., bad format, invalid date), show proper usage message
        print(f"Usage: python {os.path.basename(__file__)} MM-DD-YYYY")
