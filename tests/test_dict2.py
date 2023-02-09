#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_dict.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
sys.path.append("../")
import arramooz.arabicdictionary as arz
import arrand.arrandom
import random
import pyarabic.araby as araby
def lookup():
    """Test lookup"""
    mydict = arz.ArabicDictionary('verbs') 
    word = arrand.arrandom.word()
    mydict.lookup(word)
def get_wordlist():
    texts = arrand.arrandom.sample("text", 100)
    words = []
    for tx in texts:
        words.extend(araby.tokenize(tx))
    return words
def lookup_nb(nb):
    """Test lookup"""
    mydict = arz.ArabicDictionary('verbs') 
    mydict2 = arz.ArabicDictionary('nouns') 
    words  = get_wordlist()
    for i in range(nb):
        word = random.choice(words)
        mydict.lookup(word)
        mydict2.lookup(word)
if __name__  ==  '__main__':
    
    lookup_nb(200000)
    #~ print(get_wordlist())
    #~ print(random.choice(get_wordlist()))
