from random import randint
for i in range(10):
	n= str(i+1)
	file= n+".txt"
	f= open(file, "w")
	a= randint(1, 200)
	n1= str(a)+"\n"
	f.write(n1)
	for j in range(a):
		c= str(randint(1, 60000))
		c+= " "
		if j==a-1:
			f.write(c)
		else:
			f.write(c,)