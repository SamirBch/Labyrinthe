import random, json, socket, threading

class ServerAI:
    game_server = None
    server_AI_port = None
    server_AI_adress = None
    player_name = None
    player_matricule = None
    

    def __init__(self, game_server, server_AI_port, server_AI_adress, player_name, player_matricule):
        self.game_server = game_server #('localhost', 3000)
        self.server_AI_port = server_AI_port
        self.server_AI_adress = server_AI_adress
        self.player_name = player_name
        self.player_matricule = player_matricule

        
    def send_subscribe_request_to_server(self):
        s = socket.socket()
        s.connect(self.game_server)
        request = self.get_subscribe_request()
        s.send(request.encode())
        s.close()
        print("subscribe request sended")
    
    def get_subscribe_request(self):
        request = {
        'request': 'subscribe',
        'port': self.server_AI_port,
        'name': self.player_name,
        'matricules': [self.player_matricule],
        }
        request = json.dumps(request)
        return request
    
    def get_request_type(self, jsonFile):
        data = json.loads(jsonFile)
        return data["request"]
    
    def get_ping_response(self):
         response = json.dumps({"response": "pong",}).encode()
         return response
    
    def send_response(self, connection, response):
        total = 0
        while total < len(response):
            sent = connection.send(response[total:])
            total += sent
            print('sended')    

    def run_server_AI(self):
        self.send_subscribe_request_to_server()
        s2 = socket.socket()
        s2.bind((self.server_AI_adress, self.server_AI_port))
        s2.listen()
    
        while True:
                con, addr = s2.accept()
                d = con.recv(4096).decode()
                request_type = self.get_request_type(d)
                if request_type == "ping":
                    response = self.get_ping_response()
                    self.send_response(con, response)
                elif request_type == "play":
                    print("play")    














class RandomAI:
    board = None
    position = None
    target = None
    Tile = None
    move_to_play = None
    gate_to_play = None
    tile_to_play = None
    
    def __init__(self, name, port, matricule):
        self.name = name
        self.port = port
        self.matricule = matricule

    def play(self, state):
        self.set_game_state(state)
        possible_moves = self.possible_path()
        if len(possible_moves) > 0:
            self.move_to_play = possible_moves[random.randint(0,len(possible_moves)-1)]
        else:
            self.move_to_play = self.position
        gates = self.not_affecting_random_gates(self.move_to_play, self.position)
        self.gate_to_play = gates[random.randint(0,len(gates)-1)] 
        self.tile_to_play = state["tile"]
        return self.create_server_response()

    def create_server_response(self):
        response = {
            'tile': self.tile_to_play,
            'gate': self.gate_to_play,
            'new_position': self.move_to_play,
         }
        response = json.dumps(response)
        return response

    
    def set_game_state(self, state):
        self.board = state["board"]
        self.position = state["positions"][state["current"]]
        self.target = state["target"]
        self.tile = state["tile"]

    


    def get_neighbors(self, position):
        neighbors = []
        if position == 0 :
            neighbors = [('E',position + 1), ('S',position + 7)]        
        elif position > 0 and position < 6 :
            neighbors = [('E',position + 1), ('W',position - 1), ('S', position + 7)]
        elif position > 42 and position < 48 :
            neighbors = [('W',position - 1), ('E',position + 1), ('N',position - 7)]
        elif position == 6 :
            neighbors = [('W',position - 1), ('S',position + 7)]
        elif position == 42 :
            neighbors = [('E',position + 1), ('N',position - 7)]
        elif position == 48:
            neighbors = [('E',position - 1),('N', position - 7)]    
        elif position %7 == 0 :
            neighbors = [('E',position + 1), ('N',position - 7), ('S',position + 7)]   
        elif position + 1 %7 == 0 :
            neighbors = [('N',position - 7), ('S',position + 7), ('W',position -1)]
        else :
            neighbors = [('E',position + 1), ('W',position - 1), ('S',position + 7), ('N',position - 7)]
        
        return neighbors

    def available_neighbors(self,neighbors, exit_directions):
        available_neighbors = []
        for neighbor in neighbors:
            if neighbor[0] in exit_directions:                     
                available_neighbors.append(neighbor)

        return available_neighbors        

    def possible_path(self):
        tuile = self.board[self.position]
        exits = self.exit_gate(tuile)
   
        neighbors = self.get_neighbors(self.position)
        neighbors = self.available_neighbors(neighbors,exits)
        neighbor_information = []
        for neighbor in neighbors:
            neighbor_tuile = self.board[neighbor[1]]
            neighbor_information.append((neighbor[0],neighbor[1],neighbor_tuile))
        possible_moves = []
        for info in neighbor_information:
            opposite_direction = self.get_opposite_direction(info[0])
            if info[2][opposite_direction]:
                possible_moves.append(info[1])     
        return possible_moves
  

    def exit_gate(self,tuile):
        exits = []
        for direction in ["N", "E", "S", "W"]:
            if tuile[direction]:
                exits.append(direction)
        return exits           


    def get_opposite_direction(self,direction):
        if direction == "N":
            return "S"
        elif direction == "S":
            return "N"
        elif direction == "E":
            return "W"
        else:
            return "E"


    def not_affecting_random_gates(self,destination_position, current_position):
        dico = {
            "A" : [1, 8, 15, 22 , 29, 36, 43],
            "B" : [3, 10, 17, 24, 31, 38, 45],
            "C" : [5, 12, 19, 26, 33, 40, 47],
            "L" : [7, 8, 9, 10, 11, 12, 13],
            "K" : [21, 22, 23, 24, 25, 26, 27],
            "J" : [35, 36, 37, 38, 39, 40, 41]
        }
        gates = []
        for key, value in dico.items():
            if destination_position not in value and current_position not in value:
                gates.append(key)
        return gates       



board =  [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": False, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": 15}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 4}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 5}, {"N": True, "E": False, "S": False, "W": True, "item": 
    12}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 13}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 23}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": True, "W": False, "item": 21}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": False, "W": True, "item": 19}, {"N": True, "E": False, "S": True, "W": True, "item": 9}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": 14}, {"N": False, "E": 
    True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 20}, {"N": False, "E": False, "S": True, "W": True, "item": 17}, {"N": 
    False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 
    10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}]



state = {"players": ["player1", "player2"], "current": 0, "positions": [0, 48], "board": [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": False, 
"S": True, "W": True, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, 
"E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 13}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": 
True, "item": 5}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, 
"W": False, "item": 14}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": 
False, "W": True, "item": 20}, {"N": True, "E": False, "S": True, "W": True, 
"item": 9}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 15}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": False, "W": True, "item": None}], "tile": {"N": True, "E": False, "S": True, "W": False, "item": None}, "target": 17, "remaining": [4, 4]}

#player1 = RandomAI("sam", 8888, "20053")
#player2 = RandomAI("ammar", 8889, "1010")
#print(player1.play(state))

#thread = threading.Thread(target=player1.connect_to_server, daemon=True)
#thread.start()
#player2.connect_to_server()


server = ServerAI(("localhost", 3000), 8888, "localhost", "samir", 20053)
server.run_server_AI()