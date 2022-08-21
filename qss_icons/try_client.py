from ast import Pass
import socket
import threading
import json
class Client(): #threading

    def __init__(self,HOST,PORT):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket object that supports IPv4, TCP Protocol
        # self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.connect((HOST, PORT)) # connect to server
        # self.receiver()
        # self.sender()
        self.thread = threading.Thread(target=self.receiver)
        self.thread.start()
        self.thread2=threading.Thread(target=self.taking_inputs)
        self.thread2.start()
        self.data={'USA': 'Washington D.C.', 'France': 'Paris', 'India': 'New Delhi'}
    
    def receiver(self):
        
        print('Connected!')
        data = bytearray()
        self.s.send(str.encode('Server is working!'))
        while True:
            try:
                self.data = self.s.recv(500)
                if data == 'q':
                    socket.close()
                    break
                self.data=json.loads(data.decode('utf-8'))
                print(data)
                if isinstance(data, dict):
                    print ("dictionary")
                else:
                    print ("no")
            except ConnectionError:
                Pass
                # print('Socket error')
                # break
        return data

    def sender(self, data): 

            self.s.send((bytes(data, 'utf-8')))
            
    def taking_inputs(self):
        while True:
            x=input()
            self.sender(x)

HOST =socket.gethostname() #'192.168.0.163' 
PORT = 4072
client1 = Client(HOST,PORT)  
# client2= Client(HOST,4073)

   
while True :
    print(client1.data['USA'])
