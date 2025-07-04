# multithreading = Used to perform multiple tasks concurrently(multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading. Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"you finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_meal():
    time.sleep(4)
    print("You get the meal")

# walk_dog() # it will not running concurrently
# take_out_trash()
# get_meal()

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # this does run concurrently
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_meal)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")