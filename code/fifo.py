from myhdl import *


@block
def fifo(dout, din, we, re, empty, full, clk):

    data_width = 128
    fifo_depth = 8

    fifo_counter = Signal(intbv(0, min=0, max=fifo_depth))
    fifo_rear = Signal(modbv(fifo_depth - 1, min=0, max=fifo_depth))
    fifo_front = Signal(modbv(0, min=0, max=fifo_depth))

    fifo_buffer = [Signal(intbv(0)[fifo_depth:0])
                     for i in range(data_width)]


    @always(clk.posedge)
    def access():
        if we ==1:

            fifo_rear.next = fifo_rear + 1
            fifo_buffer[fifo_rear.next].next =  din
            fifo_counter.next = fifo_counter + 1

        if re ==1:
            fifo_front.next = fifo_front + 1
            fifo_counter.next = fifo_counter - 1

    @always_comb
    def fifo_status():
        empty.next = (fifo_counter.next == 0)
        dout.next = fifo_buffer[fifo_front]
        full.next = (fifo_counter.next == fifo_depth)

    return access, fifo_status


def main():

    data_width = 128

    clk = Signal(bool(0))
    we = Signal(bool(0))
    re = Signal(bool(0))
    empty = Signal(bool(0))
    full = Signal(bool(0))

    din = Signal(intbv(0)[data_width:0])
    dout = Signal(intbv(0)[data_width:0])

    var_to_verilog = fifo(dout, din, we, re, empty, full, clk)
    var_to_verilog.convert(hdl="Verilog", initial_values=True)


if __name__ == "__main__":
    main()