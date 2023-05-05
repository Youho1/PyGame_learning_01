from AudioVisual import AudioVisual
class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)
    def tune(self):
        str = "La la la..." if self.power else "turn it on"
        print(str)
    
    
