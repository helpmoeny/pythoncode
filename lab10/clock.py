class Time:
    '''Creates Time'''
    def __init__(self, hours = 12, minutes = 00, seconds = 00):
        '''Construct and initialize a refernce to the current time'''
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        '''Format for time'''
        print( "%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))

    def __init__(self):
        self._hours = 12
        self._minutes = 0
        self._seconds = 0

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
