import unittest
from translator import frenchText, englishText

class TestFrenchText(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchText('Hello'), 'Bonjour') # test when Hello is given as input the output is Bonjour.
        self.assertNotEqual(frenchText('how are you?'), 'comment as-tu?')  # test when how are you? is given as input the output is comment es-tu?.
        
class TestEnglishText(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishText('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertNotEqual(englishText('comment es-tu'), 'my name is') # test when comment es-tu is given as input the output is how are you.

        unittest.main()