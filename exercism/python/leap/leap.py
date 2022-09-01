def leap_year(year):
    """Calculate if a year is a leap year in the Gregorian calendar.

    :param year: int - year to evaluate if it's a leap year
    :return: bool - True or False indicating if it's a leap year or not, respectively.
    """
    # evenly divisible by 4
    is_evenly_div_4 = (year % 4) == 0
    
    # not evenly divisible by 100
    is_evenly_div_100 = (year % 100) == 0

    # unless evenly divisible by 400
    is_evenly_div_400 = (year % 400) == 0

    return (is_evenly_div_4 and not is_evenly_div_100) or (is_evenly_div_4 & is_evenly_div_100 & is_evenly_div_400)


