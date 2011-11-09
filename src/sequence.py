
# ============================================
# Sequential Circuits
# ============================================


from pydlcs import *

# ================
# D - FlipFlop
# ================

class DFlipFlop (LG):

	def __init__(self, name):
		LG.__init__(self,name)
		self.D = Connector(self,'D')
		self.Q = Connector(self,'Q')
		self.C = Connector(self,'C', activates = 1)
		self.Q.value = 0
		self.prev = 0

	def evaluate (self):
		if (not self.C.value) and self.prev:	# clock drop
			self.Q.set(self.D.value)
		self.prev = self.C.value


		
# ================
# T - FlipFlop
# ================

class TFlipFlop (LG):

	def __init__(self, name):
		LG.__init__(self,name)
		self.T = Connector(self,'T')
		self.Q = Connector(self,'Q')
		self.C = Connector(self,'C', activates = 1)
		self.Q.value = 0
		self.prev = 0
		
	def evaluate (self):
		if (not self.C.value) and self.prev and self.T.value:	# clock drop and T=1
			self.Q.set(not self.Q.value)
		self.prev = self.C.value


