class Time(object):
    '''Creates Time'''
    def __init__(self, hours = 24, minutes = 00, seconds = 00):
        """ Construct the Time using three integers. """
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        """ Return a string as the formal representation a Time. """
        string="Class Time: {:02d}:{:02d}:{:02d}".format(self._hours,self._minutes,self._seconds)
        return string

    def __str__(self):
        """ Return a string (mm/dd/yyyy) to represent a Time. """
        string="{:02d}:{:02d}:{:02d}".format(self._hours,self._minutes,self._seconds)
        return string

    def from_str(self,time_str):
        '''Updates Time with given string parameters'''
        hours, minutes, seconds = [ int( n ) for n in time_str.split( ':' )]
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        print(time_str)
