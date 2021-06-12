#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
import time
import Si4703 #import the driver Allan created. https://github.com/accutron/Si4703
from smbus import SMBus
i2cbus = SMBus(1)  # Create a new I2C bus
from configparser import ConfigParser
fm_file = ConfigParser()


#Si4703.initialize() #initialize i2c for radio


def updateInput():# audio source select TDA7418 chip
    i2cbus.write_byte_data(0x44, 0x00, 128 + input_sel.get()) #input reg

def getRadioButtonValue():
    fm_chan_slider.set(fm_chan.get() + 1)
    set_channel()
    
def getScaleValue(self):
    fm_chan.set(fm_chan_slider.get() - 1)
    set_channel()
    
def preset1():
    if pb_counter.get() == 0:
        pb_counter.set(1)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
def preset2():
    if pb_counter.get() == 0:
        pb_counter.set(2)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
def preset3():
    if pb_counter.get() == 0:
        pb_counter.set(3)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
def preset4():
    if pb_counter.get() == 0:
        pb_counter.set(4)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
def preset5():
    if pb_counter.get() == 0:
        pb_counter.set(5)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
def preset6():
    if pb_counter.get() == 0:
        pb_counter.set(6)
        start_time.set(time.time_ns())
    current_time.set(time.time_ns())
    
def long_press():
    if pb_counter.get() > 0:
        if current_time.get() - start_time.get() > 2000000000: # 2 secs
            if pb_counter.get() ==1:
                preset1_var.set(fm_chan_dspl.get())
            if pb_counter.get() ==2:
                preset2_var.set(fm_chan_dspl.get())
            if pb_counter.get() ==3:
                preset3_var.set(fm_chan_dspl.get())
            if pb_counter.get() ==4:
                preset4_var.set(fm_chan_dspl.get())
            if pb_counter.get() ==5:
                preset5_var.set(fm_chan_dspl.get())
            if pb_counter.get() ==6:
                preset6_var.set(fm_chan_dspl.get())
            pb_counter.set(0)
            savetofile()
    if pb_counter.get() > 0:
        if time.time_ns() - current_time.get() < 2000000000: # 2 secs
            if time.time_ns() - current_time.get() > 100000000: # 0.1 secs
                if pb_counter.get() ==1:
                    fm_chan.set(preset1_var.get() * 10)
                    set_channel()
                if pb_counter.get() ==2:
                    fm_chan.set(preset2_var.get() * 10)
                    set_channel()
                if pb_counter.get() ==3:
                    fm_chan.set(preset3_var.get() * 10)
                    set_channel()
                if pb_counter.get() ==4:
                    fm_chan.set(preset4_var.get() * 10)
                    set_channel()
                if pb_counter.get() ==5:
                    fm_chan.set(preset5_var.get() * 10)
                    set_channel()
                if pb_counter.get() ==6:
                    fm_chan.set(preset6_var.get() * 10)
                    set_channel()                    
                pb_counter.set(0)
    root.after(100, long_press)
    
def savetofile():
    #put file saving stuff here
    #global fm_file
    fm_file['Selections']['preset_1'] = str(preset1_var.get())
    fm_file['Selections']['preset_2'] = str(preset2_var.get())
    fm_file['Selections']['preset_3'] = str(preset3_var.get())
    fm_file['Selections']['preset_4'] = str(preset4_var.get())
    fm_file['Selections']['preset_5'] = str(preset5_var.get())
    fm_file['Selections']['preset_6'] = str(preset6_var.get())

    with open('/home/pi/Documents/fm_file.ini', 'w') as configfile:
        fm_file.write(configfile)

    print("Saving Config")

