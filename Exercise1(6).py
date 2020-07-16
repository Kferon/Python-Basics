import time
from itertools import cycle

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']


    def running(self):
        for i in cycle(self.__color):
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(4)




x = TrafficLight()
x.running()
