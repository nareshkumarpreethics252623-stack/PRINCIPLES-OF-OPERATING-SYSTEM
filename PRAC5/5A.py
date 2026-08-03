# Name : Preethi Naresh
# Roll No : S103

import threading

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{threading.current_thread().name}: Factorial of {n} = {result}")

# List of numbers
numbers = [5, 7, 10, 4]

threads = []

# Create and start threads
for num in numbers:
    thread = threading.Thread(target=factorial, args=(num,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("\nAll threads have completed execution.")
