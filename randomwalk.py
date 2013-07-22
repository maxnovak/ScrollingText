import os 
import random
import time

def random_walk(top = "/"):
    """recursively walks through folders and displays files, psuedo randomly jumps out of files and back up the path"""

    files = os.listdir(top)
    for f in files:
        path = os.path.join(top,f)
        if os.path.isdir(path):
            print path
            try:
                random_walk(path)
            except OSError:
                pass
        else:
            print path
        if len(top) >10:
            break
        if random.random() < 0.2:
            break
        time.sleep(0.05)

if __name__ == "__main__":
    random_walk()

