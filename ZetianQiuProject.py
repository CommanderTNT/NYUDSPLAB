#Zetian Qiu

import tkinter as Tk
import pyaudio
import struct
import numpy as np
from math import sin, cos, pi
import random
from scipy import signal
import tkinter as Tk    
from random import random
import wave
Note = 0 *13


BLOCKLEN   = 512        # Number of frames per block
gain = 20000
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 4000      # Frames per second
RECORD_SECONDS= 2
# Set parameters of delay system
file_name = 'Final.wav'          # Name of output wavefile
wf = wave.open(file_name, 'w')    # wf : wave file
wf.setnchannels(CHANNELS)                # one channel (mono)
wf.setsampwidth(WIDTH)                # two bytes per sample (16 bits per sample)
wf.setframerate(RATE)   
K = 0.93
b = 1
N = 12
MAXVALUE = 2**15-1
f0=55
freqs=[0]*12
for i in range(12):
    freqs[i] =2**(i/12) * f0
buffer = [0 for i in range(N)]


N0=int(freqs[11])
N1=int(freqs[10])
N2=int(freqs[9])
N3=int(freqs[8])
N4=int(freqs[7])
N5=int(freqs[6])
N6=int(freqs[5])
N7=int(freqs[4])
N8=int(freqs[3])
N9=int(freqs[2])
N10=int(freqs[1])
N11=int(freqs[0])


buffer0 = N0 *[0]

buffer1 = N1 *[0]
buffer2 = N2 *[0]
buffer3 = N3 *[0]
buffer4 = N4 *[0]

buffer5 = N5 *[0]
buffer6 = N6 *[0]
buffer7 = N7 *[0]
buffer8 = N8 *[0]
buffer9 = N9 *[0]
buffer10 = N10 *[0]
buffer11 = N11 *[0]

# Initialize buffer indices
bufferindex0 = int(N0/2)     # read index


bufferindex1 = int(N1/2)   

bufferindex2 = int(N2/2)  

bufferindex3 = int(N3/2)   

bufferindex4 = int(N4/2)   

bufferindex5 = int(N5/2)   

bufferindex6 = int(N6/2)     
                 
bufferindex7 = int(N7/2)   

bufferindex8 = int(N8/2)   

bufferindex9 = int(N9/2)   

bufferindex10 = int(N10/2)   

bufferindex11 = int(N11/2) 



x0 = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
x11 = 0
x12 = 0


# Open the audio output stream for guitar
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)


Guitar = True
CONTINUE = True
KEYPRESS = False

def my_function(event):
    global CONTINUE
    global KEYPRESS
    global Note
    print('You pressed ' + event.char)
    if event.char == "z":
        Note = 0
    if event.char == "x":
        Note = 1
    if event.char == "c":
        Note = 2
    if event.char == "v":
        Note = 3
    if event.char == "b":
        Note = 4
    if event.char == "n":
        Note = 5
    if event.char == "m":
        Note = 6
    if event.char == "a":
        Note = 7
    if event.char == "s":
        Note = 8      
    if event.char == "d":
        Note = 9
    if event.char == "f":
        Note = 10
    if event.char == "g":
        Note = 11           
    if event.char == ' ':
        print('this is drum')         
        Note = 12
        
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    KEYPRESS = True
root = Tk.Tk()
root.bind("<Key>", my_function)

