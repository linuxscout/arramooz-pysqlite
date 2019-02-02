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


from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import arramooz.arabicdictionary as arz
import arramooz.stopwordsdictionaryclass as arstop
def mainly():
    """
    main test
    """
    #ToDo: use the full dictionary of arramooz
    mydict = arz.ArabicDictionary('verbs')
#    mydict_stop= arstop.StopWordsDictionary("classedstopwords")

    wordlist = [u"استقلّ", u'استقل', u"كذب"]
    tmp_list = []
    for word in wordlist:
        foundlist = mydict.lookup(word)
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            vocalized = word_tuple['vocalized']
            tmp_list.append(dict(word_tuple))
    print(repr(tmp_list).replace('},','},\n').decode("unicode-escape")) 

    mydict = arstop.StopWordsDictionary('classedstopwords')
    wordlist = [u"بعضهما", u'في', u"منً", u"أن", u'عندما']
    tmp_list =[]
    for word in wordlist:
        print("-------")
        print("word looked up ", mydict.is_stopword(word))
        idlist = mydict.lookup(word)
        for word_tuple in idlist:
            #~ vocalized = word_tuple["vocalized"]
            tmp_list.append(dict(word_tuple))
    print(repr(tmp_list).replace('},','},\n').decode("unicode-escape"))           
if __name__  ==  '__main__':
    mainly()
