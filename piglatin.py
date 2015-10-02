#Pig Latin Translator


def pigify(word):
	vowels = "aeiouy"
	slice_pos = 0
	for i in range(len(word)):
		if word[i] in vowels:
			slice_pos = i 
			break
			
	return word[slice_pos: ] + word[:slice_pos] + "aye"
	

def main():
	while True:
		word = raw_input("Enter a word: ")
		if word == "exit":
			break
		
	#print pigify(word)
	
main()	
