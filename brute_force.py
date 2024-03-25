
dictionary_filename = "dictionary.txt"
password_dictionary = open(dictionary_filename,"r")

sha1_website = "http://www.sha1-online.com/"

password_dictionary_values = password_dictionary.read().split("\n")

hash_filename = "passwords.txt"
hash_file_lines = open(hash_filename,"r").read().split("\n")

password_hash_values = [hash_format[3:] for hash_format in hash_file_lines]