#!/usr/bin/python3

from cli_subCal import *
from tkinter import *

class SubnettingCalculatorDisplay():
    
    def __init__(self):
        # Initialize a high-level window object
        self.window = Tk()
        # Initialize diplay elements
        self.address_label, self.address_field = self.set_label_and_entry(self.window, "IPv4 address (192.168.0.0 default): ", 10, 20, "IPv4 address", 300, 20)     
        self.mask_decimal_label, self.mask_decimal_field = self.set_label_and_entry(self.window, "Subnet mask in decimal form (24 default): ", 10, 60, "Subnet mask", 300, 60)     
        self.notice_label, self.notice_field = self.set_label_and_entry(self.window, "Notice box: ", 10, 300, "Notice Box:", 100, 300, 50)
        self.networkID_label, self.networkID_field = self.set_label_and_entry(self.window, "Network ID:", 150, 160, "Network address", 300, 160)
        self.firstAddress_label, self.firstAddress_field = self.set_label_and_entry(self.window, "First address:", 150, 190, "First address", 300, 190)
        self.lastAddress_label, self.lastAddress_field = self.set_label_and_entry(self.window, "Last address:", 150, 220, "Last address", 300, 220)
        self.broadcastAddress_label, self.broadcastAddress_field = self.set_label_and_entry(self.window, "Broadcast address:", 150, 250, "Broadcast address", 300, 250)
        # Button that invokes the calculation
        self.calculation_button = Button(self.window, text="Calculate")
        self.calculation_button.place(x=335, y=100, width=100)
        self.calculation_button.bind('<Button-1>', self.calculate)
        # Finalise the window creation
        self.window.title("Subnetting calculator")
        self.window.geometry('600x400+10+10')
        self.window.mainloop()

 
    # Implementing functionality
    def calculate(self, event):
        """
        Function collects and verifies user inputs from address and mask fields and
        subsequently provides the output 
        """
    
        self.notice_field.delete(0, 'end')
        octets_list = self.address_field.get().split('.')
        mask_decimal = 0
    
        try:
            
            if 0 <= int(self.mask_decimal_field.get()) <= 32:
                mask_decimal = int(self.mask_decimal_field.get())
            else:
                self.notice_field.insert(END, "Using default mask of 24;")
                mask_decimal = 24        
        except:
            mask_decimal = 24
            self.notice_field.insert(END, "Using default mask of 24; ")
        
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
            self.notice_field.insert(END, "Using default address 192.168.0.0; ")
        else:
            self.notice_field.insert(END, "Provide a correct IPv4 address in a DDN form;")
            print("Provide a correct IPv4 address in a DDN form")    
    
        if counter == 4:
            Sub = SubnettingCalculator(octets_list, mask_decimal)
            self.insert_text(self.networkID_field, Sub.get_networkID())
            self.insert_text(self.firstAddress_field, Sub.get_firstAddress())
            self.insert_text(self.lastAddress_field, Sub.get_lastAddress())
            self.insert_text(self.broadcastAddress_field, Sub.get_broadcastAddress())

        self.window.mainloop()

    def set_label_and_entry(self, window_object, label_text, label_xPos, label_yPos, entry_text, entry_xPos, entry_yPos, width=20):
        """
        Function will return a label and an entry object according
        to predefined values
        """
        label = Label(window_object, text=label_text)
        label.place(x=label_xPos, y=label_yPos)
        entry_field = Entry(window_object, text=entry_text, width=width)
        entry_field.place(x=entry_xPos, y=entry_yPos)
        return label, entry_field       

    def insert_text(self, field, text):
        """
        Function clears and susequently populates a selected field
        """
        field.delete(0, 'end')
        field.insert(END, text)


#window = Tk()
display = SubnettingCalculatorDisplay()
