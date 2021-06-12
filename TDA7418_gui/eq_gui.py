#!/usr/bin/env python3

import tkinter as tk
#from tkinter import ttk
from tkinter import *
from smbus import SMBus
i2cbus = SMBus(1)  # Create a new I2C bus
from configparser import ConfigParser
eq_config = ConfigParser()

vol_map = dict([(30,15),(29,14),(28,13),(27,12),(26,11),(25,10),(24,9),(23,8),(22,7),(21,6),
(20,5),(19,4),(18,3),(17,2),(16,1),(15,16),(14,17),(13,18),(12,19),(11,20),(10,21),(9,22),
(8,23),(7,24),(6,25),(5,26),(4,27),(3,28),(2,29),(1,30),(0,96)])


# this is a function to get the selected radio button value
def getRadioButtonValue():
    print("input", 128 + input_sel.get() + input_gain.get())
    print("treble", 128 + treble_gain.get() + treble_hz_sel.get())
    print("middle",middle_q_sel.get() + middle_gain.get())
    print("bass", bass_q_sel.get() + bass_gain.get())
    print("bass/middle hz", 32 + middle_hz_sel.get() + bass_hz_sel.get())
    
    write_i2c()

def getScaleValue(self):
    
    print("input", 128 + input_sel.get() + input_gain.get())
    print("treble", 128 + treble_gain.get() + treble_hz_sel.get())
    print("middle",middle_q_sel.get() + middle_gain.get())
    print("bass", bass_q_sel.get() + bass_gain.get())
    print("bass/middle hz", 32 + middle_hz_sel.get() + bass_hz_sel.get())
    print("sub", sub_gain.get())
    print("fr ", fr_gain.get())
    print("fl ", fl_gain.get())
    print("rr ", rr_gain.get())
    print("rl ", rl_gain.get())
    
    write_i2c()
    
def load_preset1():
    eq_config.read('/home/pi/Documents/eq_file.ini')
    input_sel.set(int(eq_config.get('Selections', 'input_sel')))
    treble_hz_sel.set(int(eq_config.get('Selections', 'treble_hz_sel')))
    middle_q_sel.set(int(eq_config.get('Selections', 'middle_q_sel')))
    bass_q_sel.set(int(eq_config.get('Selections', 'bass_q_sel')))
    middle_hz_sel.set(int(eq_config.get('Selections', 'middle_hz_sel')))
    bass_hz_sel.set(int(eq_config.get('Selections', 'bass_hz_sel')))

    input_gain.set(int(eq_config.get('Gain', 'input_gain')))
    treble_gain.set(int(eq_config.get('Gain', 'treble_gain')))
    middle_gain.set(int(eq_config.get('Gain', 'middle_gain')))
    bass_gain.set(int(eq_config.get('Gain', 'bass_gain')))
    sub_gain.set(int(eq_config.get('Gain', 'sub_gain')))
    fr_gain.set(int(eq_config.get('Gain', 'fr_gain')))
    fl_gain.set(int(eq_config.get('Gain', 'fl_gain')))
    rr_gain.set(int(eq_config.get('Gain', 'rr_gain')))
    rl_gain.set(int(eq_config.get('Gain', 'rl_gain')))
    
    write_i2c()
    
def load_preset2():
    eq_config.read('/home/pi/Documents/eq_file.ini')
    input_sel.set(int(eq_config.get('Selections2', 'input_sel2')))
    treble_hz_sel.set(int(eq_config.get('Selections2', 'treble_hz_sel2')))
    middle_q_sel.set(int(eq_config.get('Selections2', 'middle_q_sel2')))
    bass_q_sel.set(int(eq_config.get('Selections2', 'bass_q_sel2')))
    middle_hz_sel.set(int(eq_config.get('Selections2', 'middle_hz_sel2')))
    bass_hz_sel.set(int(eq_config.get('Selections2', 'bass_hz_sel2')))

    input_gain.set(int(eq_config.get('Gain2', 'input_gain2')))
    treble_gain.set(int(eq_config.get('Gain2', 'treble_gain2')))
    middle_gain.set(int(eq_config.get('Gain2', 'middle_gain2')))
    bass_gain.set(int(eq_config.get('Gain2', 'bass_gain2')))
    sub_gain.set(int(eq_config.get('Gain2', 'sub_gain2')))
    fr_gain.set(int(eq_config.get('Gain2', 'fr_gain2')))
    fl_gain.set(int(eq_config.get('Gain2', 'fl_gain2')))
    rr_gain.set(int(eq_config.get('Gain2', 'rr_gain2')))
    rl_gain.set(int(eq_config.get('Gain2', 'rl_gain2')))
    
    write_i2c()    
    
