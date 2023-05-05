class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    def switch(self, on_off):
        self.power = on_off
    def set_volume(self, vol):
        self.volume = vol