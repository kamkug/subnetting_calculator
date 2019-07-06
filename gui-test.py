#!/usr/bin/python3

from functools import partial
from subCal import *
from tkinter import *

# Implementing functionality
def calculate(event):
    octets_list = address_field.get().split('.')
    mask_decimal = int(mask_decimal_field.get())
    Sub = ''    
    counter = 0
    length = len(octets_list)

    if length == 4:
        for i in range (length):
            if  octets_list[i].isdecimal() and 0 <= int(octets_list[i]) <= 255:
                counter += 1
            else:
                break
            
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
        
    else:
        print("Provide a correct Ipv4 in a DDN form")

# Initialise a high-level window object
window = Tk()
# Add an address input field
address_label = Label(window, text="Provide an IPv4 address in a DDN format:")
address_label.place(x=10 , y=20)
address_field = Entry(window, text="Ip address")
address_field.place(x=300, y=20)
# Add a subnet mask input field
mask_decimal = Label(window, text="Provide a subnet mask in its decimal form:")
mask_decimal.place(x=10, y=60)
mask_decimal_field = Entry(window, text="Subnet mask")
mask_decimal_field.place(x=300, y=60)
# Button that invokes calculation 
calculation_button = Button(window, text="Calculate")
calculation_button.place(x=335, y=100, width=100)
calculation_button.bind('<Button-1>', calculate)
# Present the result
networkID_label = Label(window, text="Network ID:")
networkID_label.place(x=150, y=160)
networkID_field = Entry(window, text="Network ID")
networkID_field.place(x=300, y=160)

firstAddress_label = Label(window, text="First address:")
firstAddress_label.place(x=150, y=190)
firstAddress_field = Entry(window, text="First address")
firstAddress_field.place(x=300, y=190)

lastAddress_label = Label(window, text="Last address:")
lastAddress_label.place(x=150, y=220)
lastAddress_field = Entry(window, text="Last address")
lastAddress_field.place(x=300, y=220)

broadcastAddress_label = Label(window, text="Broadcast address:")
broadcastAddress_label.place(x=150, y=250)
broadcastAddress_field = Entry(window, text="Broadcast address")
broadcastAddress_field.place(x=300, y=250)


window.title("Subnetting calculator")
window.geometry('600x400+10+10')
window.mainloop()


