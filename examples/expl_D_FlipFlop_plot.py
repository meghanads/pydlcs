# CIRCUIT:
#
#	I_STREAM--->D Filp Flop---->O_STREAM
#
#	1. plotting working


from sequential import *

sim = SIMU('sim1',start = 0,plots = 1, debug = 1 , step =0, pannotate = 1)

I = Istream('IN', fname = 'inp', stream =1)
O = Ostream('OUT', stream = 1)

D1 = DFlipFlop('D1')
N = Not('N')

sim.clk_out.connect([I.clk_in, N.A, O.clk_in])
I.data_out.connect([D1.D])
N.B.connect([D1.C])

D1.Q.connect([O.data_in])

sim.addplot([I.data,O.data])
sim.addpname(["input1","output"])

#sim.addplot([I.data])
#sim.addpname(["input"])


sim.start = 1
sim.simulate()

