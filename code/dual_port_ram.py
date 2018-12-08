from myhdl import *


'''
addr_width: size of the RAM'''
@block
def dual_port_ram(clk, wr, addr, din,
                  dout, addr_width, data_width):


    ram_dual_port = [Signal(intbv(0)[addr_width:0])
                     for i in range(data_width)]

    @always(clk.posedge)
    def write_logic():

        if wr == 1:
            ram_dual_port[addr].next = din

#always_comb: The combinational Block
    @always_comb
    def read_logic():

        dout.next = ram_dual_port[addr]

    return write_logic, read_logic


def main():

    addr_width =  8
    data_width = 128

    clk = Signal(bool(0))
    wr = Signal(bool(0))

    addr = Signal(intbv(0)[addr_width:0])

    din = Signal(intbv(0)[data_width:0])

    dout = Signal(intbv(0)[data_width:0])

    var_to_verilog = dual_port_ram(clk, wr, addr, din, dout, addr_width, data_width)
    print var_to_verilog
    var_to_verilog.convert(hdl="Verilog", initial_values=True)


if __name__ == '__main__':
    main()



