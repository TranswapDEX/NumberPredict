from random import randint

'''
a1 = [4, 6, 8, 10]
c1 = 12


a2 = [6, 8, 10, 12]
c2 = 14

'''

a1 = [2, 3, 5, 7, 11]
c1 = 13

a2 = [13, 17, 19, 23, 29]
c2 = 31

a4 = [31, 37, 41, 43, 47]
c4 = 53

weightsA = []
weights0 = []
biasA = []


def model(input1, gt1, input2, gt2, input3, gt3):
	weights = ["w", "x", "y", "z"]
	weights2 = ["w", "x", "y", "z"]
	d1 = ["w", "x", "y", "z"]
	d2 = ["w", "x", "y", "z"]
	d3 = ["w", "x", "y", "z"]
	e1 = 0
	e2 = 0
	e3 = 0
	while ((gt1 - e1) != (gt2 - e2)) or ((gt1 - e1) != (gt3 - e3)):
		for i in input1[0:4]:
			w = randint(1, 10)
			w2 = randint(1, 10)
			weights2[input1.index(i)] = w2
			weights[input1.index(i)] = 1/w
			z1 = (i//w2) * ((input1[input1.index(i)+1] - i) + (1/w))
			z2 = (input2[input1.index(i)]//w2) + ((input2[input1.index(i)+1] - input2[input1.index(i)]) * (1/w))
			z3 = (input3[input1.index(i)]//w2) + ((input3[input1.index(i)+1] - input3[input1.index(i)]) * (1/w))
			d1[input1.index(i)] = z1
			d2[input1.index(i)] = z2
			d3[input1.index(i)] = z3
		e1 = sum(d1)
		e2 = sum(d2)
		e3 = sum(d3)
		b = (e1 - gt1) * -1
	for i in weights:
		weightsA.append(i)
	for i in weights2:
		weights0.append(i)
	biasA.append(b)
	#bias0.append(w2)
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



a3 = [53, 59, 61, 67, 71]
#a3 = [23, 30, 37, 44]
#c3 = 11

def trained (input):
	d = ["w", "x", "y", "z"]
	for i in input[0:4]:
		z = (i//weights0[0]) + ((input[input.index(i)+1] - i) * weightsA[input.index(i)])
		d[input.index(i)] = z
	print(sum(d) + biasA[0])

print("")
trained(a3)
print("")





