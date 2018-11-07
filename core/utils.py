# coding: utf-8

#
# Utility functions
#

def abspath(path=''):
    ''' Return absolute path of provided item
    If provided item is an absolute path, just return it.
    If provided item is a relative path, add absolute to front
    main.py to before it to make a completely absolute path.
    '''
    import os
    return os.path.join(basepath(), path)

def basepath():
    ''' Return base path to front main.py file '''
    import os
    back_level = 2
    base_path = os.path.abspath(__file__)
    for count in range(back_level):
        base_path = os.path.dirname(base_path)
    return base_path + os.sep

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
