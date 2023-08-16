
class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60

    def info(self):
        print('Name: {}\nMatrix: {}\nRes: {}\nFreq: {}\n'.format(self.name, self.matrix, self.res, self.freq))

class Headphone:
    name = 'Sony'
    sensivity = 108
    micro = True

    def info(self):
        print(('Name: {}\nSensivity: {}\nMicro: {}\n'.format(self.name, self.sensivity, self.micro)))

monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_3 = Monitor()
monitor_4 = Monitor()
monitor_2.freq = 144
monitor_3.freq = 70

headphone_1 = Headphone()
headphone_2 = Headphone()
headphone_3 = Headphone()
headphone_1.micro = False

monitor_1.info()
monitor_2.info()
monitor_3.info()
monitor_4.info()
headphone_1.info()
headphone_2.info()
headphone_3.info()