import sounddevice as sd
import threading
import time

data_type = "float32"

class Voice():
    def __init__(self, file, device):
        self.file = file
        self.device = device


    def __play_stream(self):
        print(f'Starting stream on device {self.device}')
        sd.play(self.file, loop=True, device=self.device)
        sd.wait()
        # print("thread finished")
    

    def loop_voice(self):
        thread = threading.Thread(target=self.__play_stream)
        thread.start()
        # if thread.is_alive():
        #     print('cool')
        #     self.loop_voice()
        # thread.join()
        # self.stream.close()
        # self.loop_voice()