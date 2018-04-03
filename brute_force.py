'''
program to crack password from a given file using a given dictionary

exctution info: python brute_force.py pass.txt dictionary.txt hash_type

''' 
import sys
import hashlib 
# define the hash function get from command line
hash_to_call = getattr(hashlib,sys.argv[3].lower())

# function that call the built-in hash function 
# hexdigest is needed 'cause hash to call do not return a string 
def hash_function(word):
	return hashlib.hash_to_call(word).hexdigest()
									
if __name__ == 'main'
# argument passed trough command line
password_file_name = sys.argv[1]
dictionary_file_name = sys.argv[2]


# open the dictionary and the password file
# for each password try every word of the dictionary
# hashing one word at time and then try to match with each passsword   
with open(password_file_name, 'r') as pwd_file, open(dictionary_file_name,'r') as dict_file:
	
	for line in dict_file:
		for word in line.split():
			hashed_word = hash_function(word)
			for line_pwd in pwd_file:
				for pwd in pwd_file:
					if pwd == hashed_word:
						print word
					
					# try digits from 1 to 20 after and before the word
					else:
						for i in range(21):
							hashed_word_i = hash_function(word + str(i))
							hashed_i_word =  hash_function(str(i) + word)
							if hashed_word_i == pwd or hashed_i_word == pwd:
								print word,i
								break
								
							for j in range(10):
								hashed_word_ij = hash_function(word+str(i)+str(j))
								hashed_ij_word = hash_function(str(i)+str(j)+word)
								if hashed_word_ij == pwd or hashed_ij_word == pwd:
									print word,i,j
									break

