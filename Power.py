import serial,time,sys
import RPi.GPIO as GPIO
from xbee import ZigBee
import ast

ser = serial.Serial('/dev/ttyAMA0',9600)
zb = ZigBee(ser)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#from azure.storage.blob import BlockBlobService, ContentSettings, AppendBlobSe$
#append_blob_service = AppendBlobService(account_name = 'powerdemoreadings', ac$
i = 0
line1 = ""

#def Foo(first =[]):
# if first ==[]:
#       append_blob_service.create_container('3dprinter',public_access = Public$
#       append_blob_service.create_blob('3dprinter','power')
#       first.append('Not empty')


def power():
        volt = 'wait'
        curr = 'wait'
        ser = serial.Serial('/dev/ttyAMA0',9600)
        zb = ZigBee(ser)
        zb.send("remote_at", id = b'\x17', frame_id = b'\x00', dest_addr_long =$
        response = zb.wait_read_frame()
        Address = response.get('source_addr_long')
        if Address == '\x00\x13\xA2\x00\x41\x54\xF3\xFC':
                Samples = response.get('samples')
                Samples = str(Samples)[1:-1]
                Samples = ast.literal_eval(Samples)
                current_raw = Samples.get('adc-2') #pin 18 on xbee
                voltage_raw = Samples.get('adc-3') #pin 17 on xbee
                curr = repr(current_raw)
                volt = repr(voltage_raw)
       return volt, curr

while True:
#       Foo();
        volt,curr = power()
        print(volt)
        print(curr)
        line1 = volt + "," + curr + "\n"
#       if i == 100:
                #run sliver of code for azure stuff
#               append_blob_service.append_blob_from_text('3dprinter','power',l$
#               append_blob = append_blob_service.get_blob_to_text('3dprinter',$
#               i = 0
#               line1 = ""
#       i = i + 1
        time.sleep(0.5)

