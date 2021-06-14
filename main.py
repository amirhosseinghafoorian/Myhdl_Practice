#!/usr/bin/env python3
from myhdl import *


@block
def HelloWorld():

    @always(delay(10))
    def say_hello():
        print(f'{now()} hello')

    return say_hello


inst = HelloWorld()
inst.run_sim(30)

