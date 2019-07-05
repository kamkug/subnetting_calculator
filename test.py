#!/usr/bin/python3.6

#test1 = ['11111111', '11111111' , '11111111', '11111111']

def get_address_count(all_ones, mask_decimal, mask_binary):
    """
    Function returns a number of available addreses within
    the IPv4 Network ID space for a given mask
    """
    #print(mask_decimal)
    if int(mask_decimal) == 32:
        return 1
    elif int(mask_decimal) == 31:
        return 1
    else:
        return int(all_ones,2) - int(mask_binary, 2) - 1

def get_binary(option, octets_list=[]):
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

def get_broadcastAddress(last_address_list):
    """
    Function returns a broadcast address based on a last index of 
    previously obtained last_address_list
    """
    last_address_list[-1] = str(int(last_address_list[-1]) + 1)
    return get_DDN(last_address_list)

def get_DDN(binary_list):
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

def get_firstAddress(list_decimal, networkID, mask_decimal):
    """
    Function returns first valid address from address range
    depending on the length of the mask
    """
    list_decimal[-1] = str(int(list_decimal[-1]) + 1)
    return networkID if mask_decimal == 32 else get_DDN(list_decimal)

def get_lastAddress(addresses_count, list_binary, mask_decimal, networkId):
    """
    Function returns last_address and last_address_list based on a decimal mask
    and previously obtained Network ID
    """
    address_binary = ''.join(list_binary)
    last_address_decimal = int(address_binary,2) + addresses_count
    last_address_binary = format(last_address_decimal, '032b')
    last_address_list = []
    for i in range(4):
        last_address_list.append(str(int(last_address_binary[(byte * i):(byte * i + byte)], 2)))
    last_address = networkId if mask_decimal == 32 else first_address if mask_decimal == 31 else get_DDN(last_address_list)
    return last_address, last_address_list

def get_mask_binary(mask_decimal):
    """
    Function returns a binary representation of a decimal subnet_mask
    """
    mask = ''
    for i in range(0, 32):
        mask += '1' if i < mask_decimal else '0'
    return mask

def get_networkID(full_address_binary, mask_binary):
    """
    Function returns Network ID in Doted Decimal Notation format,
    on top of that it also its binary representation and a list
    of each octet value from the Network ID as well.
    """
    
    network_id = int(full_address_binary,2) & int(mask_binary,2)
    network_id_binary = format(network_id, '032b')
    list_binary = []
    list_decimal = []
    
    for i in range(4):
        list_binary.append(network_id_binary[(i * byte):(i * byte + byte)])
        list_decimal.append(str(int(list_binary[i],2)))
    
    return get_DDN(list_decimal), list_binary, list_decimal

#print(get_DDN(test1))

#arbitrary addresses
ip_address1 = "172.13.12.123/3"
ip_address2 = "192.168.4.36/27"

# retrieve an address and a mask
address_list = ip_address1.split('/')
octets_list = address_list[0].split('.')
mask_decimal = int(address_list[1])
# get important subnet info
byte = 8
full_ones = get_binary("full_ones")
full_address_binary = get_binary("binaddress", octets_list=octets_list)#[]
# get mask in binary
mask_binary = get_mask_binary(mask_decimal)
##print(mask)
##print(get_address_count(full_ones ,subnet_mask,mask))

#Network ID
networkId,list_binary,list_decimal = get_networkID(full_address_binary, mask_binary)

#First Address
first_address = get_firstAddress(list_decimal, networkId, mask_decimal)

#Last addressi 
addresses_count = get_address_count(full_ones,mask_decimal,mask_binary)
last_address, last_address_list = get_lastAddress(addresses_count, list_binary, mask_decimal, networkId)

#Broadcast addressi

broadcastAddress = get_broadcastAddress(last_address_list)

#Display the results
print()
print(f"Based on the following IPv4 address: {ip_address1}")
print()
print(22*'-'+'RESULT'+'-'+22*'-')
print()
print(f"Network ID: {networkId}")
print(f"First usable address: {first_address}")
print(f"Last usable address : {last_address}")
print(f"Broadcast address: {broadcastAddress}")
print()

