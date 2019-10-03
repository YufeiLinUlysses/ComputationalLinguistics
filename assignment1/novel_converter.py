#!/usr/bin/env python3
"""
    Justin's demo code
    02/20/19
"""

import regex

file_name = "Pride_and_Prejudice_Original.txt"
out_file_name = "Pride_and_Prejudice_Fixed.txt"

with open(file_name, 'r') as open_book:
    with open(out_file_name, 'w') as open_out_book:
        text = open_book.read()
        text = regex.sub(r'\b(wo)?man\b', r'person', text)  #man or woman
        text = regex.sub(r'\bMrs?\.(\s)', r'Mx.\1', text)
        text = regex.sub(r'\b(son|daughter)\b', r'child', text)
        text = regex.sub(r'\b(son|daughter)s\b', r'children', text)
        text = regex.sub(r'\b(s)?he(\s)is\b', r'they\2are', text)
        text = regex.sub(r'\b(his|her)\b', r'their', text)
        text = regex.sub(r'_', r'', text)
        text = regex.sub(r'\b(s)?he(\s\w+)s', r'they\2', text)
        r'[Ss]?[Hh]e' #She He he SHe Shed hear here their the #Won't match SHE
        r'\bhe [A-Za-z]+s'
        text = regex.sub(r'[\p{InHiragana}\p{InKatakana}\p{Han}]+', r'Hello??', text)
        open_out_book.write(text)
        r'[A-Z]'
        r'[0-9\-]'
        r'+' #Matches 1 or more
        r'*' #Matches 0 or more