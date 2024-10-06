import emp,pickle

with open('dt.txt','rb') as f:
	while True:
		try:
			o=pickle.load(f)
			o.show()
		except:
			print('All records printed')
			break;
