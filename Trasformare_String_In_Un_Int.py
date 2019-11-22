a= str(input("Inserisci una variabile: "))
ok=len(a)
Number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", " "]
while ok == len(a):
	ok=0
	for i in range(len(a)):
		if a[i] in Number:
			ok += 1
		else:
			ok -=1
	if ok < len(a):
		print("La variabile inserita non è numerica:")
		a = input("Reinserire una variabile: ")
		ok = len(a)
	elif ok == len(a):
		c = float(a)
		print("La variabile inserita corrisponde a ", c)
		ok = len(a)-1