def savetofile1():
    #put file saving stuff here
    #global eq_config
    eq_config['Selections']['input_sel'] = str(input_sel.get())
    eq_config['Selections']['treble_hz_sel'] = str(treble_hz_sel.get())
    eq_config['Selections']['middle_q_sel'] = str(middle_q_sel.get())
    eq_config['Selections']['bass_q_sel'] = str(bass_q_sel.get())
    eq_config['Selections']['middle_hz_sel'] = str(middle_hz_sel.get())
    eq_config['Selections']['bass_hz_sel'] = str(bass_hz_sel.get())
    
    eq_config['Gain']['input_gain'] = str(input_gain.get())
    eq_config['Gain']['treble_gain'] = str(treble_gain.get())
    eq_config['Gain']['middle_gain'] = str(middle_gain.get())
    eq_config['Gain']['bass_gain'] = str(bass_gain.get())
    eq_config['Gain']['sub_gain'] = str(sub_gain.get())
    eq_config['Gain']['fr_gain'] = str(fr_gain.get())
    eq_config['Gain']['fl_gain'] = str(fl_gain.get())
    eq_config['Gain']['rr_gain'] = str(rr_gain.get())
    eq_config['Gain']['rl_gain'] = str(rl_gain.get())

    with open('/home/pi/Documents/eq_file.ini', 'w') as configfile:
        eq_config.write(configfile)

    print("Saving Config 1")

def savetofile2():
    #put file saving stuff here
    #global eq_config
    eq_config['Selections2']['input_sel2'] = str(input_sel.get())
    eq_config['Selections2']['treble_hz_sel2'] = str(treble_hz_sel.get())
    eq_config['Selections2']['middle_q_sel2'] = str(middle_q_sel.get())
    eq_config['Selections2']['bass_q_sel2'] = str(bass_q_sel.get())
    eq_config['Selections2']['middle_hz_sel2'] = str(middle_hz_sel.get())
    eq_config['Selections2']['bass_hz_sel2'] = str(bass_hz_sel.get())
    
    eq_config['Gain2']['input_gain2'] = str(input_gain.get())
    eq_config['Gain2']['treble_gain2'] = str(treble_gain.get())
    eq_config['Gain2']['middle_gain2'] = str(middle_gain.get())
    eq_config['Gain2']['bass_gain2'] = str(bass_gain.get())
    eq_config['Gain2']['sub_gain2'] = str(sub_gain.get())
    eq_config['Gain2']['fr_gain2'] = str(fr_gain.get())
    eq_config['Gain2']['fl_gain2'] = str(fl_gain.get())
    eq_config['Gain2']['rr_gain2'] = str(rr_gain.get())
    eq_config['Gain2']['rl_gain2'] = str(rl_gain.get())

    with open('/home/pi/Documents/eq_file.ini', 'w') as configfile:
        eq_config.write(configfile)

    print("Saving Config 2")

    
def write_i2c():
    #commented out sections written on boot with "audio_init.py"
    i2cbus.write_byte_data(0x44, 0x00, 128 + input_sel.get() + input_gain.get()) #input reg
    #i2cbus.write_byte_data(0x44, 0x01, 0x00)    #update loudness
    #i2cbus.write_byte_data(0x44, 0x02, 40)      #update volume
    i2cbus.write_byte_data(0x44, 0x03, 128 + treble_gain.get() + treble_hz_sel.get()) #treble reg
    i2cbus.write_byte_data(0x44, 0x04, middle_q_sel.get() + middle_gain.get()) #middle reg
    i2cbus.write_byte_data(0x44, 0x05, bass_q_sel.get() + bass_gain.get()) #bass reg
    i2cbus.write_byte_data(0x44, 0x06, 32 + middle_hz_sel.get() + bass_hz_sel.get()) #bass/mid fc reg
    i2cbus.write_byte_data(0x44, 0x07, vol_map.get(fl_gain.get())) #middle reg   
    i2cbus.write_byte_data(0x44, 0x08, vol_map.get(rl_gain.get())) #bass/mid fc reg
    i2cbus.write_byte_data(0x44, 0x09, vol_map.get(rr_gain.get())) #bass reg
    i2cbus.write_byte_data(0x44, 0x0A, vol_map.get(fr_gain.get())) #treble reg
    i2cbus.write_byte_data(0x44, 0x0B, vol_map.get(sub_gain.get())) #input reg
    #i2cbus.write_byte_data(0x44, 0x0C, 0x01)   # Update soft mute register
    #i2cbus.write_byte_data(0x44, 0x0D, 0x82)   # Update testing register


