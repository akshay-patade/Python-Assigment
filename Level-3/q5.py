
class Time:


    def __init__(self, hour = 0, minute = 0):
        self.hour = hour
        self.minute = minute
    

    def addTime(self,  t2: 'Time') -> None:
        newTime = Time()
        additionalHour = True if (self.minute + t2.minute) >= 60 else False

        newTime.minute = (self.minute + t2.minute) - 60 if (self.minute + t2.minute) >= 60 else  (self.minute + t2.minute)

        newTime.hour = self.hour + t2.hour
        
        if additionalHour:
            newTime.hour += 1
        
        return newTime
    
    def displayTime(self):
        print(f"{self.hour} hr {self.minute} min")
    
    def displayMinute(self):
        print(f"{self.hour * 60 + self.minute} minutes")

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = t1.addTime(t2)

t3.displayTime()
t3.displayMinute()