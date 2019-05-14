import math


class Matrix:
	SIZE = 2
	
	def __init__(self, element_list):
		self.m = list(element_list)
	
	@staticmethod
	def rotation(axis, angle):
		x = axis.normalize()
		fSin = math.sin(-angle)
		fCos = math.cos(-angle)
		fOneMinusCos = 1.0 - fCos
		
		return Matrix([
			x.x * x.x * fOneMinusCos + fCos,
			x.x * x.y * fOneMinusCos - x.z * fSin,
			x.x * x.z * fOneMinusCos + x.y * fSin,
			0.0,
			x.y * x.x * fOneMinusCos + x.z * fSin,
			x.y * x.y * fOneMinusCos + fCos,
			x.y * x.z * fOneMinusCos - x.x * fSin,
			0.0,
			x.z * x.x * fOneMinusCos - x.y * fSin,
			x.z * x.y * fOneMinusCos + x.x * fSin,
			x.z * x.z * fOneMinusCos + fCos,
			0.0,
			0.0, 0.0, 0.0, 1.0])
	
	@staticmethod
	def zero():
		return Matrix([0] * (Matrix.SIZE*Matrix.SIZE))
	
	@staticmethod
	def identity():
		res = Matrix.zero()
		for i in range(Matrix.SIZE):
			res[i,i] = 1
		return res
	
	def __getitem__(self, key):
		y, x = key
		return self.m[y * Matrix.SIZE + x]
	
	def __setitem__(self, key, value):
		self.m[key[0] * Matrix.SIZE + key[1]] = value
	
	def __matmul__(self, other):
		res = Matrix([0] * (Matrix.SIZE*Matrix.SIZE))
		for y in range(Matrix.SIZE):
			for x in range(Matrix.SIZE):
				res[y, x] = sum(self[y, i] * other[i, x] for i in range(Matrix.SIZE))
		return res
	
	def __str__(self):
		return "\n".join("\t".join(str(self[y,x]) for x in range(Matrix.SIZE)) for y in range(Matrix.SIZE))

if __name__ == "__main__":
	a = Matrix([0,1,1,1])
	print(pow(a,2))