print('Press keys for sound.')
print('Press "q" to quit')
while CONTINUE:
    root.update()


    for i in range(0, BLOCKLEN):
        if KEYPRESS and CONTINUE:    
            if Note == 0:
                x0 = gain
            if Note == 1:
                x1 = gain
            if Note == 2:
                x2 = gain
            if Note == 3:
                x3 = gain
            if Note == 4:
                x4 = gain
            if Note == 5:
                x5 = gain
            if Note == 6:
                x6 = gain
            if Note == 7:
                x7 = gain
            if Note == 8:
                x8 = gain
            if Note == 9:
                x9 = gain
            if Note == 10:
                x10 = gain
            if Note == 11:
                x11 = gain
            if Note == 12:
                x12 = gain
            
        
            # Compute output value
            # y(n) = x(n) + K/2 x(n-N) + K/2 x(n-N-1)
        y0 = x0 + K/2 * buffer0[bufferindex0] + K/2 * buffer0[bufferindex0-1]
        y1 = x1 + K/2 * buffer1[bufferindex1] + K/2 * buffer1[bufferindex1-1]
        y2 = x2 + K/2 * buffer2[bufferindex2] + K/2 * buffer2[bufferindex2-1]
        y3 = x3 + K/2 * buffer3[bufferindex3] + K/2 * buffer3[bufferindex3-1]
        y4 = x4 + K/2 * buffer4[bufferindex4] + K/2 * buffer4[bufferindex4-1]
        y5 = x5 + K/2 * buffer5[bufferindex5] + K/2 * buffer5[bufferindex5-1]
        y6 = x6 + K/2 * buffer6[bufferindex6] + K/2 * buffer6[bufferindex6-1]
        y7 = x7 + K/2 * buffer7[bufferindex7] + K/2 * buffer7[bufferindex7-1]
        y8 = x8 + K/2 * buffer8[bufferindex8] + K/2 * buffer8[bufferindex8-1]
        y9 = x9 + K/2 * buffer9[bufferindex9] + K/2 * buffer9[bufferindex9-1]
        y10 = x10 + K/2 * buffer10[bufferindex10] + K/2 * buffer10[bufferindex10-1]
        y11 = x11 + K/2 * buffer11[bufferindex11] + K/2 * buffer11[bufferindex11-1]
        
        if Note== 12:   
            prob=0.5
            r = np.random.binomial(1, prob)
            sign = float(r == 1) * 2 - 1
            y12 = x12 + sign*(K/2 * buffer11[bufferindex11] + K/2 * buffer11[bufferindex11-1])
            buffer11[bufferindex11] = y12
            bufferindex11 = bufferindex11 + 1
            if bufferindex11 == N11:
                bufferindex11 = 0
            KEYPRESS = False    

            # Update buffer (pure delay)
        buffer0[bufferindex0] = y0
        buffer1[bufferindex1] = y1
        buffer2[bufferindex2] = y2
        buffer3[bufferindex3] = y3
        buffer4[bufferindex4] = y4
        buffer5[bufferindex5] = y5
        buffer6[bufferindex6] = y6
        buffer7[bufferindex7] = y7
        buffer8[bufferindex8] = y8
        buffer9[bufferindex9] = y9
        buffer10[bufferindex10] = y10
        buffer11[bufferindex11] = y11
            

 
            # Increment read index
        bufferindex0 = bufferindex0 + 1
        if bufferindex0 == N0:
            bufferindex0 = 0
        bufferindex1 = bufferindex1 + 1
        if bufferindex1 == N1:
            bufferindex1 = 0
        bufferindex2 = bufferindex2 + 1
        if bufferindex2 == N2:
            bufferindex2 = 0
        bufferindex3 = bufferindex3 + 1
        if bufferindex3 == N3:
            bufferindex3 = 0
        bufferindex4 = bufferindex4 + 1
        if bufferindex4 == N4:
            bufferindex4 = 0
        bufferindex5 = bufferindex5 + 1
        if bufferindex5 == N5:
            bufferindex5 = 0
        bufferindex6 = bufferindex6 + 1
        if bufferindex6 == N6:
            bufferindex6 = 0
        bufferindex7 = bufferindex7 + 1
        if bufferindex7 == N7:
            bufferindex7 = 0
        bufferindex8 = bufferindex8 + 1
        if bufferindex8 == N8:
            bufferindex8 = 0
        bufferindex9 = bufferindex9 + 1
        if bufferindex9 == N9:
            bufferindex9 = 0
        bufferindex10 = bufferindex10 + 1
        if bufferindex10 == N10:
            bufferindex10 = 0
        bufferindex11 = bufferindex11 + 1
        if bufferindex11 == N11:
            bufferindex11 = 0


        y = y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +  y9 + y10 + y11
        if Note == 12:
            y=y12+ y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +  y9 + y10 + y11
            
        
        KEYPRESS = False    
            # Clip and convert output value to binary data
        outputg_bytes = struct.pack('h' , int(np.clip(y, -MAXVALUE, MAXVALUE)))

            # Write output value to audio stream
        stream.write(outputg_bytes)
        wf.writeframes(outputg_bytes)     
        x0 = 0
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0
        x8 = 0
        x9 = 0
        x10 = 0
        x11 = 0
        x12 = 0 

           


print('* Finished')            
           
           
        

 
# Close audio stream
stream.stop_stream()
stream.close()

p.terminate()