import socket, time, json

def receveid(jsonFile):
    data = json.loads(jsonFile)
    print(type(data),data)
    if data["request"] == "ping":
         return True
    else:
         return False 


s = socket.socket()
address = ('localhost', 3000)
s.connect(address)
print('connected')


msgdict = {
   'request': 'subscribe',
   'port': 8889,
   'name': 'player1',
   'matricules': ['20053'],
}


msgJson = json.dumps(msgdict)
s.send(msgJson.encode())
s.close()

s2 = socket.socket()
s2.bind(('localhost', 8889 ))
s2.listen()


while True:
        con, addr = s2.accept()
        d = con.recv(4096).decode()
        print(d)
        pong = json.dumps(
            {
                "response": "pong",
            }
        ).encode()
        print("Sending pong")
        if receveid(d):    
            total = 0
            while total < len(pong):
                sent = con.send(pong[total:])
                total += sent
            print('sended')
            
            
     