#Python sonar data analysis and plotting code for Jetson TX-2 Initial interfacing

file = r'C:\Users\wnath\PycharmProjects\untitled3\dataset1\static\sample_15_rotation_angle_27.00.txt'




def main():
    with open(file) as data:
        # Split data into left and right ear arrays
        c = 0
        R_Data = [0]*10000
        L_Data = [0]*10000
        for line in data:
            if c <= 9999:
                R_Data[c] = int(line)
            else:        
                L_Data[c-10000] = int(line)
            c += 1




if __name__ == '__main__':
    main()
    
