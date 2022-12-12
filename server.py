import socket
 
# Here we use localhost ip address
# and port number
LOCALHOST = "127.0.0.1"
PORT = 8081
# calling server socket method
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started\n")
print("Waiting for client request..\n")
# Here server socket is ready for
# get input from the user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
# Running infinite loop
while True:
    
    inp,sub,choice=[str(i) for i in clientConnection.recv(1024).decode('utf-8').split('\n')]
    print("IP address is ",inp)
    print("SubnetMask is ",sub)
    print("Your choice is ",choice)
    list1=[]
    
    print("\nIP adress is recievied")
    
    ip_octets = inp.split('.')
        

    if(len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
        valid1=1

    else:
        valid1=0
        
                       
    
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    
    mask_octets = sub.split('.')
            
    if(len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
        valid2=1

    else:
        valid2=0


    def Int2Bin(integer):
        binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
        return binary

    def complement(number):
        if number == '0':
            number = '1'
        elif number == '.':
            pass
        else:
            number = '0'
        return number

    def find_wildcard(binary_subnet):
        binary_list = list(binary_subnet)
        wildcard = ''.join(complement(binary_list[y]) for y in range(len(binary_list)))
        return wildcard

    def convert_decimal(wildcard_Binary):
        binary = {}
        for x in range(4):
            binary[x] = int(wildcard_Binary.split(".")[x], 2)
        dec = ".".join(str(binary[x]) for x in range(4))
        return dec

    def andOP(IP1, IP2):
        ID_list = {}
        for y in range(4):
            ID_list[y] = int(IP1.split(".")[y]) & int(IP2.split(".")[y])
        ID = ".".join(str(ID_list[z]) for z in range(4))
        return ID

    def orOP(IP1, IP2):
        Broadcast_list = {}
        for z in range(4):
            Broadcast_list[z] = int(IP1.split(".")[z]) | int(IP2.split(".")[z])
        broadcast = ".".join(str(Broadcast_list[c]) for c in range(4))
        return broadcast

    def maxiIP(brdcstIP):
        maxIPs = brdcstIP.split(".")
        if int(brdcstIP.split(".")[3]) - 1 == 0:
            if int(brdcstIP.split(".")[2]) - 1 == 0:
                if int(brdcstIP.split(".")[1]) - 1 == 0:
                    maxIPs[0] = int(brdcstIP.split(".")[0]) - 1
                else:
                    maxIPs[1] = int(brdcstIP.split(".")[1]) - 1
            else:
                maxIPs[2] = int(brdcstIP.split(".")[2]) - 1
        else:
            maxIPs[3] = int(brdcstIP.split(".")[3]) - 1
        return ".".join(str(maxIPs[x]) for x in range(4))

    def miniIP(ntwrkID):
        miniIPs = ntwrkID.split(".")
        if int(ntwrkID.split(".")[3]) + 1 == 256:
            if int(ntwrkID.split(".")[2]) + 1 == 256:
                if int(ntwrkID.split(".")[1]) + 1 == 256:
                    miniIPs[0] = int(ntwrkID.split(".")[0]) + 1
                    miniIPs[1] = 0
                    miniIPs[2] = 0
                    miniIPs[3] = 0
                else:
                    miniIPs[1] = int(ntwrkID.split(".")[1]) + 1
                    miniIPs[2] = 0
                    miniIPs[3] = 0
            else:
                miniIPs[2] = int(ntwrkID.split(".")[2]) + 1
                miniIPs[3] = 0
        else:
            miniIPs[3] = int(ntwrkID.split(".")[3]) + 1
        return ".".join(str(miniIPs[x]) for x in range(4))

    
    if choice == "1":
        if(int(valid1)==1):
            result=Int2Bin(inp)
            t=str(result)
            output=str(t)
            clientConnection.send(output.encode())
        else:
            result="Invalid Input"
            output=str(result)
            clientConnection.send(output.encode())
            

    if choice == "2":
        if(int(valid2==1)):
            result=Int2Bin(sub)
            z=str(result)
            output=str(z)
            clientConnection.send(output.encode())
        else:
            result="Invalid Subnet mask "
            output=str(result)
            clientConnection.send(output.encode())
            
            

    if choice == "3":
        if(int(valid2==1)):
            wildcard_binary = find_wildcard(Int2Bin(sub))
            WildCard = convert_decimal(wildcard_binary)
            output=str(WildCard)
            clientConnection.send(output.encode())
        else:
            result="Invalid Subnet mask "
            output=str(result)
            clientConnection.send(output.encode())
            


    if choice == "4":
        if(int(valid2==1)):
            wildcard_binary =find_wildcard(Int2Bin(sub))
            output=str(wildcard_binary)
            clientConnection.send(output.encode())
        else:
            result="Invalid Subnet mask "
            output=str(result)
            clientConnection.send(output.encode())
            

    if choice == "5":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            network_Binary = Int2Bin(networkID)
            output=str(network_Binary)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())
            

    if choice == "6":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            output=str(networkID)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())
            

    
    if choice == "7":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            wildcard_binary = find_wildcard(Int2Bin(sub))
            WildCard = convert_decimal(wildcard_binary)
            broadcastIP = orOP(networkID, WildCard)
            broadcastIP_binary = Int2Bin(broadcastIP)
            output=str(broadcastIP_binary)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())
            
            

    if choice == "8":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            wildcard_binary = find_wildcard(Int2Bin(sub))
            WildCard = convert_decimal(wildcard_binary)
            broadcastIP = orOP(networkID, WildCard)
            output=str(broadcastIP)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())
            

    if choice == "9":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            wildcard_binary = find_wildcard(Int2Bin(sub))
            WildCard = convert_decimal(wildcard_binary)
            broadcastIP = orOP(networkID, WildCard)
            maxIP = maxiIP(broadcastIP)
            maxIP_binary = Int2Bin(maxIP)
            output=str(maxIP_binary)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())

            

    if choice == "10":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            wildcard_binary = find_wildcard(Int2Bin(sub))
            WildCard = convert_decimal(wildcard_binary)
            broadcastIP = orOP(networkID, WildCard)
            maxIP = maxiIP(broadcastIP)
            output=str(maxIP)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())
        
        

    if choice == "11":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            minIP = miniIP(networkID)
            minIP_binary = Int2Bin(networkID)
            output=str(minIP_binary)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())

    if choice == "12":
        if(int(valid1==1) and int(valid2==1)):
            networkID = andOP(inp,sub)
            minIP = miniIP(networkID)
            output=str(minIP)
            clientConnection.send(output.encode())
        else:
            result="Invalid IP or Subnet mask"
            output=str(result)
            clientConnection.send(output.encode())

    if choice == "13":
        result="connection closed"
        output=str(result)
        clientConnection.send(output.encode())
        break
        
        
        
    
clientConnection.close()
            
            
            

 

    
    
