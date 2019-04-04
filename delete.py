import os

l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','del','nothing','space']

for prefix in l:
	for i in range(101,3001):
		delete = 'dataset/' + prefix +'/' + prefix + str(i)+'.jpg'
		if os.path.exists(delete):
  			os.remove(delete)
		else:
			pass	
	