def loadfromfile():
    fm_file.read('/home/pi/Documents/fm_file.ini')
    preset1_var.set(float(fm_file.get('Selections', 'preset_1')))
    preset2_var.set(float(fm_file.get('Selections', 'preset_2')))
    preset3_var.set(float(fm_file.get('Selections', 'preset_3')))
    preset4_var.set(float(fm_file.get('Selections', 'preset_4')))
    preset5_var.set(float(fm_file.get('Selections', 'preset_5')))
    preset6_var.set(float(fm_file.get('Selections', 'preset_6')))
    
def scan_up():
    rds_dspl.set("FM Radio      ")
    chan = Si4703.seek(1)
    pb_flag.set(1)
    get_status()
   
def scan_down():
    rds_dspl.set("FM Radio      ")
    chan = Si4703.seek(0)
    pb_flag.set(1)
    get_status()
    
def tune_up():
    fm_chan.set(fm_chan.get() + 2)
    if fm_chan.get() > 1079:
        fm_chan.set(1079)
    fm_chan_slider.set(fm_chan.get() + 1)
    set_channel()
       
def tune_down():
    fm_chan.set(fm_chan.get() - 2)
    if fm_chan.get() < 875:
        fm_chan.set(875)
    fm_chan_slider.set(fm_chan.get() + 1)
    set_channel()

def colors_pb():
    print("colors")
    window = Toplevel(root)
    window.configure(background= '#222222')
    window.title('Colors')
    
def exit_pb():
    i2cbus.write_byte_data(0x44, 0x00, 128 + 0) #set audio source back to pi
    root.destroy()
def eq_pb():
    print("eq")

def init_button(): #re-initialise fm chip if things go wrong
    i2cbus.write_byte_data(0x44, 0x00, 128 + 2) #change to different audio source. this is to remove poping noise when fm chip boots
    Si4703.initialize()
    time.sleep(0.5)
    i2cbus.write_byte_data(0x44, 0x00, 128 + 3) #change to fm radio audio source
      
def set_channel():
    rds_dspl.set("FM Radio      ")
    data = Si4703.goToChannel(fm_chan.get())
    chan = data[0]
    stereo = data[1]
    rssi = data[2]
    fm_chan.set(chan)
    fm_chan_dspl.set(chan / 10)
    signal_var.set(rssi)   
    print(fm_chan.get())
    if stereo == 1:
        stereo_dspl.set("(( Stereo ))")
    else:
        stereo_dspl.set("Mono")
    
def get_status():
    data = Si4703.getChannel()
    chan = data[0]
    stereo = data[1]
    rssi = data[2]
    fm_chan.set(chan) #update fm for tune up/down buttons
    fm_chan_dspl.set(chan / 10) #update fm channel display
    fm_chan_slider.set(fm_chan.get() + 1) #update slider
    signal_var.set(rssi / 2)
    if signal_var.get() < counter.get(): #reset signal bar
        signal_dspl.set("|")
        counter.set(0)
    signal_strenght()
    if stereo == 1:
        stereo_dspl.set("(( Stereo ))")
    else:
        stereo_dspl.set("Mono")
    rds_data = Si4703.readRDS()
    rds_data = rds_data[0:8]
    curr_rds.set(rds_data)
    if curr_rds.get() != prev_rds.get(): #not equal to (print text when it changes)
        prev_rds.set(curr_rds.get())
        rds_dspl.set(rds_dspl.get() + curr_rds.get())
    if pb_flag.get() == 0:
        root.after(2000, get_status) #rechedule in 2 secs
    else:
        pb_flag.set(0)


def signal_strenght():
    if signal_var.get() > counter.get():
        signal_dspl.set(signal_dspl.get() + "|")
        counter.set(counter.get() + 1)
        signal_strenght()
        

init_button() #initialise fm chip

# Create the main window
root = Tk()
root.attributes ('-zoomed', True) #lcd resolution is 1024x600
root.configure(background= '#222222')
root.title('FM Radio')


