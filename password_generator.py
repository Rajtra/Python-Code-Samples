# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []


#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)
print(word_list)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
	password = ""
	for w in random.sample(word_list,3):
		password += w
	return password
print(password)	

generate_password()


#Approach2

# def generate_password():
# 	return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


# def generate_password():
#     return str().join(random.sample(word_list,3))