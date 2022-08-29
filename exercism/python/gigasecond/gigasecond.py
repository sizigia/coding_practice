from datetime import datetime, timedelta

def add(moment):
    """Determine the moment that would
    be after a gigasecond has passed.
    
    :param moment: datetime - moment in time.
    :return: int - moment after a gigasecond has passed.

    Function that takes a moment in time and determines
    the moment that would be after a gigasecond has passed.
    """

    return moment + timedelta(seconds=1000000000)
