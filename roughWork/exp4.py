from gates import *
I = Istream('I',fname = 'inp', stream = 1)
O = Ostream('O',stream = 1)
I.data_out.connect([O.data_in])
N = Not('N')
N.B.connect([I.clk_in, O.clk_in])
