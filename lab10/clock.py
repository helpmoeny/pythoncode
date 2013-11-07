import clock
class Time(object):
    '''Creates Time'''
    def __init__(self, hours = 24, minutes = 00, seconds = 00):
        '''Construct and initialize a refernce to the current time'''
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        '''Format for time'''
        if self._minutes <10 or self._seconds <10:
            string="Class Time: {}:0{}:0{}".format(self._hours,self._minutes,self._seconds)
        else:
            string="Class Time: {}:{}:{}".format(self._hours,self._minutes,self._seconds)
        return string

    def __str__(self):
        '''Return's string with format “hh:mm:ss” which will be used to display a human-readable representation of time'''
        return "{}:0{}:0{}".format(self._hours,self._minutes,self._seconds)

    def from_str(self,time_str):
        '''Updates Time with given string parameters'''
        self._hours = int(time_str[0:2])
        self._minutes = int(time_str[3:5])
        print(time_str)
        self._seconds = int(time_str[-2:])
        if self._minutes <10 or self._seconds <10:
            string="Class Time: {}:0{}:0{}".format(self._hours,self._minutes,self._seconds)
        else:
            string="Class Time: {}:{}:{}".format(self._hours,self._minutes,self._seconds)
        print(string)
