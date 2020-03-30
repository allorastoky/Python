import os
n=0
somma=0
n=str(n)
while True:
	n= (input("Inserire addendo: "))
	if n=="":
		break
	else:
		n=int(n)
		somma +=n
		os.system("CLEAR")
			print(somma)
print(somma)