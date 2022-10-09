class Time:
    time = []
    def __init__(self, start_time: str, end_time: str, delta: str):
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta
    def get_timeline(self):
        hour_1 = int(self.start_time[0:2])
        hour_2 = int(self.end_time[0:2])
        min_3 = int(self.delta[3:5])
        while hour_1 <= hour_2:
            if hour_1 < 10:
                hour_1 = "0{}".format(hour_1)
            for min_1 in range(0, 60, min_3):
                if min_1 == 0:
                    min_1 = "00"
                string = "{}.{}".format(str(hour_1), str(min_1))
                if string == self.end_time:
                    Time.time.append(self.end_time)
                    break
                Time.time.append("{}.{}".format(str(hour_1), str(min_1)))
            hour_1 += 1
        return Time.time
    def reserve_time(self, _time:str):
     Time.time.remove(_time)
     return print(Time.time)

time1 = Time('10.00', '19.00', '00.30')
time1.get_timeline()
time1.reserve_time('13.00')
class ReverveDateTime(Time):
    def __init__(self, dates:list[int]):
        self.dates = dates
        for i in range(31):
            dates.append(i)
        #self.times = times
    def get_timeline(self):
        return print(self.dates)
#time2 = ReverveDateTime()
#ReverveDateTime.get_timeline()
