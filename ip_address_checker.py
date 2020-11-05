import ipaddress

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

def writeAddresses(filename):
    #Reads the addresses on the txt file
    with open(filename, "r") as file_object:
        lines = file_object.readlines()

    #Creates txt for the correct and incorrect addresses
    filename1 = "Valid-addresses.txt"
    with open(filename1, "w") as file_object:
        file_object.write("Valid IP addresses:\n")

    filename2 = "Incorrect-addresses.txt"
    with open(filename2, "w") as file_object:
        file_object.write("Incorrect IP addresses:\n")

    validAddresses = 0
    notValidAddresses = 0
    #Counts the amount of correct and incorrect addresses, also writes them to the txt files
    for line in lines:
        if compareNetworkAddr(line.rstrip()):
            validAddresses += 1
            with open(filename1, "a") as file_object:
                file_object.write(f"Address {validAddresses}: {line} \n")
        else:
            notValidAddresses += 1
            with open(filename2, "a") as file_object:
                file_object.write(f"Address {notValidAddresses}: {line} \n")

    #Write the total correct and incorrect amount of addresses to each file
    with open(filename1, "a") as file_object:
        file_object.write(f"Total valid addresses: {validAddresses}")
    
    with open(filename2, "a") as file_object:
        file_object.write(f"Total incorrect addresses: {notValidAddresses}")


filename = input("Enter the file name: \n")
writeAddresses(filename)



