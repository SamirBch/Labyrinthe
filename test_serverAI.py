from IA import ServerAI
import json
def test_creation_serverAI():
    server = ServerAI(('localhost', 3000),8888, "localhost", "samir", "20053", True)
    assert isinstance(server,ServerAI) 


def test_get_subscribe_request():
    server = ServerAI(('localhost', 3000),8888, "localhost", "samir", "20053", True)
    request = server.get_subscribe_request()
    request = json.loads(request)
    assert 'request' in request
    assert 'port' in request
    assert 'name' in request
    assert 'matricules' in request
    assert request['request'] == "subscribe"
    assert request['port'] == server.server_AI_port
    assert request['name'] == server.player_name
    assert request['matricules'] == [server.player_matricule]


def test_convert_to_dict():
    server = ServerAI(('localhost', 3000),8888, "localhost", "samir", "20053", True)
    request = server.convert_to_dict("")
    assert 'request' in request
    assert request['request'] == 'Empty'

def test_get_ping_response():
    server = ServerAI(('localhost', 3000),8888, "localhost", "samir", "20053", True)
    request = json.loads(server.get_ping_response().decode())
    assert "response" in request
    assert request["response"] == "pong"

def test_get_move_response():
    server = ServerAI(('localhost', 3000),8888, "localhost", "samir", "20053", True)
    response = json.loads(server.get_move_response(20).decode())
    assert "response" in response
    assert "move" in response
    assert "message" in response
    assert response["response"] == "move"
    assert response["move"] == 20
    