#!/usr/bin/python3
from subCal import *
from tkinter import *

# Implementing functionality
def calculate(event):
    octets_list = address_field.get().split('.')
    counter = 0
    length = len(octets_list)

    if length == 4:
        for i in range (length):
            if not octets_list[i].startswith('0') and octets_list[i].isdecimal() and 0 <= int(octets_list[i]) <= 255:
                counter += 1
            else:
                break
    if counter == 4:
        print(octets_list)
    else:
        print("Provide a correctIpv4 in a DDN form")

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


