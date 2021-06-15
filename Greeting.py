from myhdl import block, Signal

from Hello2 import ClkDriver
from Hello1 import Hello


@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClkDriver(clk1)
    clkdriver_2 = ClkDriver(clk=clk2, period=19)
    hello_1 = Hello(clk=clk1)
    hello_2 = Hello(to="MyHDL", clk=clk2)

    return clkdriver_1, hello_1, clkdriver_2, hello_2
