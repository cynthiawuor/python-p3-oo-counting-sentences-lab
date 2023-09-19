#!/usr/bin/env python3

import re


class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Input must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string using punctuation as separators
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)
    pass
# Create a MyString instance
string = MyString("This is a string! It has three sentences. Right?")

# Test the methods
print(string.is_sentence())  
print(string.is_question())  
print(string.is_exclamation())  
print(string.count_sentences())  
