#!/usr/bin/python3.6

class SubnettingCalculator():
    def __init__(self, ipv4_address, cidr_mask):
        
        # Collecting some essential information
        self.ipv4_address = self.set_DDN(ipv4_address)
        self.octets_list = ipv4_address
        self.mask_decimal = cidr_mask
        self.byte = 8
        self.full_ones = self.set_binary("full_ones")
        self.full_address_binary = self.set_binary("binaddress", octets_list=self.octets_list)
        # Get mask in binary
        self.mask_binary = self.set_mask_binary(self.mask_decimal)
        # Network ID
        self.networkId,self.list_binary,self.list_decimal = self.set_networkID()
        # First Address
        self.firstAddress = self.set_firstAddress(self.list_decimal, self.networkId, self.mask_decimal)
        # Last Address
        self.addresses_count = self.set_address_count()
        self.lastAddress, self.last_address_list = self.set_lastAddress(self.addresses_count, self.firstAddress, self.list_binary, self.mask_decimal, self.networkId)
        self.broadcastAddress = self.set_broadcastAddress(self.last_address_list, self.mask_decimal)
        # display informations
        self.display_informations()
    
    def display_informations(self):
        """
        Function displays all of the gathered informations
        """
        print()
        print(f"Based on the following IPv4 address: {self.ipv4_address}")
        print()
        print(22*'-'+'RESULT'+'-'+22*'-')
        print()
        print(f"Network ID: {self.networkId}")
        print(f"First usable address: {self.firstAddress}")
        print(f"Last usable address : {self.lastAddress}")
        print(f"Broadcast address: {self.broadcastAddress}")
        print()
    
    # Setters        
    def set_address_count(self):
        """
        Function returns a number of available addreses within
        the IPv4 Network ID space for a given mask
        """
        if int(self.mask_decimal) == 32:
            return 1
        elif int(self.mask_decimal) == 31:
            return 1
        else:
            return int(self.full_ones,2) - int(self.mask_binary, 2) - 1

    def set_binary(self, option, octets_list=[]):
        """
        Function returns binary representation of: 
        - full_ones: 255.255.255.255 subnet mask
        - binaddress: IPv4 binary representation of a given decimal octets list
        """
        full_ones = ''
        full_address = []
        for i in range(0,4):
            if option == "full_ones" and octets_list == []:
                full_ones += '11111111'
            elif "binaddress":
                full_address.append(format(int(octets_list[i]),'08b'))
        full_address = ''.join(full_address)
        return full_ones if option == "full_ones" else full_address
 
    def set_broadcastAddress(self, last_address_list, mask_decimal):
        """
        Function returns a broadcast address based on a last index of 
        previously obtained last_address_list
        """
        last_address_list[-1] = str(int(last_address_list[-1]) + 1) if mask_decimal < 31 else last_address_list[-1]
        return self.set_DDN(last_address_list)   
   
    def set_DDN(self, binary_list):
        """
        Function returns an address formated in Dotted Decimal Notation
        Functions returns a warning if it is unsuccessful (requires a list
        of four numeric elements)
        """
        if len(binary_list) == 4:
            for i in range(4):
                if binary_list[i].isdecimal():
                    continue
                else:
                    #print("[-] A list of decimal octets is required")
                    return 1
            return '.'.join(binary_list)

    def set_firstAddress(self, list_decimal, networkID, mask_decimal):
        """
        Function returns first valid address from address range
        depending on the length of the mask
        """
        list_decimal[-1] = str(int(list_decimal[-1]) + 1)
        return networkID if mask_decimal == 32 else self.set_DDN(list_decimal)

    def set_lastAddress(self, addresses_count, first_address , list_binary, mask_decimal, networkId):
        """
        Function returns last_address and last_address_list based on a decimal mask
        and previously obtained Network ID
        """
        address_binary = ''.join(list_binary)
        last_address_decimal = int(address_binary,2) + addresses_count
        last_address_binary = format(last_address_decimal, '032b')
        last_address_list = []
        for i in range(4):
            last_address_list.append(str(int(last_address_binary[(self.byte * i):(self.byte * i + self.byte)], 2))) 
        if mask_decimal == 32:
            last_address_list[-1] = networkId.split('.')[-1]
        elif mask_decimal == 31:
            last_address_list[-1] = first_address.split('.')[-1]
        last_address = self.set_DDN(last_address_list)
            
        return last_address, last_address_list

    def set_mask_binary(self, mask_decimal):
        """
        Function returns a binary representation of a decimal subnet_mask
        """
        mask = ''
        for i in range(0, 32):
            mask += '1' if i < mask_decimal else '0'
        return mask

    def set_networkID(self):
        """
        Function returns Network ID in Doted Decimal Notation format,
        on top of that it also its binary representation and a list
        of each octet value from the Network ID as well.
        """
    
        network_id = int(self.full_address_binary,2) & int(self.mask_binary,2)
        network_id_binary = format(network_id, '032b')
        list_binary = []
        list_decimal = []
    
        for i in range(4):
            list_binary.append(network_id_binary[(i * self.byte):(i * self.byte + self.byte)])
            list_decimal.append(str(int(list_binary[i],2)))
    
        return self.set_DDN(list_decimal), list_binary, list_decimal
    
    #Getters
    def get_addresses_count(self):
        return self.addresses_count

    def get_broadcastAddress(self):
        return self.broadcastAddress
   
    def get_firstAddress(self):
        return self.firstAddress
    
    def get_lastAddress(self):
        return self.lastAddress

    
    def get_networkID(self):
        return self.networkId

   

"""
s = SubnettingCalculator('192.168.4.200',24)
print(s.get_addresses_count())
print(s.get_networkID())
print(s.get_firstAddress())
print(s.get_lastAddress())
print(s.get_broadcastAddress())
"""
