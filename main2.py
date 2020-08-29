"""
Play multiple loopings wav files
Based on Pear project by Devon Bray
"""
 

import sounddevice
import soundfile
# import threading
import os
from voice2 import Voice 

data_type = "float32"
 

def load_sound_file_into_memory(path):
    """
    get the in-memory version of a given path to a wav file
    :param path: wav file to be loaded
    :return: audio_data, a 2d numpy array
    """
 
    audio_data, _ = soundfile.read(path, dtype=data_type)
    return audio_data
 

def get_device_number_if_usb_soundcard(index_info):
    """
    given a device dict, return true if the device is one of our usb sound cards and false if otherwise
    :param index_info: a device info dict from pyaudio.
    :return: true if usb sound card, false if otherwise
    """
 
    index, info = index_info
 
    if "C-Media" in info["name"]:
        return index
    return False
 

# def play_wav_on_index(audio_data, stream_object):
#     """
#     play an audio file given as the result of `load_sound_file_into_memory`
#     :param audio_data: a two-dimensional numpy array
#     :param stream_object: a sounddevice.outputstream object that will immediately start playing any data written to it.
#     :return: none, returns when the data has all been consumed
#     """
 
#     stream_object.write(audio_data)
 

# def create_running_output_stream(index):
#     """
#     create an sounddevice.outputstream that writes to the device specified by index that is ready to be written to.
#     you can immediately call `write` on this object with data and it will play on the device.
#     :param index: the device index of the audio device to write to
#     :return: a started sounddevice.outputstream object ready to be written to
#     """
 
#     output = sounddevice.outputstream(
#         device=index,
#         dtype=data_type
#     )
#     output.start()
#     return output
 

if __name__ == "__main__":
 
    def good_filepath(path):
        """
        macro for returning false if the file is not a non-hidden wav file
        :param path: path to the file
        :return: true if a non-hidden wav, false if not a wav or hidden
        """
        return str(path).endswith(".wav") and (not str(path).startswith("."))
 
    cwd = os.getcwd()
    sound_file_paths = [
        os.path.join(cwd, path) for path in sorted(filter(lambda path: good_filepath(path), os.listdir(cwd)))
    ]

    print("discovered the following .wav files:", sound_file_paths)
 
    files = [load_sound_file_into_memory(path) for path in sound_file_paths]
 
    print("files loaded into memory, looking for usb devices.")
 
    devices = list(filter(lambda x: x is not False,
                                         map(get_device_number_if_usb_soundcard,
                                             [index_info for index_info in enumerate(sounddevice.query_devices())])))
 
    print("discovered the following usb sound devices", devices)
 

    voices = [Voice(file, device) for file, device in zip(files, devices)]

    print(voices)

    for voice in voices:
        print(f'Starting loop {voice.device}')
        voice.loop_voice()
        
