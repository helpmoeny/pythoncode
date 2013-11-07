class Time:
    '''Creates Time'''
    def __init__(self, hours = 12, minutes = 00, seconds = 00):
        '''Construct and initialize a refernce to the current time'''
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        '''Format for time'''
        time=print( "%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))
        return str(time)

    def __str__(self):
        '''Return's string with format “hh:mm:ss” which will be used to display a human-readable representation of time'''
        return(self)
    
    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def show(self):
        print( "%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))

    def setTime(self, hours = 12, minutes = 34, seconds = 2):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
