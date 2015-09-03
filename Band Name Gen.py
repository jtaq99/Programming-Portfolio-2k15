# Band name generator
import random


titles = ["gigantic", "sour", "steamy", "gross", "stupid",
"ironic", "greasy", "tangy", "smelly", "small",
"inventive", "spherical", "spiritual", "green",
"blue", "pot bellied", "pickled", "prickly"]

adjs = ["tiny", "fat", "shiny", "ecclectic", "fluffy", "brights",
"corrupt", "aggressive", "alarming", "amazing", "amazing", "magical",
"courageous", "fierce", "colorless", "red", "thoughtless",
"smart", "delirious", "fabulous", "fergalicious", "dangerous"]

plural_nouns = ["apples", "oranges", "kiwis", "clementines",
"wildabeasts", "mammouths", "rabbits", "sloths", "crashes",
"spices", "eggs", "herbs", "pony tails", "bears", "snitches",
"unicorns", "kermits", "signs", "indians", "cowboys", "checks"]
 
def title():
 
 	return random.choice(titles)
 	 
def adj():
 	return random.choice(adjs)
 	 	 
 	 	 
def plural_noun():
	return random.choice(plural_nouns)
	
def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()
		
main()

