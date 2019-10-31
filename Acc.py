import smbus
import time
import datetime


#from azure.storage.blob import BlockBlobService, ContentSettings, AppendBlobSe$
#append_blob_service=AppendBlobService(account_name='iotcapstone3',account_key=$

import serial,time,sys,Adafruit_GPIO.SPI as SPI, Adafruit_MCP3008
import RPi.GPIO as GPIO
#from azure.storage.blob import BlockBlobService, ContentSettings, AppendBlobSe$
#append_blob_service = AppendBlobService(account_name = 'powerdemoreadings', ac$

mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(0,0))

#def Foo(first =[]):
#       if first ==[]:
#               append_blob_service.create_container('3dprinter',public_access $
#               append_blob_service.create_blob('3dprinter','acc')
#               first.append('Not empty')

#def Foo2(first =[]):
#       if first ==[]:
#               append_blob_service.create_container('3dprinter',public_access $
#               append_blob_service.create_blob('3dprinter','piezo')
#               first.append('Not empty')

line1 = ""
line2 = ""
i = 0
j = 0
#now=datetime.datetime.now()
#st=now.strftime('%Y-%m-%d-%H-%M')
#st=str(st)

# Get I2C bus
bus = smbus.SMBus(1)

# I2C address of the device
MMA8452Q_DEFAULT_ADDRESS = 0x68 #used to be 1D

# MMA8452Q Register Map
MMA8452Q_REG_STATUS = 0x00 # Data status Register
MMA8452Q_REG_OUT_X_MSB = 0x01 # Output Value X MSB
MMA8452Q_REG_OUT_X_LSB = 0x02 # Output Value X LSB
MMA8452Q_REG_OUT_Y_MSB = 0x03 # Output Value Y MSB
MMA8452Q_REG_OUT_Y_LSB = 0x04 # Output Value Y LSB
MMA8452Q_REG_OUT_Z_MSB = 0x05 # Output Value Z MSB
MMA8452Q_REG_OUT_Z_LSB = 0x06 # Output Value Z LSB
MMA8452Q_REG_SYSMOD = 0x0B # System mode Register
MMA8452Q_REG_INT_SOURCE = 0x0C # System Interrupt Status Register
MMA8452Q_REG_WHO_AM_I = 0x0D # Device ID Register
MMA8452Q_REG_XYZ_DATA_CFG = 0x0E # Data Configuration Register
MMA8452Q_REG_CTRL_REG1 = 0x2A # Control Register 1
MMA8452Q_REG_CTRL_REG2 = 0x2B # Control Register 2
MMA8452Q_REG_CTRL_REG3 = 0x2C # Control Register 3
MMA8452Q_REG_CTRL_REG4 = 0x2D # Control Register 4
MMA8452Q_REG_CTRL_REG5 = 0x2E # Control Register 5

# MMA8452Q Data Configuration Register
MMA8452Q_DATA_CFG_HPF_OUT = 0x10 # Output Data High-Pass Filtered
MMA8452Q_DATA_CFG_FS_2 = 0x00 # Full-Scale Range = 2g
MMA8452Q_DATA_CFG_FS_4 = 0x01 # Full-Scale Range = 4g
MMA8452Q_DATA_CFG_FS_8 = 0x02 # Full-Scale Range = 8g

# MMA8452Q Control Register 1
MMA8452Q_ASLP_RATE_50 = 0x00 # Sleep mode rate = 50Hz
MMA8452Q_ASLP_RATE_12_5 = 0x40 # Sleep mode rate = 12.5Hz
MMA8452Q_ASLP_RATE_6_25 = 0x80 # Sleep mode rate = 6.25Hz
MMA8452Q_ASLP_RATE_1_56 = 0xC0 # Sleep mode rate = 1.56Hz
MMA8452Q_ODR_800 = 0x00 # Output Data Rate = 800Hz
MMA8452Q_ODR_400 = 0x08 # Output Data Rate = 400Hz
MMA8452Q_ODR_200 = 0x10 # Output Data Rate = 200Hz
MMA8452Q_ODR_100 = 0x18 # Output Data Rate = 100Hz
MMA8452Q_ODR_50 = 0x20 # Output Data Rate = 50Hz
MMA8452Q_ODR_12_5 = 0x28 # Output Data Rate = 12.5Hz
MMA8452Q_ODR_6_25 = 0x30 # Output Data Rate = 6.25Hz
MMA8452Q_ODR_1_56 = 0x38 # Output Data Rate = 1_56Hz
MMA8452Q_MODE_NORMAL = 0x00 # Normal Mode

MMA8452Q_MODE_REDUCED_NOISE = 0x04 # Reduced Noise Mode
MMA8452Q_MODE_FAST_READ = 0x02 # Fast Read Mode
MMA8452Q_MODE_ACTIVE = 0x01 # Active Mode
MMA8452Q_MODE_STANDBY = 0x00 # Standby Mode
a = ""

