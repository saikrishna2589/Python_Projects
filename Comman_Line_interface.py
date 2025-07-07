import sys
import datetime as dt
args = sys.argv

userdate_1 = args[1]
userdate_2 = args[2]


datetime_1 = dt.datetime.strptime(userdate_1,"%Y%m%d")

datetime2=dt.datetime.strptime(userdate_2,"%Y%m%d")

difference_time = (datetime2-datetime_1).days

print(f"{difference_time} days")


