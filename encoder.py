import sys
from sys import argv
from struct import *





input_file, n = argv[1:]                
maximum_table_size = pow(2,int(n))      
file = open(input_file)                 
data = file.read()                      


dictionary_size = 256                   
dictionary = {chr(i): i for i in range(dictionary_size)}    
string = ""             
compressed_data = []    



for symbol in data:                     
    string_plus_symbol = string + symbol 
    if string_plus_symbol in dictionary: 
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        print(dictionary[string])
        if(len(dictionary) <= maximum_table_size):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])
    print(dictionary[string])


out = input_file.split(".")[0]
output_file = open(out + ".lzw", "wb")
for data in compressed_data:
    output_file.write(pack('>H',int(data)))
    
output_file.close()
file.close()