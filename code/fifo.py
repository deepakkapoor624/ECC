from myhdl import *

fifo_counter = Signal(modbv(0,min=0,max=8))

def fifo(dout, din, we, re, empty, full, clk, fifo_depth=8):

    fifo_buffer = [Signal(intbv(0)[addr_width:0])
                     for i in range(data_width)]


    @always(clk.posedge)
    def access():
        if we:
            fifo_buffer[fifo_counter].next =  din
            fifo_counter.next = fifo_counter + 1

        if re:
            dout.next = fifo_buffer[fifo_counter]
            fifo_counter.next = fifo_counter - 1;


        empty.next = (fifo_counter == 0)
        full.next = (fifo_counter == fifo_depth)

    return access



