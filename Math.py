import os

def somma():
	number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", " "]
	n=0
	while n!=\n:
		n= input("Inserire l'addendo: ")
		for i in range(len(n)-1):
			if n[i] in number:
				if i== len(n)-1:
					n=int(n)
					s+=n
					print("La somma parziale corrispone a: ", s)
			else:
				print("Ciò che hai inserito non può essere sommato")

	print("La somma totale corrisponde a:", s)
somma()