# Create the main window
root = Tk()
root.attributes ('-zoomed', True)
#root.geometry('853x500') #lcd resolution is 1024x600
root.configure(background= '#222222')
root.title('EQ Tuning')

# Tkinter variable
input_sel = tk.IntVar()
treble_hz_sel = tk.IntVar()
middle_q_sel = tk.IntVar()
bass_q_sel = tk.IntVar()
middle_hz_sel = tk.IntVar()
bass_hz_sel = tk.IntVar()

input_gain = tk.IntVar()
treble_gain = tk.IntVar()
middle_gain = tk.IntVar()
bass_gain = tk.IntVar()
sub_gain = tk.IntVar()
fr_gain = tk.IntVar()
fl_gain = tk.IntVar()
rr_gain = tk.IntVar()
rl_gain = tk.IntVar()

#load config file here
load_preset1()

#color variables
bg_col = '#222222' #grey
fg_col = '#25d5f8' #blue
dis_col = '#96edf8' #light blue
txt_col = '#ffffff' #white


# Create widgets here
input_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Audio Input Selection")
inputgain_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Audio Input Gain Adjustment")
treble_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Treble Ajustments")
middle_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Mids Ajustments")
bass_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Bass Ajustments")
sub_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Subwoofer Volume Level")
fr_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Front Right Speaker")
fl_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Front Left Speaker")
rr_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Rear Right Speaker")
rl_lbl = tk.Label(root, bg=bg_col, foreground=txt_col, font=('arial', 12, 'bold'), text="Rear Left Speaker")

inputscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555', variable=input_gain, width=40, length=355, resolution=8, tickinterval=0, to=120, from_=0, showvalue=0, command=getScaleValue)
treblescale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555', variable=treble_gain, width=40, length=355, resolution=1, tickinterval=0, to=16, from_=31, showvalue=0, command=getScaleValue)
middlescale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=middle_gain, width=40, length=355, resolution=1, tickinterval=0, to=16, from_=31, showvalue=0,command=getScaleValue)
bassscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=bass_gain, width=40, length=355, resolution=1, tickinterval=0, to=16, from_=31, showvalue=0, command=getScaleValue)

frscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=fr_gain, width=40, length=200, resolution=1, tickinterval=0, to=30, from_=0, showvalue=1, command=getScaleValue)
flscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=fl_gain, width=40, length=200, resolution=1, tickinterval=0, to=30, from_=0, showvalue=1, command=getScaleValue)
rrscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=rr_gain, width=40, length=200, resolution=1, tickinterval=0, to=30, from_=0, showvalue=1, command=getScaleValue)
rlscale = tk.Scale(root, orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=rl_gain, width=40, length=200, resolution=1, tickinterval=0, to=30, from_=0, showvalue=1, command=getScaleValue)
subscale = tk.Scale(root,orient=tk.HORIZONTAL, bg=fg_col, troughcolor='#555555',variable=sub_gain, width=40, length=400, resolution=1, tickinterval=0, to=30, from_=0, showvalue=1, command=getScaleValue)

save_button_1 = tk.Button(root,width=7,height=3,bg=fg_col,activebackground=fg_col, font=('arial', 12, 'bold'), text="Save \n Preset 1", command=savetofile1)
save_button_2 = tk.Button(root,width=7,height=3,bg=fg_col,activebackground=fg_col, font=('arial', 12, 'bold'), text="Save \n Preset 2", command=savetofile2)
preset1_button = tk.Button(root,width=7,height=3,bg=fg_col,activebackground=fg_col, font=('arial', 12, 'bold'), text="Load \n Preset 1", command=load_preset1)
preset2_button = tk.Button(root,width=7,height=3,bg=fg_col,activebackground=fg_col, font=('arial', 12, 'bold'), text="Load \n Preset 2", command=load_preset2)

