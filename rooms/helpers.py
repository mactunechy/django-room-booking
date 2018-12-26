from random import randint



#A function that creates a random 14 digit alpha numericc number
def random_apha_numeric():
	nums = [0,1,2,3,4,5,6,7,8,9]
	letters_combined = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
	letters = letters_combined.split(' ')
	
	
	alpha_number = ''
	for i in range(7):
		digit = randint(0,10)
		alpha_number +=str(digit) 
		letter_picker = randint(0,25)
		letter = letters[letter_picker]
		alpha_number+=letter
		
		
	return alpha_number	

