import random, json, socket, threading, logging

logging.basicConfig(level=logging.INFO)

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0
    
    def clear_queue(self):
        self.data = []
        


class ServerAI:
    game_server = None
    server_AI_port = None
    server_AI_adress = None
    player_name = None
    player_matricule = None
    AI = None
    

    def __init__(self, game_server, server_AI_port, server_AI_adress, player_name, player_matricule):
        self.game_server = game_server #('localhost', 3000)
        self.server_AI_port = server_AI_port
        self.server_AI_adress = server_AI_adress
        self.player_name = player_name
        self.player_matricule = player_matricule
        self.AI = RandomAI()

        
    def send_subscribe_request_to_server(self):
        s = socket.socket()
        s.connect(self.game_server)
        request = self.get_subscribe_request()
        s.send(request.encode())
        s.close()
        logging.info("Player %s: Subscribe request sended", self.player_name)

    def get_subscribe_request(self):
        request = {
        'request': 'subscribe',
        'port': self.server_AI_port,
        'name': self.player_name,
        'matricules': [self.player_matricule],
        }
        request = json.dumps(request)
        return request
    
    def convert_to_dict(self, jsonFile):
        data = json.loads(jsonFile)
        return data
    
    def get_ping_response(self):
         response = json.dumps({"response": "pong",}).encode()
         return response
    
    def send_response(self, connection, response):
        total = 0
        while total < len(response):
            sent = connection.send(response[total:])
            total += sent
        logging.info("Player %s: response send to %s", self.player_name, self.game_server)    
    
    def get_response(self,connection):
        connection.settimeout(0.1)
        chunks = []
        finished = False
        while not finished:
            try:
                data = connection.recv(4096)
                chunks.append(data)
                finished = data == b''
            except socket.timeout:
                break
        return b''.join(chunks).decode() 

    def get_move_response(self, AI_move):
         response = json.dumps({"response": "move", "move": AI_move, "message": "i will win"}).encode()
         return response

    def run_server_AI(self):
        self.send_subscribe_request_to_server()
        s2 = socket.socket()
        s2.bind((self.server_AI_adress, self.server_AI_port))
        s2.listen()
        logging.info("Player %s: listening on port %s", self.player_name, self.server_AI_port)
    
        while True:
                con, addr = s2.accept()
                #d = con.recv(4096).decode()
                d = self.get_response(con)
                request = self.convert_to_dict(d)
                logging.info("Player %s: got request %s", self.player_name, request["request"])
                if request["request"] == "ping":
                    response = self.get_ping_response()
                    self.send_response(con, response)
                elif request["request"] == "play":
                    AI_move = self.AI.play(request["state"])
                    response = self.get_move_response(AI_move)
                    #print("Ai move = ",AI_move)
                    self.send_response(con, response)
            
                

class RandomAI: 
    board = None
    position = None
    target = None
    Tile = None
    move_to_play = None
    gate_to_play = None
    tile_to_play = None


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
            "tile": self.tile_to_play,
            "gate": self.gate_to_play,
            "new_position": self.move_to_play,
         }
        #response = json.dumps(response)
        return response

    
    def set_game_state(self, state):
        self.board = state["board"]
        self.position = state["positions"][state["current"]]
        self.target = state["target"]
        self.tile = state["tile"]

    
    def get_neighbors(self, position):
        neighbors = []
        if position == 0 :
            neighbors = [('E',position + 1), ('S',position + 7), ('N', position + 42), ('W', position + 6)]        
        elif position > 0 and position < 6 :
            neighbors = [('E',position + 1), ('W',position - 1), ('S', position + 7), ('N', position + 42)]
        elif position > 42 and position < 48 :
            neighbors = [('W',position - 1), ('E',position + 1), ('N',position - 7), ('S', position - 42)]
        elif position == 6 :
            neighbors = [('W',position - 1), ('S',position + 7), ('N', position + 42), ('E', position - 6)]
        elif position == 42 :
            neighbors = [('E',position + 1), ('N',position - 7), ('S', position - 42), ('W', position + 6)]
        elif position == 48:
            neighbors = [('W',position - 1),('N', position - 7), ('S', position - 42), ('E', position - 6)]    
        elif position %7 == 0 :
            neighbors = [('E',position + 1), ('N',position - 7), ('S',position + 7), ('W', position + 6)]   
        elif (position + 1) %7 == 0 :
            neighbors = [('N',position - 7), ('S',position + 7), ('W',position -1), ('E', position - 6)]
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




