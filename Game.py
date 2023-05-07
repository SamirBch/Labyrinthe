from IA import ServerAI
import threading

player1 = ServerAI(("localhost", 3000), 8888, "localhost", "samir", "20053", False)
player2 = ServerAI(("localhost", 3000), 8889, "localhost", "ammar", "0000", True)
thread = threading.Thread(target=player2.run_server_AI, daemon=True)
thread.start()
player1.run_server_AI()
