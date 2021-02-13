import ipaddress, sys, getopt

#Address format: ip address,network address/mask
#Example: 192.168.10.10,192.168.10.0/24

def compareNetworkAddr(line):
    #Split the ip address and network address
    split1 = line.split(",")
    ip = split1[0]
    network = split1[1]
    #Split the network address and the mask
    split2 = network.split("/")
    mask = split2[1]
    network = split2[0]
    ip += "/" + mask
    print(ip)
    networkaddr = ipaddress.ip_network(ip, strict=False)
    print(networkaddr)
    print(network + "/" + mask)
    #Compares the calculated network address to the on in the txt file
    if str(networkaddr) == network + "/" + mask:
        isCorrect = True
    else:
        isCorrect = False
    return isCorrect

def writeAddresses(input_file, output_file1, output_file2):
    #Reads the addresses on the txt file
    with open(input_file, "r") as file_object:
        lines = file_object.readlines()

    #Creates txt for the correct and incorrect addresses
    with open(output_file1, "w") as file_object:
        file_object.write("Valid IP addresses:\n")

    with open(output_file2, "w") as file_object:
        file_object.write("Incorrect IP addresses:\n")

    validAddresses = 0
    notValidAddresses = 0
    #Counts the amount of correct and incorrect addresses, also writes them to the txt files
    for line in lines:
        if compareNetworkAddr(line.rstrip()):
            validAddresses += 1
            with open(output_file1, "a") as file_object:
                file_object.write(f"Address {validAddresses}: {line} \n")
        else:
            notValidAddresses += 1
            with open(output_file2, "a") as file_object:
                file_object.write(f"Address {notValidAddresses}: {line} \n")

    #Write the total correct and incorrect amount of addresses to each file
    with open(output_file1, "a") as file_object:
        file_object.write(f"Total valid addresses: {validAddresses}")
    
    with open(output_file2, "a") as file_object:
        file_object.write(f"Total incorrect addresses: {notValidAddresses}")

def main(argv):
    input_file = ""
    output_file1 = "Valid-addresses.txt"
    output_file2 = "Incorrect-addresses.txt"
    try:
        opts, args = getopt.getopt(argv, "hi:", ["input_file="])
    except getopt.GetoptError:
        print("python ip_address_checker.py -i <input_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("""python ip_address_checker.py -i <input_file>
            The txt file must be in the following format
            Address format: ip address,network address/mask
            Example: 192.168.10.10,192.168.10.0/24""")
        elif opt in ("-i", "--input_file"):
            input_file = arg
        if input_file != "":
            writeAddresses(input_file, output_file1, output_file2)
            print(f"Check the output files {output_file1} and {output_file2} for results")
            
if __name__ == "__main__":
    main(sys.argv[1:])