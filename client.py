import socket
from tkinter import *
import tkinter


# In this Line we define our local host
# address with port number
from tkinter.ttk import Combobox

SERVER = "127.0.0.1"
PORT = 8081

# Making a socket instance

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))
# Running a infinite loop
choice=-1
root = Tk()
root.title("Client")
root.geometry("800x600")
#initializing combobox
optionslist=[" Convert IP address to binary","Convert subnet mask to binary ","Wildcard","Wildcard in binary","NetworkID in binary","NetworkID in Decimal","BroadcastIP in Binary","BroadcastIP in Decimal","Maximum IP address in network(in Binary)","Maximum IP address in network(in Decimal)","Minimum IP address in network(in Binary)","Minimum IP address in network(in Decimal) "]
optionsdict={"Enter a choice!":0," Convert IP address to binary":1,"Convert subnet mask to binary ":2,"Wildcard":3,"Wildcard in binary":4,"NetworkID in binary":5,"NetworkID in Decimal":6,"BroadcastIP in Binary":7,"BroadcastIP in Decimal":8,"Maximum IP address in network(in Binary)":9,"Maximum IP address in network(in Decimal)":10,"Minimum IP address in network(in Binary)":11,"Minimum IP address in network(in Decimal) ":12}
options =Combobox(root, width=45,value=optionslist,justify="center")
options.set("Enter a choice!")
options.place(x=200,y=300)
#setting up labels
font1=('Arial',12)
ip_label=Label(text="Enter IP address",font=font1).place(x= 20,y= 100)
sub_labes=Label(text="Enter Subnet Mask",font=font1).place(x= 20,y= 200)
options_labes=Label(text="Select a mode",font=font1).place(x= 20,y= 300)
#print("Example : 192.234.56.43")
# here we get the input from the user

#print("Type '13' to terminate")

#input("Enter choice for Compute!\n 1.Convert IP address to binary\n 2.Convert subnet mask to binary \n 3.Wildcard \n 4.Wildcard in binary\n 5.NetworkID in binary\n 6.NetworkID in Decimal\n 7.BroadcastIP in Binary\n 8.BroadcastIP in Decimal\n 9.Maximum IP address in network(in Binary)\n 10.Maximum IP address in network(in Decimal)\n 11.Minimum IP address in network(in Binary)\n 12.Minimum IP address in network(in Decimal)\n 13.Over\n")
inp=StringVar()
ip=Entry(root,textvariable=inp,width=20) # entry
ip.place(x= 200,y= 100)
sub=StringVar()
subnet=Entry(root,textvariable=sub,width=20) # entry
subnet.place(x= 200,y= 200)
answer=StringVar()
ans=Entry(root,textvariable=answer,width=50) # entry
ans.place(x= 200,y= 400)

#inp = input("Enter IP address: ")
#sub = input("enter subnet mask: ")
# If user wants to terminate
# the server connection he can type Over
# Here we send the user input
# to server socket by send Method
def compute():

    choice = optionsdict[options.get()]
    client.sendall(str.encode("\n".join([str(ip.get()),str(subnet.get()),str(choice)])))
    print(str(ip.get()),str(subnet.get()),str(choice))
    # Here we received output from the server socket
    answer_recv = client.recv(1024)
    answer.set(answer_recv.decode())
    if choice==13:
        client.close()
    #print("Type 'Over' to terminate")
compute_button=Button(root,text="Calculate",command=compute).place(x=200,y=500)
root.mainloop()
