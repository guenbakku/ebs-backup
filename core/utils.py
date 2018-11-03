# coding: utf-8

#
# Utility functions
#

def utc2epoch(dt):
    ''' Convert UTC datetime object to Epoch timestamp '''
    import calendar
    return calendar.timegm(dt.timetuple())

def is_int(s):
    ''' Check if a string is representing for integer or not '''
    try:
        int(s)
        return True
    except ValueError:
        return False