# Tkinter variable
fm_chan = tk.IntVar() #raw fm channel value
fm_chan_slider = tk.IntVar() #raw fm channel value +1 for the slider 
input_sel = tk.IntVar() #audio source seletion
fm_chan_dspl = tk.DoubleVar() #formated fm channel display
signal_var = tk.IntVar() #signal streght display
stereo_dspl = tk.StringVar() #stereo / mono
signal_dspl = tk.StringVar() #signal streght
rds_dspl = tk.StringVar() #rds display
curr_rds = tk.StringVar()
prev_rds = tk.StringVar() 
counter = tk.IntVar() #used for signal streght drawing
pb_flag = tk.IntVar()#flag for get status loop rescheduling
pb_counter = tk.IntVar() #preset counter
start_time = tk.IntVar() #used for long press
current_time = tk.IntVar() #used for long press
preset1_var = tk.DoubleVar() #formated fm channel display
preset2_var = tk.DoubleVar() #formated fm channel display
preset3_var = tk.DoubleVar() #formated fm channel display
preset4_var = tk.DoubleVar() #formated fm channel display
preset5_var = tk.DoubleVar() #formated fm channel display
preset6_var = tk.DoubleVar() #formated fm channel display

# things to initiallise
pb_flag.set(0)
signal_var.set(0)
counter.set(0)
pb_counter.set(0)
signal_dspl.set("|")
input_sel.set(3)

#load presets and last channel

#preset1_var.set(92.7)
#preset2_var.set(93.5)
#preset3_var.set(95.5)
#preset4_var.set(93.5)
#preset5_var.set(105.3)
#preset6_var.set(107.9)

loadfromfile()

fm_chan.set(preset1_var.get() * 10)

set_channel() #set initial fm channel

# Color variable
bg_col = '#222222' #grey #222222
fg_col = '#25d5f8' #blue #25d5f8
dis_col = '#96edf8' #light blue #96edf8  brown #945217 
txt_col = '#FFFFFF' #white
txt2_col = '#f89c02' #orange


# Create widgets here
rssi_var_lbl = tk.Label(root, bg = '#444444', width= 22, foreground= txt_col, anchor = "w", font=('arial', 12, 'bold'), textvariable = signal_dspl)
rssi_lbl = tk.Label(root, bg = bg_col, foreground= txt2_col, font=('Orbitron', 16, 'normal'), text = "FM Signal")
stereo_lbl = tk.Label(root, bg = bg_col, width= 12, foreground= txt2_col, anchor = "center", font=('Orbitron', 16, 'normal'), textvariable = stereo_dspl)
fmchan_lbl = tk.Label(root, bg = bg_col, width=5, foreground= txt_col, font=('open 24 display st ', 100, 'normal'), textvariable = fm_chan_dspl)
rds_lbl = tk.Label(root, bg='#222232', width=23, foreground= txt_col, anchor = "e", font=('arcade', 41, 'normal'), textvariable = rds_dspl)
mhz_lbl = tk.Label(root, bg= bg_col, foreground= txt_col, font=('arial', 20, 'normal'), text = 'MHz')


chan_frame = tk.Frame(root, bg=bg_col)
fmsc1_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 88.9 MHz')
fmsc2_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 92.3 MHz')
fmsc3_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 95.7 MHz')
fmsc4_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 98.9 MHz')
fmsc5_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 102.5 MHz')
fmsc6_lbl = tk.Label(chan_frame, bg= bg_col, foreground= txt2_col, font=('arial', 14, 'normal'), text = '| \n 106.1 MHz')

fm_slider = tk.Scale(root, orient=tk.HORIZONTAL, bg = fg_col, troughcolor='#555555', variable=fm_chan_slider, width=50, length=630, from_=876, to=1080, resolution=2, tickinterval=0, showvalue=0, command=getScaleValue)


