#!/usr/bin/python3.6

def display_address(address_type, octets_index, octets_list):
    octets_list[active_octet_index] = str(address_type)
    return '.'.join(octets_list)
        

        


def reset_octets_list(octets_list, active_octet_index, by_value):
    return str(int(octets_list[active_octet_index]) + by_value)

#arbitrary addresses
ip_address1 = "192.168.16.15/5"
ip_address2 = "192.168.4.36/27"

#retrieve an address and a mask
address_list = ip_address1.split('/')
octets_list = address_list[0].split('.')
subnet_mask = int(address_list[1])

#get important subnet info
byte = 8
active_octet_index = subnet_mask // byte
active_octet_subnet_bits = subnet_mask % 8
remainding_octets = 3 - active_octet_index
print(remainding_octets)
#work with the active octet
active_octet = int(octets_list[active_octet_index])

#get the full on binary octet
full_octet = '11111111'
active_octet_binary_representation = f'{active_octet:b}'

mask = ''

#create a binary representation of a mask
for i in range(8):
    mask = mask + '1' if i < active_octet_subnet_bits else mask + '0'

#calculate and display a network id
active_octet_value = int(mask,2) & int(active_octet_binary_representation,2)
octets_list[active_octet_index] = str(active_octet_value)
network_id = '.'.join(octets_list)
#print(active_octet_value)

#calculate first legal address
first_legal_address = int(octets_list[active_octet_index]) + 1
#calculate addresses range
addresses_count = int(mask,2) ^ int(full_octet,2)
octets_list[active_octet_index] = str(active_octet_value)

#calculate the last valid address
broadcast_address = int(octets_list[active_octet_index]) + addresses_count
last_address = broadcast_address - 1

networkId = display_address(active_octet_value, active_octet_index, octets_list)
firstAddress = display_address(first_legal_address, active_octet_index, octets_list)
lastAddress = display_address(last_address, active_octet_index, octets_list)
broadcastAddress = display_address(broadcast_address, active_octet_index, octets_list)

print(f"Based on a following ipv4 address: {ip_address1}")
print("")
print(22*"-"+"RESULTS"+22*"-")
print("")
print(f"Network ID: {networkId}")
print(f"First usable address: {firstAddress}")
print(f"Last usable address: {lastAddress}")
print(f"Broadcast address: {broadcastAddress}")
print("")