class AI:
    board = None
    position = 40
    target = 10
    achievable_positions = None
    path_to_target = None
    tile = None
    move_to_play = None
    gate_to_play = None
    tile_to_play = None


    def __init__(self, board):
        self.board = board

    def play(self, state):
        #self.set_game_state(state)
        self.achievable_positions = self.BFS(self.position, self.target)
        if self.is_target_found():
            self.path_to_target = self.get_path()
            gates = self.not_affecting_random_gates(self.path_to_target)
            if len(gates) != 0:
                self.move_to_play = self.path_to_target[0]
                self.gate_to_play = gates[random.randint(0,len(gates)-1)]
            else:
                self.move_to_play = self.get_random_move()
                gates = self.not_affecting_random_gates([self.move_to_play])
                self.gate_to_play = gates[random.randint(0,len(gates)-1)]
        else:
            self.move_to_play = self.get_random_move()
            gates = self.not_affecting_random_gates([self.move_to_play])
            self.gate_to_play = gates[random.randint(0,len(gates)-1)]
        
        self.tile_to_play = self.tile
        return self.create_server_response()

        
    def set_game_state(self, state):
        self.board = state["board"]
        self.position = state["positions"][state["current"]]
        self.target = state["target"]
        self.tile = state["tile"]

    def possible_path(self, position):
        tuile = self.board[position]
        exits = self.exit_gate(tuile)
   
        neighbors = self.get_neighbors(position)
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
    
    def get_neighbors(self, position):
        neighbors = []
        if position == 0 :
            neighbors = [('E',position + 1), ('S',position + 7), ('N', position + 42), ('W', position + 6)]        
        elif position > 0 and position < 6 :
            neighbors = [('E',position + 1), ('W',position - 1), ('S', position + 7), ('N', position + 42)]
        elif position > 42 and position < 48 :
            neighbors = [('W',position - 1), ('E',position + 1), ('N',position - 7), ('S', position - 42)]
        elif position == 6 :
            neighbors = [('W',position - 1), ('S',position + 7), ('N', position + 42), ('E', position - 6)]
        elif position == 42 :
            neighbors = [('E',position + 1), ('N',position - 7), ('S', position - 42), ('W', position + 6)]
        elif position == 48:
            neighbors = [('W',position - 1),('N', position - 7), ('S', position - 42), ('E', position - 6)]    
        elif position %7 == 0 :
            neighbors = [('E',position + 1), ('N',position - 7), ('S',position + 7), ('W', position + 6)]   
        elif (position + 1) %7 == 0 :
            neighbors = [('N',position - 7), ('S',position + 7), ('W',position -1), ('E', position - 6)]
        else :
            neighbors = [('E',position + 1), ('W',position - 1), ('S',position + 7), ('N',position - 7)]   
        return neighbors

    def available_neighbors(self,neighbors, exit_directions):
        available_neighbors = []
        for neighbor in neighbors:
            if neighbor[0] in exit_directions:                     
                available_neighbors.append(neighbor)

        return available_neighbors 

    def get_opposite_direction(self,direction):
        if direction == "N":
            return "S"
        elif direction == "S":
            return "N"
        elif direction == "E":
            return "W"
        else:
            return "E"  

    def exit_gate(self,tuile):
        exits = []
        for direction in ["N", "E", "S", "W"]:
            if tuile[direction]:
                exits.append(direction)
        return exits

    def BFS(self, start_position, target):
        agenda = Queue()
        achievable_positions  = []
        agenda.enqueue(start_position)
        if start_position == target:
            return [(start_position, start_position)]
        while not agenda.isEmpty():
            node = agenda.dequeue() 
            neighbor_positions = self.possible_path(node)
            for neighbor_position in neighbor_positions:
                if not self.positions_in_achievable_positions(neighbor_position, achievable_positions):
                    agenda.enqueue(neighbor_position)
                    achievable_positions.append((neighbor_position, node))
                    if neighbor_position == target:
                        agenda.clear_queue()
                        break           
        return achievable_positions        
        
    def positions_in_achievable_positions(self, position, achievable_positions):
        for achievable_position in achievable_positions:
            if position == achievable_position[0] or position == achievable_position[1]:
                return True
        return False

    def is_target_found(self):
        return len(self.achievable_positions) != 0 and self.achievable_positions[-1][0] == self.target
        
    def get_parent(self, node):               
        return node[1]

    def get_parent_node(self, parent, achievable_positions):
        for node in achievable_positions:
            if node[0] == parent:
                return node

    def get_path(self):
        path = []
        node = self.achievable_positions[-1]
        while node[1] != self.position:
            path.append(node[0])
            parent = self.get_parent(node)
            node = self.get_parent_node(parent, self.achievable_positions)
        path.append(node[0])
        path.append(node[1])
        return path    
    
    def not_affecting_random_gates(self, path):
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
            if len(self.intersection(value, path)) == 0:
                gates.append(key)
        return gates       

    def intersection(self, list1, list2):
        list3 = [value for value in list1 if value in list2]
        return list3

    def create_server_response(self):
        response = {
            "tile": self.tile_to_play,
            "gate": self.gate_to_play,
            "new_position": self.move_to_play,
         }
        #response = json.dumps(response)
        return response


    def get_random_move(self):
        random_moves = self.possible_path(self.position)
        if len(random_moves) != 0:
            return random_moves[random.randint(0,len(random_moves)-1)]
        return self.position






board = [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": True, "S": True, "W": False, "item": 14}, {"N": False, "E": True, "S": True, "W": True, "item": 1}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None},
        {"N": False, "E": False, "S": True, "W": True, "item": 15}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None},
        {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": True, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 5},
        {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 22}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": True, "E": False, "S": False, "W": True, "item": None},
        {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, "W": False, "item": 16}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 6},
        {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 20},
        {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": False, "E": True, "S": True, "W": False, "item": 13}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}]



state = {"players": ["player1", "player2"], "current": 0, "positions": [0, 48], "board": [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": False, 
"S": True, "W": True, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, 
"E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 13}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": 
True, "item": 5}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, 
"W": False, "item": 14}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": 
False, "W": True, "item": 20}, {"N": True, "E": False, "S": True, "W": True, 
"item": 9}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 15}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": False, "W": True, "item": None}], "tile": {"N": True, "E": False, "S": True, "W": False, "item": None}, "target": 17, "remaining": [4, 4]}



player3 = AI(board)
print(player3.play("state"))

'''
player1 = ServerAI(("localhost", 3000), 8888, "localhost", "samir", 20053)
player2 = ServerAI(("localhost", 3000), 8889, "localhost", "ammar", 0000)
thread = threading.Thread(target=player1.run_server_AI, daemon=True)
thread.start()
player2.run_server_AI()
'''
