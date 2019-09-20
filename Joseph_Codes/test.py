import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import serial
import struct
import time
import math
import os

# Native USB port of Due (use Device Manager to find)
PORT = 'COM5'

# Number of milliseconds between switching from dynamic and static
DYNAMIC_STATIC_INTERVAL = 3000

# Number of runs between plot updates. Plotting almost doubles the
# duration of each run, so keep this large
PLOT_INTERVAL = 10

# Number of milliseconds for each run. This accounts for the time it
# takes dynamic motion to complete. Set to 0 to achieve the maximum
# collection rate
RUN_DURATION = 0

# Number of milliseconds to wait after switching from dynamic. This
# accounts for any reverberations created by dynamic motion
DELAY_AFTER_SWITCHING_FROM_DYNAMIC = 200

def main():
    # Open connection to device
    ser = serial.Serial(PORT)
    ser.setDTR(False)
    ser.flushInput()
    ser.setDTR(True)
    
    print('Communicating over port {}'.format(ser.name))

    # Send handshake to device
    ser.write(bytearray([0, 0, 0, 0, 0]))
    opcode, response_len = struct.unpack('<BI', ser.read(size=5))
    if opcode != 0x80 or response_len != 2:
        print('Unexpected packet! Reset the Due'
               .format(opcode, response_len))
        return

    version = struct.unpack('<BB', ser.read(size=response_len))
    print('Connected to device v{}.{}'.format(*version))
    if version != (0, 2):
        print('Invalid device version! Update the Due')
        return

    # Ask for name of output folder
    print('Enter name of folder: ', end='')
    folder_name = input()
    
    # Create a subplot for each channel
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.set_xlim([0, 10000])
    ax1.set_ylim([0, 4096])
    ax2.set_xlim([0, 10000])
    ax2.set_ylim([0, 4096])

    num_runs = 0
    use_dynamic_motion = True
    trial_start = datetime.now()
    last_switch = time.time_ns()
    first_since_switch = True

    print('Starting with {}'.format('dynamic' if use_dynamic_motion else 'static'))

    while True:
        try:
            # Switch motion profile from static to dynamic every 10 seconds
            if (time.time_ns() - last_switch) * 1e-6 > DYNAMIC_STATIC_INTERVAL:
                num_runs_since_switch = 0
                use_dynamic_motion  ^= True
                last_switch = time.time_ns()

                print('Switching to {}'.format('dynamic' if use_dynamic_motion else 'static'))

                # Wait for some time if we're switching from dynamic to static
                if not use_dynamic_motion:
                    while (time.time_ns() - last_switch) * 1e-6 < DELAY_AFTER_SWITCHING_FROM_DYNAMIC:
                        pass

            run_start = time.time_ns()

            # Initiate data collection
            collection_opcode = (3 if first_since_switch else 4) if use_dynamic_motion else 2
            ser.write(bytearray([collection_opcode, 0, 0, 0, 0]))
            opcode, response_len = struct.unpack('<BI', ser.read(size=5))
            if opcode != (0x80 | collection_opcode) or response_len != 0:
                print('Hi packet! Reset the Due'
                       .format(opcode, response_len))
                return

            first_since_switch = False

            # Wait for data collection to finish
            opcode, response_len = struct.unpack('<BI', ser.read(size=5))
            if opcode != 0x82:
                print('Hi packet! opcode=0x{:02x}, response_len={}'
                       .format(opcode, response_len))
                return

            run_end = time.time_ns()
            
            # Create output folder and file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')[:-3]
            output_folder = folder_name + '/' + ('dynamic' if use_dynamic_motion else 'static') + '/'
            output_filename = timestamp + '.txt'
            output_path = output_folder + output_filename
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Transfer the raw data
            raw_data = ser.read(size=response_len)
            #while len(raw_data) < response_len:
            #    raw_data.extend(ser.read(size=4000))

            # Process the raw data
            joined_data = [(y << 8) | x for x, y in zip(raw_data[::2], raw_data[1::2])]
            separated_data = joined_data[::2] + joined_data[1::2]

            with open(output_path, 'w') as f:
                for data in separated_data:
                    f.write('{}\n'.format(data))

            num_runs += 1

            # Periodically plot an incoming signal
            if num_runs % PLOT_INTERVAL == 0:
                elapsed = datetime.now() - trial_start

                # Leave a status message
                ax1.set_title('{} runs - {}'.format(num_runs, str(elapsed)[:-7]))
                ax2.set_title('{} runs/min'.format(int(num_runs/max(elapsed.seconds,1)*60)))

                # Clear previous lines for speed
                ax1.lines = ax2.lines = []

                # Split the data into two channels
                split_point = len(separated_data)//2
                left, right = separated_data[:split_point], separated_data[split_point:]
                
                ax1.plot(left)
                ax2.plot(right)

                # Show the plot without blocking (there's no separate UI
                # thread)
                plt.show(block=False)
                plt.pause(0.001)
                
            # Make sure that each run takes at least RUN_DURATION
            while (time.time_ns() - run_start) * 1e-6 < RUN_DURATION:
                pass

            # Show timing info (this adds time!)
            #processing_end = time.time_ns()
            #print('collect: {:0.3f} ms, total: {:0.3f} ms'.format((run_end - run_start) * 1e-6, (processing_end - run_start) * 1e-6))

        except KeyboardInterrupt:
            break

    print('Closing connection')
    ser.close()

if __name__ == '__main__':
    main()
