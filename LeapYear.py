def LeapYear( year ):
    if (year % 4 == 0):
        if (year % 100 == 0):
            return False
        return True
    return False
