from IA import RandomAI

test_board = [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": True, "S": True, "W": False, "item": 14}, {"N": False, "E": True, "S": True, "W": True, "item": 1}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None},
        {"N": False, "E": False, "S": True, "W": True, "item": 15}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None},
        {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": True, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 5},
        {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 22}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": True, "E": False, "S": False, "W": True, "item": None},
        {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, "W": False, "item": 16}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 9},
        {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 20},
        {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": False, "E": True, "S": True, "W": False, "item": 13}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}]

test_state = {"players": ["player1", "player2"], "current": 0, "positions": [0, 48], "board": [{"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": False, 
"S": True, "W": True, "item": 16}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, 
"E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 12}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 13}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": 
False, "E": True, "S": True, "W": True, "item": 4}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": 
True, "item": 5}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 23}, {"N": True, "E": False, "S": True, "W": True, "item": 21}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": True, "E": True, "S": False, 
"W": False, "item": 14}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": True, "S": 
False, "W": True, "item": 20}, {"N": True, "E": False, "S": True, "W": True, 
"item": 9}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": 15}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 22}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": True, "E": False, "S": False, "W": True, "item": None}], "tile": {"N": True, "E": False, "S": True, "W": False, "item": None}, "target": 17, "remaining": [4, 4]}



def test_create_server_response():
    ia = RandomAI() 
    ia.tile_to_play = ["N", "S"]
    ia.gate_to_play = "L" 
    ia.move_to_play = 42
    expected_response = {"tile": ["N", "S"], "gate": "L", "new_position": 42}
    assert ia.create_server_response() == expected_response


def test_set_games_state():
    ia = RandomAI()
    ia.set_game_state(test_state)
    assert ia.board == test_state["board"]
    assert ia.position == test_state["positions"][test_state["current"]]
    assert ia.target != None
    assert ia.tile == test_state["tile"]

def test_get_neighbors():
    ia = RandomAI()
    neighbors  = ia.get_neighbors(0)
    assert neighbors == [('E', 1), ('S', 7)]
    neighbors  = ia.get_neighbors(1)
    assert neighbors == [('E', 2), ('W', 0), ('S', 8)]
    neighbors  = ia.get_neighbors(43)
    assert neighbors == [('W', 42), ('E', 44), ('N', 36)]
    neighbors  = ia.get_neighbors(6)
    assert neighbors == [('W', 5), ('S', 13)]
    neighbors  = ia.get_neighbors(42)
    assert neighbors == [('E', 43), ('N', 35)]
    neighbors  = ia.get_neighbors(48)
    assert neighbors == [('E', 47), ('N', 41)]
    neighbors  = ia.get_neighbors(7)
    assert neighbors == [('E', 8), ('N', 0), ('S', 14)]
    neighbors  = ia.get_neighbors(13)
    assert neighbors == [('N', 6), ('S', 20), ('W', 12)]
    neighbors  = ia.get_neighbors(8)
    assert neighbors == [('E', 9), ('W', 7), ('S', 15), ('N', 1)]




def test_available_neighbors():
    ia = RandomAI()
    neighbors = ia.get_neighbors(0)
    exit_direction = ia.exit_gate(test_board[0])
    avalaible_neighbors = ia.available_neighbors(neighbors,exit_direction)
    assert avalaible_neighbors == [('E', 1),('S', 7)]
    neighbors = ia.get_neighbors(7)
    exit_direction = ia.exit_gate(test_board[7])
    avalaible_neighbors = ia.available_neighbors(neighbors,exit_direction)
    assert avalaible_neighbors == [('S', 14)]
    neighbors = ia.get_neighbors(25)
    exit_direction = ia.exit_gate(test_board[25])
    avalaible_neighbors = ia.available_neighbors(neighbors,exit_direction)
    assert avalaible_neighbors == [('S', 32),('N', 18)]



def test_exit_gate():
    ia = RandomAI()
    tuile = {"N": True, "E": True, "S": True, "W": True}
    assert ia.exit_gate(tuile) == ["N", "E", "S", "W"]  
    tuile = {"N": False, "E": False, "S": True, "W": True}
    assert ia.exit_gate(tuile) == ["S", "W"]
    tuile = {"N": False, "E": True, "S": False, "W": True}
    assert ia.exit_gate(tuile) == ["E", "W"]
    tuile = {"N": True, "E": True, "S": False, "W": False}
    assert ia.exit_gate(tuile) == ["N", "E"]
    tuile = {"N": False, "E": False, "S": False, "W": False}
    assert ia.exit_gate(tuile) == []


def test_get_opposite_direction():
    ia = RandomAI()
    assert ia.get_opposite_direction("N") == "S"
    assert ia.get_opposite_direction("S") == "N"
    assert ia.get_opposite_direction("W") == "E"
    assert ia.get_opposite_direction("E") == "W"


def test_not_affecting_random_gates():
    ia = RandomAI()
    current = 8
    destination = 10
    result = ia.not_affecting_random_gates(current, destination)
    assert result == ['C', 'K', 'J']
  
