'''
Dada una cadena, contar la cantidad de vocales que hay en una cadena.
Entrada:
string = "fdertsusybjkofiDJHFI"

Salida:
5/20
'''

string = "fdertsusybjkofiDJHFI"

# Array of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Counting the number of vowel in a string
counter = 0
for item in string:
    print(type(item), item)
    if item.lower() in vowels:
        counter+=1

print("--", counter,"/", len(string))