#f8a602
# input radio buttons
inputframe=Frame(root, width=0, height=0, bg='#000000')
INPUTS=[('Pi Audio', 0), (' Radio ', 3), ('Input 1', 1), ('Input 2', 2), ]
for INPUTS, val in INPUTS:
    inputgroup=Radiobutton(inputframe, width=9,height=2, text=INPUTS, indicatoron = 0, variable=input_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, fg='#000000', bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')



# treble khz radio buttons
trebleframe=Frame(root, width=0, height=0, bg='#F0F8FF')
TREBLEHZ=[('10.0 Khz', 0), ('12.5 Khz', 32), ('15.0 Khz', 64), ('17.5 Khz', 96), ]
for TREBLEHZ, val in TREBLEHZ:
    treblegroup=Radiobutton(trebleframe, width=9,height=2,text=TREBLEHZ, indicatoron = 0, variable=treble_hz_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')


# middle q radio buttons
middleframe=Frame(root, width=0, height=0, bg='#F0F8FF')
MIDDLEQ=[('Q 0.50', 0), ('Q 0.75', 32), ('Q 1.00', 64), ('Q 1.25', 96), ]
for MIDDLEQ, val in MIDDLEQ:
    middlegroup=Radiobutton(middleframe, width=9,height=2,text=MIDDLEQ, indicatoron = 0, variable=middle_q_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')


# bass q radio buttons
bassframe=Frame(root, width=0, height=0, bg='#F0F8FF')
BASSQ=[(' Q 1.0 ', 0), ('Q 1.25', 32), (' Q 1.2 ', 64), (' Q 2.0 ', 96), ]
for BASSQ, val in BASSQ:
    bass_group=Radiobutton(bassframe, width=9,height=2,text=BASSQ, indicatoron = 0, variable=bass_q_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')

# middle hz radio buttons
middlehzframe=Frame(root, width=0, height=0, bg='#F0F8FF')
MIDDLEHZ=[('500 HZ', 0), ('1 KHz', 1), ('1.5 KHz', 2), ('2.5 KHz', 3), ]
for MIDDLEHZ, val in MIDDLEHZ:
    middlehz_group=Radiobutton(middlehzframe, width=9,height=2,text=MIDDLEHZ, indicatoron = 0, variable=middle_hz_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')

# bass hz radio buttons
basshzframe=Frame(root, width=0, height=0, bg='#F0F8FF')
BASSHZ=[(' 60 Hz ', 0), (' 80 Hz ', 4), ('100 Hz', 8), ('200 Hz', 12), ]
for BASSHZ, val in BASSHZ:
    basshz_group=Radiobutton(basshzframe, width=9,height=2,text=BASSHZ, indicatoron = 0, variable=bass_hz_sel, value=val,command=getRadioButtonValue, selectcolor=dis_col, bg=fg_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')


# Lay out widgets
input_lbl.place(x=545, y=12) 
inputframe.place(x=455, y=35)
inputgain_lbl.place(x=510, y=85)
inputscale.place(x=450, y=110)

treble_lbl.place(x=200, y=25, anchor = 'center') 
trebleframe.place(x=25, y=35)
treblescale.place(x=20, y=85)

middle_lbl.place(x=200, y=160, anchor = 'center') 
middlehzframe.place(x=25, y=170)
middleframe.place(x=25, y=210)
middlescale.place(x=20, y=260)

bass_lbl.place(x=200, y=330, anchor = 'center') 
basshzframe.place(x=25, y=340)
bassframe.place(x=25, y=380)
bassscale.place(x=20, y=430)

fl_lbl.place(x=445, y=190)
flscale.place(x=420, y=210)

fr_lbl.place(x=650, y=190)
frscale.place(x=630, y=210)

rl_lbl.place(x=445, y=290)
rlscale.place(x=420, y=310)

rr_lbl.place(x=650, y=290)
rrscale.place(x=630, y=310)

sub_lbl.place(x=525, y=390)
subscale.place(x=425, y=410)

save_button_1.place(x=1010, y=50, anchor = 'ne')
save_button_2.place(x=1010, y=150, anchor = 'ne')
preset1_button.place(x=1010, y=300, anchor = 'ne')
preset2_button.place(x=1010, y=400, anchor = 'ne')

#scale.pack(padx=20, pady=80)



# Run forever!
root.mainloop()
