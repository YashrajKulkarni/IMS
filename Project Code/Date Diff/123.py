#To calculate diff. of months between to dates for premium

from datetime import datetime
from dateutil.relativedelta import relativedelta


from dateutil.rrule import rrule, MONTHLY
from datetime import datetime

def months(start_month, start_year, end_month, end_year):
    start = datetime(start_year, start_month, 1)
    end = datetime(end_year, end_month, 1)
    return [(d.month, d.year) for d in rrule(MONTHLY, dtstart=start, until=end)]

print (months(1, 2008, 6, 2010))
#[(11, 2010), (12, 2010), (1, 2011), (2, 2011)]