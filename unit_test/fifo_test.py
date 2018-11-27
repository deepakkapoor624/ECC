from myhdl import *
from code.fifo import fifo


dout, din, re, we, empty, full, clk = args = [Signal(0) for i in range(7)]

dut = fifo(dout, din, we, re, empty, full, clk)

def clkGen():
    while 1:
        yield delay(10)
        clk.next = not clk

def read():
    yield clk.negedge
    re.next = 1
    yield clk.posedge

    yield delay(1)
    re.next = 0


def write(data):
    yield clk.negedge
    din.next = data
    we.next = 1
    yield clk.posedge
    yield delay(1)
    we.next = 0

def report():
    print "dout:%s empty: %s full: %s" %(hex(dout), empty, full)

def test():

    yield write(0x55)

    report()
    yield write(0x77)
    report()
    yield write(0x11)
    report()
    yield read()
    report()
    yield read()
    report()
    yield read()
    report()
    raise StopSimulation

sim = Simulation(clkGen(), test(), dut)


def main():
    #try
    sim.run()
    #except:
    #    traceback.print_exec()

if __name__ == "__main__":
    main()