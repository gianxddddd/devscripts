from datetime import datetime


def get12clock():
    time = datetime.strptime(datetime.now().time(), '%H:%M')
    return time.strftime('%I:%M %p')


def get24clock():
    time = datetime.now().time().strftime('%H:%M:%S')
    return time


def getdate():
    date = datetime.now().date().strftime('%D-%M-%Y')
    return date