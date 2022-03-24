'''
Program to make a piglan using recursion
'''

def pigl(word):
	
	for char in word:
		print(word)
		if char in ['a','e','i','o','u']:
			word = word + 'ay'
			break
		else:
			word = word[1:]+char
	return word

def userinput():
	word = input("What is the input word? : ")
	ans = pigl(word)
	print("The piglan form of the word is: {}".format(ans))
	cont = input("Do you want to continue Y/N :")
	if cont == 'Y':
		userinput()
	else:
		print("EXIT")

# string  = 'Scheme'
# ans = pigl(string)
#print("The piglan form of the word is: {}".format(ans))
print("/n Welcome to Piglan conversion")
userinput()