from IA import ServerAI
import threading

player1 = ServerAI(("localhost", 3000), 8888, "localhost", "Goku", "20053,22037", False)
#player2 = ServerAI(("localhost", 3000), 8889, "localhost", "reback", "22037", True)
#thread = threading.Thread(target=player2.run_server_AI, daemon=True)
#thread.start()
player1.run_server_AI()
