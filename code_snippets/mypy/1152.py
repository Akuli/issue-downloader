@contextmanager
def simulated_queue_client(client):
    real_SimpleQueueClient = queue_processors.SimpleQueueClient
    queue_processors.SimpleQueueClient = client
    yield
    queue_processors.SimpleQueueClient = real_SimpleQueueClient
