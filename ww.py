from random import randint

'''
a1 = [4, 6, 8, 10]
c1 = 12


a2 = [6, 8, 10, 12]
c2 = 14

'''

a1 = [31, 37, 41, 43]
c1 = 47


a2 = [13, 17, 19, 23]
c2 = 29

weightsA = []
biasA = []

def model(input1, gt1, input2, gt2):
	weights = ["w", "x", "y", "z"]
	d1 = ["w", "x", "y", "z"]
	d2 = ["w", "x", "y", "z"]
	e1 = 0
	e2 = 0
	while (gt1 - e1) != (gt2 - e2):
		for i in input1:
			w = randint(1, 10)
			weights[input1.index(i)] = 1/w
			z1 = i * (1/w)
			z2 = input2[input1.index(i)] * (1/w)
			d1[input1.index(i)] = z1
			d2[input1.index(i)] = z2
		e1 = sum(d1)
		e2 = sum(d2)
		b = (e1 - gt1) * -1
	for i in weights:
		weightsA.append(i)
	biasA.append(b)
	print(weights)
	print(b)
	print("")
	print("")
	print(d1)
	print(d2)
	print("")
	print("")
	print(e1 + b)
	print(e2 + b)
	
model(a1, c1, a2, c2)




a3 = [53, 59, 61, 67]
#c3 = 71

def trained (input):
	d = ["w", "x", "y", "z"]
	for i in input:
		z = i * weightsA[input.index(i)]
		d[input.index(i)] = z
	print(sum(d)+biasA[0])

print("")
trained(a3)
print("")





'''

def model(input, gt):
	weights = ["w", "x", "y", "z"]
	d = ["w", "x", "y", "z"]
	e = 0
	while e != gt:
		for i in input:
			w = randint(1, 10)
			weights[input.index(i)] = 1/w
			z = i * (1/w)
			d[input.index(i)] = z
		e = sum(d)
	print(weights)
	print(d)
	print(e)

model(a2, b2)

'''

