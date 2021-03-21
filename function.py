import datetime
from datetime import date
from datetime import datetime


def time_alive():

    '''function to find out how many days I have been alive'''
    d = datetime.now()
    only_date = d.date()
    born = date(1978,2,20)
    today = only_date
    delta = today - born
    
    # ninty = 32850
    # days_till_90 = ninty - delta
    #return delta.days
    return f"<html><body><h1>Congratulations, Liz! You have been alive for {delta.days} days!</h1></body></html>"
    #print(f"If you live until 90, you have {days_till_90.days} days to live.")
