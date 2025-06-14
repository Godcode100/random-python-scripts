#!/usr/bin/python
import random, shutil, sys, time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ["0", "1"]

DENSITY = 0.02

# sIZE PF THE TERMINAL WINDOW
WIDTH = shutil.get_terminal_size()[0]

# we cant print to the last column on windows without it adding a
# new line automatically,so we reduce the width by one

WIDTH -= 1

print("Digital stream by Joe")
print("PRESS CTRL + C TO QUIT")

time.sleep(2)

try:
    # For each column when the counter is 0, no stream is shown
    # Otherwise it acts as a counter for how many times 1 0r 0
    # should be displayed in that column
    columns = [0] * WIDTH
    while True:
        # set up the counter for each column
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # rESTART A STREAM ON THIS COLUMN
                    columns[i] == random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            # dISPLAY AN EMPTY SPACE OR 1/0 CHARACTER
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end="")
                columns[i] -= 1
            else:
                print(" ", end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()
