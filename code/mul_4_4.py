from myhdl import *
from code.mul_lut_2_2_module import mul_2_2

@block
def mul_4_4(A, B, C):

    d0 = Signal(intbv(0)[4:0])
    d1 =Signal(intbv(0)[4:0])
    d2 = Signal(intbv(0)[4:0])
    d7 = Signal(intbv(0)[4:0])

    mul0 = Signal(intbv(0)[2:0])
    mul1 = Signal(intbv(0)[2:0])
    mul2 = Signal(intbv(0)[2:0])
    mul3 = Signal(intbv(0)[2:0])
    mul4 = Signal(intbv(0)[2:0])
    mul5 = Signal(intbv(0)[2:0])


    @always_comb
    def assign_variable():
        mul0.next = A[2:0]
        mul1.next = B[2:0]
        mul2.next = (A[2:0]^A[4:2])
        mul3.next = (B[2:0]^B[4:2])
        mul4.next = A[4:2]
        mul5.next = B[4:2]


    instance_0 = mul_2_2(mul0, mul1, d0)
    instance_1 = mul_2_2(mul2, mul3, d1)
    instance_2 = mul_2_2(mul4, mul5, d2)

    @always_comb
    def status():
        d7.next = d0 ^ d1 ^ d2

    @always_comb
    def mul_status():
        C.next = ConcatSignal(d2[4:2], (d2[2:0] ^ d7[4:2]), (d0[4:2] ^ d7[2:0]), d0[2:0])

    return assign_variable,mul_status, status, instance_0, instance_1, instance_2


def main():

    A = Signal(intbv(0)[4:0])
    B = Signal(intbv(0)[4:0])
    C = Signal(intbv(0)[8:0])

    var_to_verilog = mul_4_4(A, B, C)
    var_to_verilog.convert(hdl="verilog",initial_values=True)


if __name__ == "__main__":
    main()

