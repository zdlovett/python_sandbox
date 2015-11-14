import io

class script(object):
    def __init__(self, output):
        self.power = 0
        self.time = 5
        self.output = output

    #power is set in dbm
    def set_power(self, target):
        self.power = target
        return self.power

    #duration is set in seconds
    def set_time(self, time):
        self.time += time

    def get_time_string(self):
        #return format is hh:mm:ss
        time = self.time
        hours = time / (60*60)
        time -= hours*(60*60)
        minutes = time / 60
        time -= minutes * 60
        seconds = time

        return str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)

    def start(self):
        header = "RU_NOWAIT\n-,INIT_POS,v1_m1,37.873287,-122.302500,15\n-,POW_LEV,V1_A1,0,GPS,0,0,1,1,1,1,0\n"
        self.output.write(header)

    def power_for_time(self, power, duration):
        time = self.get_time_string()
        self.set_time(duration)
        self.set_power(power)

        msg = ""
        msg += time
        msg += ",POW_LEV,V1_A1,"
        power = self.power
        if power >= 0:
            msg += "+"
            msg += str(power)
        else:
            msg += str(power)
        msg += ",GPS,0,0,1,1,1,1,0\n"
        self.output.write(msg)

    def ramp(self, start, end, step_time):
        if start > end:
            r = range(end, start + 1)
            r.reverse()
        else:
            r = range(start, end + 1)
        for i in r:
            self.power_for_time(i, step_time)



if __name__ == "__main__":
    with io.open("script.txt",'wb') as output:
        s = script(output)
        s.start()

        """The two functions that you can use are:"""
        #s.power_for_time(power, duration)
        """and"""
        #s.ramp(start_power, end_power, step_duration)
        """note that the units are seconds for the step duration"""

        """for example, to hold at 12dbm for 13 minutes and then
        ramp from +15dbm to -18dbm in ten second steps is the following"""
        #s.power_for_time(12, (13*60))
        #s.ramp(15, -18, 10)

        """This is where you can put teh codez"""
        s.power_for_time(15, (13*60))
        s.ramp(10, -18, 10)
        s.ramp(10, -9999, 10)


        """stop touching teh codez!"""
