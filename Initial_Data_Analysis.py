#Python sonar data analysis and plotting code for Jetson TX-2 Initial interfacing

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as dsp
import time
file = r'C:\Users\wnath\PycharmProjects\untitled3\dataset1\static\sample_15_rotation_angle_27.00.txt'


def main():
    start = time.time()
    [R_Data, L_Data] = parseSample()
    parsed = time.time()
    R_filt = filterData(R_Data, L_Data)
    filtered = time.time()
    plotData(R_Data, L_Data)
    plotted = time.time()

    #Calculate times
    parse_time = parsed - start
    filter_time = filtered - parsed
    plot_time = plotted - filtered
    print("Parse time: " + str(parse_time) + " seconds")
    print("Filter time: " + str(filter_time) + " seconds")
    print("Plot time: " + str(plot_time) + " seconds")
    
# Get the Sample from the due?
def importSample():
    placeholder = 1337

 # Split data into left and right ear arrays for analysis
def parseSample():
    with open(file) as data:
        c = 0
        R_Data = [0]*10000
        L_Data = [0]*10000
        for line in data:
            if c <= 9999:
                R_Data[c] = int(line)
            else:        
                L_Data[c-10000] = int(line)
            c += 1
    return [R_Data, L_Data]

def plotData(R_Data, L_Data):
    x = np.linspace(0, 1, len(R_Data))
    plt.plot(x, R_Data)
    plt.show()

def filterData(R_Data, L_Data):
    R_filt = dsp.hilbert2(R_Data)
    return R_filt

if __name__ == '__main__':
    main()
    
