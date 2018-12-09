from myhdl import *

@block
def mul_2_2(A, B, C):

    @always(A,B)
    def lut_2_2():
        if concat(A,B) == 0:
            C.next = 0b0
        elif concat(A,B) == 1:
            C.next = 0b0
        elif concat(A,B) == 2:
            C.next = 0b0
        elif concat(A,B) == 3:
            C.next = 0b0
        elif concat(A,B) == 4:
            C.next = 0b0
        elif concat(A,B) == 5:
            C.next = 0b0001
        elif concat(A,B) == 6:
            C.next = 0b0010
        elif concat(A,B) == 7:
            C.next = 0b0011
        elif concat(A,B) == 8:
            C.next = 0b0
        elif concat(A,B) == 9:
            C.next = 0b0010
        elif concat(A,B) == 10:
            C.next = 0b0100
        elif concat(A,B) == 11:
            C.next = 0b0110
        elif concat(A,B) == 12:
            C.next = 0b0
        elif concat(A,B) == 13:
            C.next = 0b0011
        elif concat(A,B) == 14:
            C.next = 0b0110
        elif concat(A,B) == 15:
            C.next = 0b0101
    return lut_2_2


def main():
    A = Signal(intbv(0)[1:0])
    B = Signal(intbv(0)[1:0])
    C = Signal(intbv(0)[3:0])
    var_to_verilog = mul_2_2(A, B, C)
    var_to_verilog.convert(hdl='verilog', initial_values=True)


if __name__ == "__main__":
    main()