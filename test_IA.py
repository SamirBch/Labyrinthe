from IA import AI


#Board from github image
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

def test_set_games_state():
    ia = AI("")
    ia.set_game_state(test_state)
    assert ia.board == test_state["board"]
    assert ia.position == test_state["positions"][test_state["current"]]
    assert ia.target != None
    assert ia.tile == test_state["tile"]

def test_set_target():
    ia = AI("")
    ia.board = test_board
    letter_position = [2,4,14,16,18,20,28,30,32,34,44,46,31,45,3,7,29,26]
    for letter in range(0,17):
        target_index = ia.set_target(letter)
        assert target_index == letter_position[letter]

def test_get_opposite_direction():
    ia = AI("")
    assert ia.get_opposite_direction("N") == "S"
    assert ia.get_opposite_direction("S") == "N"
    assert ia.get_opposite_direction("W") == "E"
    assert ia.get_opposite_direction("E") == "W"

def test_exit_gate():
    ia = AI("")
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

def test_get_neighbors():
    ia = AI("")
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
    ia = AI("")
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

def test_is_target_found():
    ia = AI("")
    ia.achievable_positions = [(1,""),(2,""),(3,""),(4,"")]
    ia.target = 5
    assert ia.is_target_found() == False
    ia.target = 4
    assert ia.is_target_found() == True
    ia.target = 2
    assert ia.is_target_found() == False

def test_get_parent():
    ia = AI("")
    node = (1,2)
    assert ia.get_parent(node) == 2

def test_get_parent_node():
    ia = AI("")
    achievable_positions = [(2, 0), (1, 0), (3, 1)]
    parent = ia.get_parent_node(3, achievable_positions)
    assert parent == (3, 1)

def test_intersection():
    ai = AI("")
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = ai.intersection(list1, list2)
    assert result == [3, 4]

def test_not_affecting_random_gates():
    ia = AI("")
    path = [15, 17, 19, 12]
    result = ia.not_affecting_random_gates(path)
    assert result == ['K', 'J']
    path = [35, 8, 22, 38]
    result = ia.not_affecting_random_gates(path)
    assert result == ['C']
    path = [1, 3, 5, 7, 4, 21, 35]
    result = ia.not_affecting_random_gates(path)
    assert result == []
    path = [2, 4, 42]
    result = ia.not_affecting_random_gates(path)
    assert result == ['A','B','C','L','K','J']

def test_create_server_response():
    ia = AI("") 
    ia.tile_to_play = ["N", "S"]
    ia.gate_to_play = "L" 
    ia.move_to_play = 42
    expected_response = {"tile": ["N", "S"], "gate": "L", "new_position": 42}
    assert ia.create_server_response() == expected_response

def test_positions_in_achievable_positions():
    ia = AI("")
    achievable_positions = [(2, 1), (5, 3), (8, 9)]
    position = 2
    assert ia.positions_in_achievable_positions(position, achievable_positions) == True

def test_get_path():
    ia =AI("")
    achievable_positions = [(21, 21), (22, 21), (29, 22), (23, 22), (24, 23), (30, 29)]
    ia.achievable_positions = achievable_positions
    ia.position = 21
    assert ia.get_path() == [30, 29, 22, 21]

def test_possible_path():
    ia = AI("")
    ia.board = test_board
    assert ia.possible_path(9) == [8, 2]
    assert ia.possible_path(0) == [1]
    assert ia.possible_path(7) == [14]

def test_play():
    ia = AI("")
    play = ia.play(test_state)
    assert 'tile' in play
    assert 'gate' in play
    assert 'new_position' in play
    assert type(play["tile"]) == dict
    assert type(play["gate"]) == str
    assert type(play["new_position"]) == int
