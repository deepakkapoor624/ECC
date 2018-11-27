from myhdl import *


data_width = 128
fifo_depth = 8

fifo_counter = Signal(intbv(0, min=0,max=fifo_depth))
fifo_rear = Signal(modbv(fifo_depth-1,min=0,max=fifo_depth))
fifo_front = Signal(modbv(0,min=0,max=fifo_depth))


def fifo(dout, din, we, re, empty, full, clk):

    fifo_buffer = [Signal(intbv(0)[fifo_depth:0])
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
