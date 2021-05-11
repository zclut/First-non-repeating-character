import string
import random

def first_non_repeating_letter(string):
    # Colocamos el string en minúscula
    str_lower = string.lower()
    
    for letter in string:
        # Colocamos la letra en minúscula
        letter_lower = letter.lower()
        # Por cada letra del string contaremos sus ocurrencias
        ocurrencies = str_lower.count(letter_lower)
        # Verificamos si la cantidad de ocurrencias es 1
        if ocurrencies == 1:
            return letter
    return ""

class RandomString():

    def letters_lower(self):
        '''Retorna un string aleatorio con letras en minúscula'''
        letters = string.ascii_lowercase
        return ( ''.join(random.choice(letters) for i in range(30)) )

    def letters_upper(self):
        '''Retorna un string aleatorio con letras en mayúscula'''
        letters = string.ascii_uppercase
        return ( ''.join(random.choice(letters) for i in range(30)) )

    def letters(self):
        '''Retorna un string aleatorio con letras con mayúsculas y minúsculas'''
        letters = letters = string.ascii_letters
        return ( ''.join(random.choice(letters) for i in range(30)) )

    def digits(self):
        '''Retorna un string aleatorio con digitos'''
        letters = string.digits
        return ( ''.join(random.choice(letters) for i in range(30)) )

    def signs(self):
        '''Retorna un string aleatorio con signos'''
        letters = string.punctuation
        return ( ''.join(random.choice(letters) for i in range(30)) )
