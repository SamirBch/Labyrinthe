import socket, json

def receveid(jsonFile):
    data = json.loads(jsonFile)
    print(type(data),data)
    if data["request"] == "ping":
         return True
    else:
         return False 

 
s = socket.socket()
s.connect(("localhost", 3000))
s.send(
    json.dumps(
        {
            "request": "subscribe",
            "port": 8888,
            "name": "player2",
            "matricules": ["1234"],
        }
    ).encode()
)
d = s.recv(4096).decode()
print(d)
 
s2 = socket.socket()
s2.bind(("0.0.0.0", 8888))
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
