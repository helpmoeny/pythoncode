import clock
class Time:
    '''Creates Time'''
    def __init__(self, hours = 24, minutes = 00, seconds = 00):
        '''Construct and initialize a refernce to the current time'''
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __repr__(self):
        '''Format for time'''
        if self._minutes <10 or self._seconds <10:
            string="Class Time: {}-0{}-0{}".format(self._hours,self._minutes,self._seconds)
        else:
            string="Class Time: {}-{}-{}".format(self._hours,self._minutes,self._seconds)
        return string

    def __str__(self):
        '''Return's string with format “hh:mm:ss” which will be used to display a human-readable representation of time'''
        return "{}-0{}-0{}".format(self._hours,self._minutes,self._seconds)

    def from_str():
        '''Updates Time with given string parameters'''
        #self._time=time
        time=input("Input new time(hh,mm,ss): ")
        hours = int(time[0:2])
        minutes = int(time[3:5])
        print(time)
        seconds = int(time[-2:])
        if minutes <10 or seconds <10:
            string="Class Time: {}-0{}-0{}".format(hours,minutes,seconds)
        else:
            string="Class Time: {}-{}-{}".format(hours,minutes,seconds)
        print(string)
