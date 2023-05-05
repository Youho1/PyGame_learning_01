from TV import TV
from Audio import Audio

obj1 = TV(False, 12, 40)
obj1.switch(True)
obj1.watch()

obj2 = Audio(True, 15)
obj2.set_volume(6)
obj2.tune()