scandn_button = tk.Button(root,width=8,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'), text="<<< Scan", command=scan_down)
tunedn_button = tk.Button(root,width=8,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'), text="< Tune", command=tune_down)
eq_button = tk.Button(root,width=6,height=2,bg=fg_col, activebackground=fg_col, font=('Orbitron', 14, 'normal'), text="EQ", command=eq_pb)
exit_button = tk.Button(root,width=6,height=2,bg=fg_col, activebackground=fg_col, font=('Orbitron', 14, 'normal'), text="Exit", command=exit_pb)

scanup_button = tk.Button(root,width=8,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'), text="Scan >>>", command=scan_up)
tuneup_button = tk.Button(root,width=8,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'), text="Tune >", command=tune_up)
colors_button = tk.Button(root,width=6,height=2,bg=fg_col, activebackground=fg_col, font=('Orbitron', 14, 'normal'), text="Colors", command=colors_pb)
init_button = tk.Button(root,width=6,height=2,bg=fg_col, activebackground=fg_col, font=('Orbitron', 14, 'normal'), text="Reboot FM", command=init_button)


preset_frame = tk.Frame(root, bg='#000000')
preset1_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset1_var, command=preset1)
preset2_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset2_var, command=preset2)
preset3_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset3_var, command=preset3)
preset4_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset4_var, command=preset4)
preset5_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset5_var, command=preset5)
preset6_button = tk.Button(preset_frame,width=4,height=3,bg=fg_col, activebackground=fg_col, font=('Orbitron', 16, 'bold'),repeatdelay = 100, repeatinterval = 100, textvariable=preset6_var, command=preset6)



# input radiobuttons
inputframe=Frame(root, width=0, height=0, bg='#000000')
INPUTS=[('Pi Audio', 0), ('FM Radio', 3), ('Aux 1', 1), ('Aux 2', 2), ]
for INPUTS, val in INPUTS:
    inputgroup=Radiobutton(inputframe, width=9,height=3, text=INPUTS, indicatoron = 0, variable=input_sel, value=val,command=updateInput, selectcolor=fg_col, fg='#000000', bg=dis_col, font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')





# Lay out widgets

rssi_var_lbl.place(x=133, y=6)
rssi_lbl.place(x=7, y=2)
stereo_lbl.place(x=840, y=2)
fmchan_lbl.pack(side = tk.TOP)
mhz_lbl.place(x=660, y=50)
rds_lbl.pack(side = tk.TOP)

fm_slider.pack(side = tk.TOP)

chan_frame.pack(side = tk.TOP)
fmsc1_lbl.pack(side = tk.LEFT, padx = 5)
fmsc2_lbl.pack(side = tk.LEFT, padx = 5)
fmsc3_lbl.pack(side = tk.LEFT, padx = 5)
fmsc4_lbl.pack(side = tk.LEFT, padx = 5)
fmsc5_lbl.pack(side = tk.LEFT, padx = 5)
fmsc6_lbl.pack(side = tk.LEFT, padx = 5)

colors_button.place(x=1010, y=125, anchor = 'ne')
scanup_button.place(x=1010, y=200, anchor = 'ne')
tuneup_button.place(x=1010, y=310, anchor = 'ne')
init_button.place(x=1010, y=420, anchor = 'ne')

eq_button.place(x=15, y=125)
scandn_button.place(x=15, y=200)
tunedn_button.place(x=15, y=310)
exit_button.place(x=15, y=420)

preset_frame.pack(side = tk.TOP, pady = 10)
preset1_button.pack(side = tk.LEFT, padx = 2) #x210 y320
preset2_button.pack(side = tk.LEFT, padx = 2)
preset3_button.pack(side = tk.LEFT, padx = 2)
preset4_button.pack(side = tk.LEFT, padx = 2)
preset5_button.pack(side = tk.LEFT, padx = 2)
preset6_button.pack(side = tk.LEFT, padx = 2)

inputframe.pack(side = tk.TOP, pady = 0)



root.after(100, long_press)
root.after(2000, get_status)
# Run forever!
root.mainloop()

