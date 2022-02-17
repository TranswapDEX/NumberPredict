
from random import randint

'''
a1 = [4, 6, 8, 10]
c1 = 12


a2 = [6, 8, 10, 12]
c2 = 14

'''

a1 = 7
c1 = 11

a2 = 11
c2 = 13

a3 = 13
c3 = 17

a4 = 23
c4 = 29

a5 = 31
c5 = 37

wA = "w"
wB = "w"
wC = "w"
wD = "w"
wE = "w"
biasA = "b"

def model(i1, gt1, i2, gt2, i3, gt3, i4, gt4, i5, gt5):
	e1 = 0
	e2 = 0
	e3 = 0
	e4 = 0
	e5 = 0
	while ((gt1 - e1) != (gt2 - e2)) or ((gt1 - e1) != (gt3 - e3)) or ((gt1 - e1) != (gt4 - e4)) or ((gt1 - e1) != (gt5 - e5)):
		w1 = randint(1, 10)
		w2 = randint(1, 10)
		w3 = randint(1, 10)
		#w4 = randint(1, 10)
		e1 = (i1 ** w1) - ((i1 * w2) + w3)
		e2 = (i2 ** w1) - ((i2 * w2) + w3)
		e3 = (i3 ** w1) - ((i3 * w2) + w3)
		e4 = (i4 ** w1) - ((i4 * w2) + w3)
		e5 = (i5 ** w1) - ((i5 * w2) + w3)
		b = (e1 - gt1) * -1
	wA = w1
	wB = w2
	wC = w3
	wD = w4
	wE = w5
	biasA = b
	print("formula: ((i * (1/w1)) ** w2) + ((i * (1/w3)) ** w4)")
	print("")
	print("")
	print("w1:")
	print(w1)
	print("")
	print("w2:")
	print(w2)
	print("w3:")
	print(w3)
	print("")
	print("")
	print("bias:", b)
	print("")
	print("")
	print("expected: 11, 13, 17, 29, 37")
	print(e1 + b)
	print(e2 + b)
	print(e3 + b)
	print(e4 + b)
	print(e5 + b)
	
model(a1, c1, a2, c2, a3, c3, a4, c4, a5, c5)



'''

a9 = [23, 29, 31, 37]
#a3 = [23, 30, 37, 44]
#c3 = 11

def trained (input):
	d = ["w", "x", "y", "z"]
	for i in input:
		z = i * weightsA[input.index(i)]
		d[input.index(i)] = z
	print((sum(d) + (bias0[0] * (input[3] - input[2]))) + biasA[0])

print("")
trained(a9)
print("")

'''
