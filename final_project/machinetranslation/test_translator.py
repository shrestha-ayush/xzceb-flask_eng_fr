import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Test translation of 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Au revoir')

        # Test translation of 'null' input
        self.assertEqual(english_to_french(None), None)

    def test_french_to_english(self):
        # Test translation of 'Bonjour'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(english_to_french('Au revoir'),'Hello')

        # Test translation of 'null' input
        self.assertEqual(french_to_english(None), None)

unittest.main()
