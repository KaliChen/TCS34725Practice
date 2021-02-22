  
# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TCS34725
# This code is designed to work with the TCS34725_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time
import matplotlib.pyplot as plt
import numpy as np
from pylive import live_plotter


def luminance():
    # Get I2C bus
    bus = smbus.SMBus(1)

    # TCS34725 address, 0x29(41)
    # Select Enable register, 0x80(128)
    #		0x03(03)	Power ON, RGBC enable, RGBC Interrupt Mask not asserted
    #					Wait disable, Sleep After Interrupt not asserted
    bus.write_byte_data(0x29, 0x80, 0x03)
    # TCS34725 address, 0x29(41)
    # Select RGBC Timing register, 0x81(129)
    #		0x00(00)	ATIME : 700ms
    bus.write_byte_data(0x29, 0x81, 0x00)
    # TCS34725 address, 0x29(41)
    # Select Wait Time register, 0x83(131)
    #		0xFF(255)	WTIME : 2.4ms
    bus.write_byte_data(0x29, 0x83, 0xFF)
    # TCS34725 address 0x29(41)
    # Select Control register, 0x8F(143)
    #		0x00(00)	AGAIN is 1x
    bus.write_byte_data(0x29, 0x8F, 0x00)

    # TCS34725 address 0x29(41)
    # Read data back from 0x94(148), 8 bytes
    # cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB
    # Blue LSB, Blue MSB 
    data = bus.read_i2c_block_data(0x29, 0x94, 8)

    # Convert the data
    cData = data[1] * 256 + data[0]
    red = data[3] * 256 + data[2]
    green = data[5] * 256 + data[4]
    blue = data[7] * 256 + data[6]

    # Calculate luminance
    luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)

    # Output data to screen
    print("Red Color luminance : %d lux" %red)
    print("Green Color luminance : %d lux" %green)
    print("Blue Color luminance : %d lux" %blue)
    print("IR luminance : %d lux" %cData)
    print("Ambient Light luminance : %.2f lux" %luminance) 
    
    r = int(red/cData *256 + luminance/cData*256)
    g = int(green/cData *256+ luminance/cData*256)
    b = int(blue/cData *256+ luminance/cData*256)
    seconds = time.time()
    return(seconds, r, g, b)
    
def Doluminance():
    while(1):
        print(luminance())
        # 暫停 1 秒
        time.sleep(1.0)      
def cData_red_green_blue():
    # Get I2C bus
    bus = smbus.SMBus(1)

    # TCS34725 address, 0x29(41)
    # Select Enable register, 0x80(128)
    #		0x03(03)	Power ON, RGBC enable, RGBC Interrupt Mask not asserted
    #					Wait disable, Sleep After Interrupt not asserted
    bus.write_byte_data(0x29, 0x80, 0x03)
    # TCS34725 address, 0x29(41)
    # Select RGBC Timing register, 0x81(129)
    #		0x00(00)	ATIME : 700ms
    bus.write_byte_data(0x29, 0x81, 0x00)
    # TCS34725 address, 0x29(41)
    # Select Wait Time register, 0x83(131)
    #		0xFF(255)	WTIME : 2.4ms
    bus.write_byte_data(0x29, 0x83, 0xFF)
    # TCS34725 address 0x29(41)
    # Select Control register, 0x8F(143)
    #		0x00(00)	AGAIN is 1x
    bus.write_byte_data(0x29, 0x8F, 0x00)

    # TCS34725 address 0x29(41)
    # Read data back from 0x94(148), 8 bytes
    # cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB
    # Blue LSB, Blue MSB 
    data = bus.read_i2c_block_data(0x29, 0x94, 8)

    # Convert the data
    cData = data[1] * 256 + data[0]
    red = data[3] * 256 + data[2]
    green = data[5] * 256 + data[4]
    blue = data[7] * 256 + data[6] 
    seconds = time.time()    
    return (seconds, cData, red, green, blue)

def Do_cData_red_green_blue():
    while(1):
        #ans = luminance()
        #ans = data_0_7()
        #print(ans)
        #ans = cData_red_green_blue()
        print(cData_red_green_blue())
        # 暫停 1 秒
        time.sleep(1.0)
        
def data_0_7():
    # Get I2C bus
    bus = smbus.SMBus(1)

    # TCS34725 address, 0x29(41)
    # Select Enable register, 0x80(128)
    #		0x03(03)	Power ON, RGBC enable, RGBC Interrupt Mask not asserted
    #					Wait disable, Sleep After Interrupt not asserted
    bus.write_byte_data(0x29, 0x80, 0x03)
    # TCS34725 address, 0x29(41)
    # Select RGBC Timing register, 0x81(129)
    #		0x00(00)	ATIME : 700ms
    bus.write_byte_data(0x29, 0x81, 0x00)
    # TCS34725 address, 0x29(41)
    # Select Wait Time register, 0x83(131)
    #		0xFF(255)	WTIME : 2.4ms
    bus.write_byte_data(0x29, 0x83, 0xFF)
    # TCS34725 address 0x29(41)
    # Select Control register, 0x8F(143)
    #		0x00(00)	AGAIN is 1x
    bus.write_byte_data(0x29, 0x8F, 0x00)

    # TCS34725 address 0x29(41)
    # Read data back from 0x94(148), 8 bytes
    # cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB
    # Blue LSB, Blue MSB 
    data = bus.read_i2c_block_data(0x29, 0x94, 8)
    # 從 1970/1/1 00:00:00 至今的秒數
    seconds = time.time()
    # 輸出結果
    #print(seconds)
    return(seconds, data)

def Do_data_0_7():
    while(1):
        print(data_0_7())
        # 暫停 1 秒
        time.sleep(1.0)
            
def matplotlibLive():
    size = 100
    x_vec = np.linspace(0,1,size+1)[0:-1]
    y_vec = np.random.randn(len(x_vec))
    line1 = []
    while True:
        rand_val = np.random.randn(1)
        y_vec[-1] = rand_val
        line1 = live_plotter(x_vec,y_vec,line1)
        y_vec = np.append(y_vec[1:],0.0)    
       
if __name__ == '__main__':
    #Do_data_0_7()
    #Do_cData_red_green_blue()
    matplotlibLive()
