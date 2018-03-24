'''
program to crack password from a given file using a given dictionary

exctution info: python brute_force.py pass.txt dictionary.txt

''' 
import sys
import hashlib 
# define the hash function get from command line
hash_to_call = getattr(hashlib,sys.argv[3].lower())

def hash_function(word):
	return hash_to_call(word).hexdigest()
				

password_file_name = sys.argv[1]
dictionary_file_name = sys.argv[2]
crypt_function = sys.argv[3]


with open(password_file_name, 'r') as pwd_file, open(dictionary_file_name,'r') as dict_file:
	for line in dict_file:
			for word in line.split():
				hashed_word = hash_function(word)
				
	 
