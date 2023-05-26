#!/usr/bin/python3

from src.emu import *
from src.bots.gopigo.gopigo import *

if __name__ == "__main__":
    program_file = input("Python file to emulate with GoPiGo emulator: ")

    pg = Playground(800, 800, "Playground")

    bot = GoPiGoBot(pg)
    bot.pen_offset = 105.5 # In mm

    emulate(pg, bot, program_file)
