#!/usr/bin/python3

from functools import partial
from subCal import *
from tkinter import *

# Implementing functionality
def calculate(event):
    """
    Function collects and verifies user inputs from address and mask fields and
    subsequently provides the output 
    """
    notice_field.delete(0, 'end')
    octets_list = address_field.get().split('.')
    mask_decimal = 0
    try:
        if 0 <= int(mask_decimal_field.get()) <= 32:
            mask_decimal = int(mask_decimal_field.get())
        else:
            mask_decimal = 24        
    except:
        mask_decimal = 24
        notice_field.delete(0, 'end')
        notice_field.insert(END, "Using default mask of 24")
        
    counter = 0
    length = len(octets_list)

    if length == 4:
        for i in range (length):
            if  octets_list[i].isdecimal() and 0 <= int(octets_list[i]) <= 255:
                counter += 1
            else:
                break
    elif octets_list == ['']:
        octets_list = ['192','168','0','0']
        counter = 4
        notice_field.delete(0, 'end')
        notice_field.insert(END, "Using default address 192.168.0.0/24")
    else:
        notice_field.delete(0, 'end')
        notice_field.insert(END, "Provide a correct IPv4 address in a DDN form")
        print("Provide a correct IPv4 address in a DDN form")    
    
    if counter == 4:
        Sub = SubnettingCalculator(octets_list, mask_decimal)
        networkID_field.delete(0, 'end')
        networkID_field.insert(END,Sub.get_networkID()) 
        firstAddress_field.delete(0, 'end')
        firstAddress_field.insert(END, Sub.get_firstAddress())
        lastAddress_field.delete(0, 'end')
        lastAddress_field.insert(END, Sub.get_lastAddress())
        broadcastAddress_field.delete(0, 'end')
        broadcastAddress_field.insert(END, Sub.get_broadcastAddress())

def get_label_and_entry(window_object, label_text, label_xPos, label_yPos, entry_text, entry_xPos, entry_yPos, width=20):
    """
    Function will return a label and an entry object according
    to predefined values
    """
    label = Label(window_object, text=label_text)
    label.place(x=label_xPos, y=label_yPos)
    entry_field = Entry(window_object, text=entry_text, width=width)
    entry_field.place(x=entry_xPos, y=entry_yPos)
    return label, entry_field       
    

# Initialise a high-level window object
window = Tk()
# Button that invokes the process
# The rest of graphical objects
address_label, address_field = get_label_and_entry(window, "IPv4 address (192.168.0.0 default): ", 10, 20, "Ipv4 address", 300, 20)
mask_decimal_label, mask_decimal_field = get_label_and_entry(window, "Subnet mask in decimal form (24 default): ", 10, 60, "Subnet mask", 300, 60)
notice_label, notice_field = get_label_and_entry(window, "Notice box: ", 10, 300, "Notice Box:", 100, 300, 50)
networkID_label, networkID_field = get_label_and_entry(window, "Network ID:", 150, 160, "Network address", 300, 160)
firstAddress_label, firstAddress_field = get_label_and_entry(window, "First address:", 150, 190, "First address", 300, 190)
lastAddress_label, lastAddress_field = get_label_and_entry(window, "Last address:", 150, 220, "Last address", 300, 220)
broadcastAddress_label, broadcastAddress_field = get_label_and_entry(window, "Broadcast address:", 150, 250, "Broadcast address", 300, 250)
calculation_button = Button(window, text="Calculate")
calculation_button.place(x=335, y=100, width=100)
calculation_button.bind('<Button-1>', calculate)
    
window.title("Subnetting calculator")
window.geometry('600x400+10+10')
window.mainloop()


