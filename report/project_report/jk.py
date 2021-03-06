# ================
# JK - FlipFlop
# ================

class JKFlipFlop (LG):

	def __init__(self, name):
		LG.__init__(self,name)
		self.J = Connector(self,'J')
		self.K = Connector(self,'K')
		self.Q = Connector(self,'Q')
		self.C = Connector(self,'C', activates = 1)
		self.Q.value = 0
		self.prev = 0
		
	def evaluate (self):
		if (not self.C.value) and self.prev and self.J.value and (not self.K.value):	
			self.Q.set(1)
		if (not self.C.value) and self.prev and not(self.J.value) and self.K.value:	
			self.Q.set(0)
		if (not self.C.value) and self.prev and self.J.value and self.K.value:	
			self.Q.set(not self.Q.value)
		self.prev = self.C.value
