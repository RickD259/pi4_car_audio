#initilializes i2c audio chip at boot from saved config file

from smbus import SMBus
i2cbus = SMBus(1)  # Create a new I2C bus
from tkinter import *
from configparser import ConfigParser

#using same volume map as eq
vol_map = dict([(30,15),(29,14),(28,13),(27,12),(26,11),(25,10),(24,9),(23,8),(22,7),(21,6),
(20,5),(19,4),(18,3),(17,2),(16,1),(15,16),(14,17),(13,18),(12,19),(11,20),(10,21),(9,22),
(8,23),(7,24),(6,25),(5,26),(4,27),(3,28),(2,29),(1,30),(0,96)])


#set variables to config file
eq_config = ConfigParser()
eq_config.read('/home/pi/Documents/eq_file.ini')
input_sel = int(eq_config.get('Selections', 'input_sel'))
treble_hz_sel = int(eq_config.get('Selections', 'treble_hz_sel'))
middle_q_sel = int(eq_config.get('Selections', 'middle_q_sel'))
bass_q_sel = int(eq_config.get('Selections', 'bass_q_sel'))
middle_hz_sel = int(eq_config.get('Selections', 'middle_hz_sel'))
bass_hz_sel = int(eq_config.get('Selections', 'bass_hz_sel'))

input_gain = int(eq_config.get('Gain', 'input_gain'))
treble_gain = int(eq_config.get('Gain', 'treble_gain'))
middle_gain = int(eq_config.get('Gain', 'middle_gain'))
bass_gain = int(eq_config.get('Gain', 'bass_gain'))
sub_gain = int(eq_config.get('Gain', 'sub_gain'))
fr_gain = int(eq_config.get('Gain', 'fr_gain'))
fl_gain = int(eq_config.get('Gain', 'fl_gain'))
rr_gain = int(eq_config.get('Gain', 'rr_gain'))
rl_gain = int(eq_config.get('Gain', 'rl_gain'))

#write values to i2c chip

i2cbus.write_byte_data(0x44, 0x00, 128 + input_sel+ input_gain) #input reg
i2cbus.write_byte_data(0x44, 0x01, 0x00)    #update loudness
i2cbus.write_byte_data(0x44, 0x02, 40)      #update volume
i2cbus.write_byte_data(0x44, 0x03, 128 + treble_gain + treble_hz_sel) #treble reg
i2cbus.write_byte_data(0x44, 0x04, middle_q_sel + middle_gain) #middle reg
i2cbus.write_byte_data(0x44, 0x05, bass_q_sel + bass_gain) #bass reg
i2cbus.write_byte_data(0x44, 0x06, 32 + middle_hz_sel + bass_hz_sel) #bass/mid fc reg
i2cbus.write_byte_data(0x44, 0x07, vol_map.get(fl_gain)) #middle reg   
i2cbus.write_byte_data(0x44, 0x08, vol_map.get(rl_gain)) #bass/mid fc reg
i2cbus.write_byte_data(0x44, 0x09, vol_map.get(rr_gain)) #bass reg
i2cbus.write_byte_data(0x44, 0x0A, vol_map.get(fr_gain)) #treble reg
i2cbus.write_byte_data(0x44, 0x0B, vol_map.get(sub_gain)) #input reg
i2cbus.write_byte_data(0x44, 0x0C, 0x1F)   # Update soft mute register
i2cbus.write_byte_data(0x44, 0x0D, 0x82)   # Update testing register
