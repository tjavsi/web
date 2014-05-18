# vim: set fileencoding=utf-8:
import random, string, time


def getRandomDate(start, end):
    format = '%Y-%m-%d'
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + (random.random() * (etime - stime))
    return time.strftime(format, time.localtime(ptime))

def addRandomEvents(amount):
    event_seasons = ['Påske', 'Jule', 'Sommer', 'Nytårs', 'Forårs']
    event_types = ['druk', 'møde', 'forplantning', ' hackday']
    start_date = '2014-01-01'
    end_date = '2015-01-01'

    for x in range(0, amount):
        event_name = event_seasons[random.randint(0,len(event_seasons)-1)] + event_types[random.randint(0,len(event_types)-1)] 
        random_start_date = getRandomDate(start_date, end_date)
        random_start_time = str(random.randint(0,24)) + ":00"
        random_end_date = getRandomDate(random_start_date, end_date)
        random_end_time = str(random.randint(0,24)) + ":00"
        e = mftutor.events.models.Event(title=event_name,
                                        start_date=random_start_date,
                                        end_date=random_end_date)
        e.save()

# Add all your random generators here
addRandomEvents(10)
