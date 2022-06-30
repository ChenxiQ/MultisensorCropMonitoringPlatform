#!/usr/bin/env python3

import serial
import matplotlib.pyplot as plt


# define x axis
x = [410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940]


def dataPlot():
    # initialize plot
    plt.ion()
    fig = plt.figure()
    ax = fig.gca()

    line, = ax.plot([], [], 'rX:')
    line.set_xdata(x)

    plt.xlabel("Wavelength (nm)")
    plt.xlim(350, 1000)

    # initialize serial port
    arduinoSerial = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    arduinoSerial.reset_input_buffer()
    
    cnt = 0
    while True:
        if arduinoSerial.in_waiting > 0:
            try:
                # read line from serial port
                spectro = arduinoSerial.readline().decode("utf-8").rstrip().split(",") 
            except ValueError:
                continue
            
            if cnt < 5:
                pass
            else:
                # process info from serial port
                spectro = [float(x) for x in spectro[:-1]]
                print(spectro)

                # update plot
                plt.ylim(0, max(spectro)+10)
                line.set_ydata(spectro)
                plt.pause(0.001)
                fig.canvas.draw()
            
            cnt += 1


def quitProgram():
    quit()


if __name__ == '__main__':
    try:
        dataPlot()
    except KeyboardInterrupt:
        quit()
