class program:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def Add(self):
		return self.a + self.b

pr = program(2, 3)
addValue = pr.Add()
print(addValue)
