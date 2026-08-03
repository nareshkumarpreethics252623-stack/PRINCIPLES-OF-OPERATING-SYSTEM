# Name : Preethi Naresh
# Roll No : S103

import threading

# even numbers
def print_even():
    print("Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

#odd numbers
def print_odd():
    print("Odd Numbers:")
    for i in range(1, 21, 2):
        print(i, end=" ")
    print()

#reverse a string
def reverse_string():
    text = "Multithreading"
    print("Original String:", text)
    print("Reversed String:", text[::-1])

# Create threads
t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
t3 = threading.Thread(target=reverse_string)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")
