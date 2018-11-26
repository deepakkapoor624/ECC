from myhdl import *

fifo_depth = 8
fifo_counter = Signal(intbv(0, min=0,max=fifo_depth))
fifo_rear = Signal(modbv(fifo_depth-1,min=0,max=fifo_depth))
fifo_front = Signal(modbv(0,min=0,max=fifo_depth))
addr_width = 8
data_width = 128


def fifo(dout, din, we, re, empty, full, clk):

    fifo_buffer = [Signal(intbv(0)[addr_width:0])
                     for i in range(data_width)]


    @always(clk.posedge)
    def access():
        print fifo_rear, fifo_front, fifo_counter
        if we:
            fifo_rear.next = fifo_rear + 1
            fifo_buffer[fifo_rear.next].next =  din
            fifo_counter.next = fifo_counter + 1

        if re:
            dout.next = fifo_buffer[fifo_front]
            fifo_front.next = fifo_front + 1
            fifo_counter.next = fifo_counter - 1

    @always_comb
    def fifo_status():
        empty.next = (fifo_counter.next == 0)
        full.next = (fifo_counter.next == fifo_depth)

    return access, fifo_status


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
    #report()
    yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)
    # yield write(0x55)


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
    #yield read()
    #report()
    raise StopSimulation

sim = Simulation(clkGen(), test(), dut)


def main():
    #try
    sim.run()
    #except:
    #    traceback.print_exec()

if __name__ == "__main__":
    main()