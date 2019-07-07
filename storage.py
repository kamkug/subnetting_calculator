import cli_subCal
import json 
import subprocess 
import sys

class PermanentStorage(): 
    def __init__(self): 
        print("loaded") 
 
    def resultToDict(json_input_file, subCal): 
        """ 
        Function returns Subnetting Calculator's results in a dictionary (JSON) format. 
        It takes addresses and masks from user predefined .json file. The file must be placed  
        inside of an 'input' directory and only the actual file name is required as a parameter  
        to this function. 
        """ 
        addresses_dict = {} 
        infile = "input/" + json_input_file 
        try:
            with open(infile) as addr: 
                addresses = json.load(addr ) 
                for item in addresses["addresses_list"]: 
                    addr_list = [] 
                    s = subCal(item['address'], item['mask']) 
                    addr_list.append({ 
                        "NetworkID": s.get_networkID(), 
                        "FirstAddress": s.get_firstAddress(), 
                        "LastAddress": s.get_lastAddress(), 
                        "BroadcastAddress": s.get_broadcastAddress(), 
                        "AddressesCount": s.get_addresses_count() 
                                }) 
                    name = str('.'.join(item['address'])) + "/" + str(item['mask']) 
                    addresses_dict[name] = addr_list 
            return addresses_dict 
        except:
            print("[-] Please provide an existing input file name")
            sys.exit(2)

    def createJSONOutfile( dictionary, outfile, show_output=False): 
        ofile = "output/" + outfile 
        with open(ofile , "w")  as addr:        
            json.dump(dictionary, addr) 
        if show_output: 
            subprocess.call(f"jq '.' {ofile}", shell=True) 
  
        return f"[+] The {ofile} file was successfully created"
