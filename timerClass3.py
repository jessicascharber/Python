import datetime

class startTime:
    for hourInput in range(24):
        if hourInput == 0:
            hourInput = int(input("Please enter the hour you would like to start the timer at:"))
    for minuteInput in range(60):
        if minuteInput == 0:
            minuteInput = int(input("Please enter the minute you would like to start the timer at:"))
    for secondInput in range(60):
        if secondInput == 0:
            secondInput = int(input("Please enter the second you would like to start the timer at:"))
        print("This your starting time is:", hourInput,":", minuteInput,":", secondInput)
    
class Timer:

    def __init__(self, hours, minutes, seconds):
        self._hours = []
        self._minutes = []
        self._seconds = []

    def __str__(self, val):
        self._hours.append(val)
        self._minutes.append(val)
        self._seconds.append(val)

    def next_second(self):
        val = self.__hours[+1]
        val = self.__minutes[+1]
        val = self.__seconds[+1]
        del self.__hours[+1]
        del self.__minutes[+1]
        del self.__seconds[+1]
        return val

    def prev_second(self):
        val = self.__hours[-1]
        val = self.__minutes[-1]
        val = self.__seconds[-1]
        del self.__hours[-1]
        del self.__minutes[-1]
        del self.__seconds[-1]
        return val


class CountingStack(Timer):
    def __init__(self):
        time = Timer(23, 59, 59)
        print(time)

    def get_counter(self):
        time.next_second()
        print(time)

    def pop(self):
        time.prev_second()
        print(time)

