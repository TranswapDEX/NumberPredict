from random import randint

'''
a1 = [4, 6, 8, 10]
c1 = 12


a2 = [6, 8, 10, 12]
c2 = 14

'''

a1 = [2, 3, 5, 7]
c1 = 11

a2 = [13, 17, 19, 23]
c2 = 29

a4 = [31, 37, 41, 43]
c4 = 47

weightsA = []
biasA = []
bias0 = []

def model(input1, gt1, input2, gt2, input3, gt3):
	weights = ["w", "x", "y", "z"]
	d1 = ["w", "x", "y", "z"]
	d2 = ["w", "x", "y", "z"]
	d3 = ["w", "x", "y", "z"]
	e1 = 0
	e2 = 0
	e3 = 0
	while ((gt1 - e1) != (gt2 - e2)) or ((gt1 - e1) != (gt3 - e3)):
		for i in input1:
			w = randint(1, 10)
			weights[input1.index(i)] = 1/w
			z1 = i * (1/w)
			z2 = input2[input1.index(i)] * (1/w)
			z3 = input3[input1.index(i)] * (1/w)
			d1[input1.index(i)] = z1
			d2[input1.index(i)] = z2
			d3[input1.index(i)] = z3
		w2 = randint(1, 10)
		e1 = sum(d1) + (w2 * (input1[3] - input1[2]))
		e2 = sum(d2) + (w2 * (input2[3] - input2[2]))
		e3 = sum(d3) + (w2 * (input3[3] - input3[2]))
		b = (e1 - gt1) * -1
	for i in weights:
		weightsA.append(i)
	biasA.append(b)
	bias0.append(w2)
	print("weights:")
	print(weights)
	print("")
	print("bias:", b)
	print("")
	print("weights applied 1:")
	print(d1)
	print("")
	print("weights applied 2:")
	print(d2)
	print("")
	print("weights applied 3:")
	print(d3)
	print("")
	print(e1 + b)
	print(e2 + b)
	print(e3 + b)
	
model(a1, c1, a2, c2, a4, c4)


a3 = [23, 29, 31, 37]
#a3 = [23, 30, 37, 44]
#c3 = 11

def trained (input):
	d = ["w", "x", "y", "z"]
	for i in input:
		z = i * weightsA[input.index(i)]
		d[input.index(i)] = z
	print((sum(d) + (bias0[0] * (input[3] - input[2]))) + biasA[0])

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
