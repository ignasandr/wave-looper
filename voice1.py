import sounddevice as sd
import threading
import time

data_type = "float32"

class Voice():
    def __init__(self, file, device):
        self.file = file
        self.device = device
        self.stream = sd.OutputStream(device=self.device, dtype=data_type)


    def __play_stream(self):
        print(f'Starting stream on device {self.device}')
        self.stream.start()
        self.stream.write(self.file)
        self.loop_voice()
    

    def loop_voice(self):
        thread = threading.Thread(target=self.__play_stream)
        thread.start()
