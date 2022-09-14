# Check Dolar word counter
while True:
	inpt = str(input('Enter word or "exit" to stop\n'))
	ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	if not all(map(str.isalpha, inpt)):
		print('Sorry word contained non-alphabet symbols, please try again')
		continue

	if inpt.lower() == 'exit':
		if str(input('Are you sure want to exit ("yes" or "no")')) == 'yes':
			print('Have a good day!')
			exit()
		else: continue

	count = 0
	for letter in inpt:
		print(letter, ltrs.index(letter.upper())+1)
		count += ltrs.index(letter.upper())+1
	if count == 100:
		print('WOW you got dollar word: %s is %d points'%(inpt, count))
	else:
		print('Sorry it\'s not Dollar Word: %s is %d cents'%(inpt, count))