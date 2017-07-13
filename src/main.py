#!/usr/bin/env python

from lib.matrix import Matrix
import time

def run(instructions):
    matrix = Matrix(set(["61", "17"]))
    for instruction in instructions:
        print("Intruction: %s" % instruction.strip())
        matrix.execute_instruction(instruction)
    matrix.done.wait()
    time.sleep(.1) # because of independent IO
    print("===\nThe result is %s" % matrix.result)


if __name__ == "__main__":
    instructions = open("input.txt").readlines()
    run(instructions)
