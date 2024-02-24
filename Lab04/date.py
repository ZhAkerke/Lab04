# Example 1
from datetime import datetime, timedelta

x = datetime.now() - timedelta(days=5)
print(x.date())

# Example 2
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)

# Example 3
from datetime import datetime

cur_datetime = datetime.now()
x = cur_datetime.replace(microsecond=0)
print(x)

# Example 4
from datetime import datetime

date1 = datetime(2023, 5, 10, 12, 30, 0)
date2 = datetime(2023, 5, 15, 10, 15, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print ("The difference is:", seconds, "seconds.")