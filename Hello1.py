from myhdl import *


@block
def HelloWorld():

    @always(delay(10))
    def say_hello():
        print(f'{now()} hello')

    return say_hello


@block
def HelloWorld2():
    clk = Signal(0)

    @always(delay(10))
    def drive_clk():
        clk.next = not clk

    @always(clk.posedge)
    def say_hello():
        print("%s Hello World!" % now())

    return drive_clk, say_hello


@block
def Hello(clk, to="World!"):

    @always(clk.posedge)
    def say_hello():
        print("%s Hello %s" % (now(), to))

    return say_hello
