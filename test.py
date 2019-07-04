#!/usr/bin/python3.6

#arbitrary addresses
ip_address1 = "172.13.12.3/13"
ip_address2 = "192.168.4.36/27"

#retrieve an address and a mask
address_list = ip_address1.split('/')
octets_list = address_list[0].split('.')
subnet_mask = int(address_list[1])

#get important subnet info
byte = 8
active_octet_index = subnet_mask // byte
remainding_octets = 4 - active_octet_index
active_octet_subnet_bits = subnet_mask
full_ones = ''
full_address = []
for i in range (0, 4):
    full_address.append(format(int(octets_list[i]),'08b'))
    full_ones += '11111111'

full_address_binary = ''.join(full_address)
mask = ''

#create a binary representation of a mask
for i in range(0,32):
    mask = mask + '1' if i < subnet_mask else  mask + '0'



#Network ID
network_id = int(full_address_binary,2) & int(mask,2)
network_id_binary = format(network_id, '032b')
list_binary = [] 
list_decimal = []
for i in range (4):
    
    list_binary.append(network_id_binary[(i * 8): (i * 8 + 8)])
    list_decimal.append(str(int(list_binary[i],2)))

networkId = '.'.join(list_decimal)

#First address
test_list = list_decimal
test_list[-1] = str(int(test_list[-1]) + 1)
first_address = '.'.join(test_list)
test_list = list_binary


#Last address
count_usable_addresses = int(full_ones,2) - int(mask,2) - 1
address = ''.join(test_list)
last_address = int(address,2) + count_usable_addresses
last_address_list = []
last_address_binary = format(last_address,'032b') 
for i in range(4):
    last_address_list.append(str(int(last_address_binary[(8 * i):(8 * i + 8)],2)))

last_address = '.'.join(last_address_list)

#Broadcast address
broadcast_list = last_address_list
broadcast_list[-1] = str(int(broadcast_list[-1]) + 1) 
broadcastAddress = '.'.join(broadcast_list)

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

