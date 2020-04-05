#! /usr/bin/python3

import time
import curses
import string
import random
from urllib.request import urlopen
import os.path


def main(screen):
    screen.addstr(1, 5, "Hello")
    screen.refresh()
    time.sleep(3)


curses.wrapper(main)
