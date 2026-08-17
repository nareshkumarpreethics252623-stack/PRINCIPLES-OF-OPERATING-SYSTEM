import threading
import time

BUFFER_SIZE = 5
ITEMS = 10

# Circular buffer
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

# Mutex for synchronized access to the buffer
mutex = threading.Lock()

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  
full = threading.Semaphore(0)


def producer():
    global in_index

    for item in range(1, ITEMS + 1):
        # Wait for an empty slot
        empty.acquire()

        # Critical section
        with mutex:
            buffer[in_index] = item
            print(f"Producer produced {item} at position {in_index}")

            # Circular queue
            in_index = (in_index + 1) % BUFFER_SIZE

        # Increase number of full slots
        full.release()

        time.sleep(0.5)


def consumer():
    global out_index

    for _ in range(ITEMS):
        # Wait until an item is available
        full.acquire()

        # Critical section
        with mutex:
            item = buffer[out_index]
            print(f"Consumer consumed {item} from position {out_index}")

            # Circular queue
            out_index = (out_index + 1) % BUFFER_SIZE

        # Increase number of empty slots
        empty.release()

        time.sleep(1)


# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("\nProducer-Consumer execution completed.")
