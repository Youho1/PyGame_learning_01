from AudioVisual import AudioVisual

class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size
    def watch(self):
        str = "have fun!" if self.power else "switch on"
        print(str)