#def Foo(firstTime = []):
        #if firstTime == []:
                #global server_sock
                #global client_sock
                #server_sock = BluetoothSocket(RFCOMM)
                #print(1)
                #server_sock.bind(("",4))
                #print(2)
                #server_sock.listen(1)
                #print(4)
                #client_sock, client_info = server_sock.accept()
                #print(5)
                #client_sock.setblocking(False)
                #print client_info
               #print(6)
                #firstTime.append('Not empty')

#making a container the first time this program is run
#def Foo(first=[]):
        #if first==[]:
                #append_blob_service.create_container('acccontainer',public_acc$
                #append_blob_service.create_blob('acccontainer','accblob')
                #first.append('Not Empty')


class MMA8452Q():
        def __init__(self):
                self.mode_configuration()
                self.data_configuration()
        def mode_configuration(self):
                """Select the Control Register-1 configuration of the accelerom$
                MODE_CONFIG = (MMA8452Q_ODR_800 | MMA8452Q_MODE_NORMAL | MMA845$
                bus.write_byte_data(MMA8452Q_DEFAULT_ADDRESS, MMA8452Q_REG_CTRL$
        def data_configuration(self):
                """Select the Data Configuration Register configuration of the $
                DATA_CONFIG = (MMA8452Q_DATA_CFG_FS_2)
                bus.write_byte_data(MMA8452Q_DEFAULT_ADDRESS, MMA8452Q_REG_XYZ_$
        def read_accl(self):
               """Read data back from MMA8452Q_REG_STATUS(0x00), 7 bytes
                Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB$
                data = bus.read_i2c_block_data(MMA8452Q_DEFAULT_ADDRESS, MMA845$
                # Convert the data
                xAccl = (data[1] * 256 + data[2]) / 16
                if xAccl > 2047 :
                        xAccl -= 4096
                yAccl = (data[3] * 256 + data[4]) / 16
                if yAccl > 2047 :
                        yAccl -= 4096
                zAccl = (data[5] * 256 + data[6]) / 16
                if zAccl > 2047 :
                        zAccl -= 4096
               return {'x' : xAccl, 'y' : yAccl, 'z' : zAccl}

#from MMA8452Q import MMA8452Q
mma8452q = MMA8452Q()

while True:
        #Foo()
        #Foo2()
        data = mcp.read_adc(0)
        data = repr(data)
        #print(data)
       mma8452q.mode_configuration()
        mma8452q.data_configuration()
        accl = mma8452q.read_accl()
        xdir = accl.get('x')
        ydir = accl.get('y')
        zdir = accl.get('z')
        xdir = str(xdir)
        ydir = str(ydir)
        zdir = str(zdir)
        dict1 = {'x':xdir,'y':ydir,'z':zdir}
       print(dict1)
        try:
                time.sleep(5.0)
        except:
                pass

       #csv writing
        #dict1 = repr(dict1)
        #accdata = open('accdata','a')
        #accdata.write(dict1)
        #accdata.write('\n')
        #accdata.close()
        #end writing


       #line1 = xdir + "," + ydir + "," + zdir + "\n"
        #if i == 100:
                #run sliver of code for azure stuff
        #       append_blob_service.append_blob_from_text('3dprinter','acc',lin$
        #       append_blob = append_blob_service.get_blob_to_text('3dprinter',$
        #       i = 0
        #       line1 = ""
        #i = i + 1


       #line2 = data + "\n"
        #if j == 150:
                #run sliver of code for azure stuff
        #       append_blob_service.append_blob_from_text('3dprinter','piezo',l$
        #       append_blob = append_blob_service.get_blob_to_text('3dprinter',$
        #       j = 0
        #       line1 = ""
        #j = j + 1

       #50 mV = g........1024 == 5V.....0 == 0V == 0g
        ##csv writing
        #piezo = repr(data)
        #piezodata = open('piezodata','a')
        #piezodata.write(piezo)
        #piezodata.write('\n')
        #piezodata.close()
        ##end writing

       #x = xdir + ',' + ydir + ',' + zdir + '\n'
        #a = a + x
        #accl = repr(accl)
        #dict1 = repr(dict1)
        #print(dict1)
        #data1 = client_sock.recv(2)
        #if data1 == "go":
        #client_sock.send(dict1)
        #append_blob_service.append_blob_from_text('acccontainer','acc',x)
        #append_blob=append_blob_service.get_blob_to_text('acccontainer','acc')
        #append_blob_service.append_blob_from_text('acccontainer','accblob','\n$
        #append_blob=append_blob_service.get_blob_to_text('acccontainer','acc')
        #print "Acceleration in X-Axis : %d"%(accl['x'])
        #print "Acceleration in Y-Axis : %d"%(accl['y'])
        #print "Acceleration in Z-Axis : %d"%(accl['z'])


