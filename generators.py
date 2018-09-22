def number():
	n=1
	yield n
	
	n+=1
	yield n
	
	n+=1
	yield n

'''
	python3 -i generators.py
	
	a = number()
	next(a)

	a = number()
	next(a)
	
	a = number()
	next(a)
'''
#python3 generators.py
