from IA import ServerAI
import threading

player1 = ServerAI(("172.17.10.59", 3000), 8881, "", "FcLurk1_4ever <3", "20053,22037", False)
#player2 = ServerAI(("localhost", 3000), 8889, "localhost", "reback", "22037", True)
#thread = threading.Thread(target=player2.run_server_AI, daemon=True)
#thread.start()
player1.run_server_AI()
