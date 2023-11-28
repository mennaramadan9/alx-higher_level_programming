#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        sep = ", " if (tens, ones) != (8, 9) else "\n"
        print("{:d}{:d}".format(tens, ones), end=sep)
