from IA import Queue

def test_queue_creation():
    q = Queue()
    assert q.isEmpty() == True

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    assert q.isEmpty() == False

def test_dequeue():
    q = Queue()
    q.enqueue(2)
    q.dequeue()
    assert q.isEmpty() == True    

def test_clear_queue():
    q = Queue()
    q.enqueue(2)
    q.enqueue(5)
    q.clear_queue()
    assert q.isEmpty() == True

def test_dequeue_sequence():
    q = Queue()
    for i in range(0,5):
        q.enqueue(i)
    for j in range(0,5):
        assert q.dequeue() == j 
