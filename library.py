def TrasformStringInt(str(a),):
	while ok == len(a):
		number= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", " "]
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
	return c
