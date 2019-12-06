from datetime import datetime
from datetime import date
import calendar
import sys

#noel = datetime(2019,12,25)
#now = date.today()

def show_noel(date_arg=""):
    noel = datetime(2019,12,25)
    #now = date.today()
    date = datetime.strptime(date_arg, '%Y-%m-%d')
    jours = (noel - date)
    print(jours)

if __name__ == "__main__":
    print(show_noel(sys.argv))
    








