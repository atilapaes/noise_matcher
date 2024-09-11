#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:58:23 2024
@author: atilapaes

REC: Record audio with default or personalized parameters.
"""
import pyaudio
import wave
import datetime

def rec():
    """
 
    """
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 5
    filename = "data/raw/"+ datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') +".wav"
    
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    
    ##print('Recording...')
    
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True,
                    input_device_index=0
                    )
    
    frames = []  # Initialize array to store frames
    
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    
    print('Writing file',filename,'. Press ctrl+c to stop.')
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    #print('Done.')    
#-------------


while True:
    start_rec = input("Press R to start recording? (R/r): ")
    if start_rec.lower() == 'r':
        break
    else:
        print("Invalid input.")

print('Recording...')

        
try:
    while True:
        rec()
except KeyboardInterrupt:
    pass    



