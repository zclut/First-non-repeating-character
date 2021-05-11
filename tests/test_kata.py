import unittest
from src.kata import first_non_repeating_letter, RandomString

class TestFirstNonRepeatingLetter(unittest.TestCase):

    def test_letters_lowercase(self):
        '''Encuentra la primera letra no repetida en un string de letras minúsculas'''
        random = RandomString()
        string = random.letters_lower()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_string_empty(self):
        '''Encuentra la primera letra no repetida en un string vacio'''
        string = ''
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_letters_uppercase(self):
        '''Encuentra la primera letra no repetida en un string de letras mayúsculas.'''
        random = RandomString()
        string = random.letters_upper()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_digits(self):
        '''Encuentra el primero digito no repetido en un string de digitos.'''
        random = RandomString()
        string = random.digits()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)


    def test_signs(self):
        '''Encuentra el primer signo no repetido un string de signos.'''     
        random = RandomString()
        string = random.signs()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_letters_uppercase_and_lowercase(self):
        '''
        Encuentra la primera letra no repetida en un string de letras 
        mayúsculas y minúsculas.
        '''
        random = RandomString()
        string = random.letters()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_letters_and_digits(self):
        '''
        Encuentra la primera letra o digito no repetido en un string de letras
        mayúsculas, minúsculas y digitos.
        '''
        random = RandomString()
        string = random.letters() + random.digits()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)
    
    def test_letters_and_signs(self):
        '''
        Encuentra la primera letra o signo no repetido en un string de letras
        mayúsculas, minúsculas y signos.
        '''
        random = RandomString()
        string = random.letters() + random.signs()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

    def test_signs_and_digits(self):
        '''
        Encuentra el primer digito o signo no repetido en un string de digitos
        y signos.
        '''
        random = RandomString()
        string = random.digits() + random.signs()
        expectedResult = first_non_repeating_letter(string)
        self.assertEqual(first_non_repeating_letter(string), expectedResult)

if __name__ == '__main__':
    unittest.main()
