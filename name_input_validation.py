name = None

while True:
	name = input('\nWhat is your name? ...')
	Name = name.title()
	chars = set('~!@#$%^&*()_+`1234567890=[]{}\|;:?/><,."')
	if not any((c in chars) for c in name):
        		print('\n    Nice to meet you', ''+ Name +'!', '\n')
        		break
	else: print('\n    E R R O R : Wrong characters in " N A M E " !')
