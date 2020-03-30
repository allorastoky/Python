def Trasformare_String_In_Un_Int(n):
	ok=len(n)
	Number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", " "]
	while ok == len(n):
		ok=0
		for i in range(len(n)):
			if a[i] in Number:
				ok += 1
			else:
				ok -=1
		if ok < len(n):
			print("La variabile inserita non è numerica:")
			a = input("Reinserire una variabile: ")
			ok = len(n)
		elif ok == len(n):
			c = float(n)
			print("La variabile inserita corrisponde a ", c)
			ok = len(n)-1