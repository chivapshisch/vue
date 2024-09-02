class Dress: 

	def __init__(self, name):
		self.name = name 

pt = Dress('ff')
res = Dress('fara')
print(res.__dict__)