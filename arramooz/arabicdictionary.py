﻿#!/usr/bin/python
# -*- coding = utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Arabic Dictionary from Arramooz Al Waseet
# Purpose:     Morphological porpus Dictionary.
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     16-12-2013
# Copyright:   (c) Taha Zerrouki 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
"""
Arabic Dictionary Class from Arramooz Al Waseet.
Used in multiporpus morpholigical treatment
"""
import re
import os, os.path
#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import sys
FILE_DB = u"data/arabicdictionary.sqlite"
import pyarabic.araby as araby

from . import nountuple
class ArabicDictionary:
    """
    Arabic dictionary Class
    Used to allow abstract acces to lexicon of arabic language, 
    can get indexed and hashed entries from the  basic lexicon
    add also, support to extract attributtes from entries
    
    Example:
        >>> import arramooz.arabicdictionary 
        >>> mydict = arramooz.arabicdictionary.ArabicDictionary('verbs')
        >>> wordlist = [u"استقلّ", u'استقل', u"كذب"]
        >>> tmp_list = []
        >>> for word in wordlist:
        >>>     foundlist = mydict.lookup(word)
        >>>     for word_tuple in foundlist:
        >>>         word_tuple = dict(word_tuple)
        >>>         vocalized = word_tuple['vocalized']
        >>>         tmp_list.append(dict(word_tuple))
        >>> print(tmp_list)
        [{'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'اِسْتَقَلَّ', 'stamped': u'ستقل', 'future_moode': 0, 'triliteral': 0, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'استقل', 'future_type': u'َ', 'double_trans': 0, 'normalized': u'استقل', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'قلل', 'id': 7495},
        {'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'كَذَبَ', 'stamped': u'كذب', 'future_moode': 0, 'triliteral': 1, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'كذب', 'future_type': u'كسرة', 'double_trans': 0, 'normalized': u'كذب', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'كذب', 'id': 1072},
        {'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'كَذَّبَ', 'stamped': u'كذب', 'future_moode': 0, 'triliteral': 0, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'كذب', 'future_type': u'َ', 'double_trans': 0, 'normalized': u'كذب', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'كذب', 'id': 2869}]

    """

    def __init__(self, table_name):
        """
        initialisation of dictionary from a data dictionary, create indexes 
        to speed up the access.

        """
        # load data from the brut dictionary into a new dictionary 
        # with numeric ids
        self.dictionary = {}
        # self.attribIndex = attribIndex
        # self.keyAttribute =  keyAttribute
        self.attrib_num_index = {}
        # create the attribute num index
        # attribIndex:         attrib_num_index
        # vocalized: 0        0: vocalized
        #unvocalized: 1        1: unvocalized
        #
        # for k in self.attribIndex.keys():
            # v = self.attribIndex[k]
            # self.attrib_num_index[v] = k
        self.table_name = table_name

        # get the database path
        if hasattr(sys, 'frozen'): # only when running in py2exe this exists
            base = sys.prefix
        else: # otherwise this is a regular python script
            base = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base, FILE_DB)

        if os.path.exists(file_path):
            try:
                self.db_connect = sqlite.connect(file_path, check_same_thread=False)
                self.db_connect.row_factory = sqlite.Row 
                self.cursor = self.db_connect.cursor()
            except  IOError:
                print("Fatal Error Can't find the database file", file_path)
        else:
            print(u" ".join(["Inexistant File", file_path, " current dir ", 
            os.curdir]).encode('utf8'))
        #create index  by word stampfor dictionary to accelerate word search.
        # the word stamp is the arabic word without any affixation  letters,
        # for example
        # the word قالب give قلب, by removing meem and beh, the word قوالب give قلب.
        # the stamp is used as a first level of indexing, especially
        # for verbs
        # the stamp pattern is used to create the word stamp
        self.stamp_pat = re.compile(u"[%s%s%s%s%s%s%s%s%s%s]"% (araby.ALEF, 
        araby.YEH, araby.HAMZA, araby.ALEF_HAMZA_ABOVE, araby.WAW_HAMZA,
         araby.YEH_HAMZA, araby.WAW, araby.ALEF_MAKSURA, araby.SHADDA, araby.ALEF_MADDA), 
         re.UNICODE)

    def __del__(self):
        """
        Delete instance and close database connection
        
        """
        if self.db_connect:
            self.db_connect.close()


    def get_entry_by_id(self, idf):
        """ Get dictionary entry by id from the dictionary
        @param idf :word identifier
        @type idf: integer
        @return: all attributes
        @rtype: dict
        """
        # if the id exists and the attribute existe return the value, 
        # else return False
        # The keys in the dictinary are numeric, for comression reason, 
        # then we use text keys in output, according to 
        # the self.attrib_num_index
        # eg.
        # entry  = {0:"kataba", 1:"ktb"}
        # output entry  = {'vocalized':'kataba', 'unvocalized':'ktb'}
        sql = u"select * FROM %s WHERE id='%s'" % (self.table_name, idf)
        try:
            self.cursor.execute(sql)
            if self.cursor:
                return self.cursor.fetchall()            
                # for row in self.cursor:
                    # entry_dict = {}
                    # for numKey in self.attrib_num_index:
                        # textKey = self.attrib_num_index[numKey]
                        # entry_dict[textKey] = row[numKey]
                    # return entry_dict
        except  sqlite.OperationalError:
            return False
        return False

    def get_attrib_by_id(self, idf, attribute):
        """ Get attribute value by id from the dictionary
        @param idf :word identifier
        @type idf: integer
        @param attribute :the attribute name
        @type attribute: unicode
        @return: The attribute value
        @rtype: mix.
        """
        # if the given attribute existes on the attrib index
        #in order to redure the dictionary size we use numecric 
        # index to show the attributes
        # like
        #NOUN_DICTIONATY_INDEX = {u'vocalized':0, u'unvocalized':1, 
        # u'wordtype':2, u'root':3, u'original':4, u'mankous':5, u'feminable':6,
        # u'number':7, u'dualable':8, u'masculin_plural':9,
        # u'feminin_plural':10, u'broken_plural':11, u'mamnou3_sarf':12, 
        #u'relative':13, u'w_suffix':14, u'hm_suffix':15, u'kal_prefix':16, 
        #u'ha_suffix':17, u'k_suffix':18, u'annex':19, u'definition':20,
        # u'note':21, }
        #NOUN_DICTIONARY = {
        #u'مفرد/تكسير':{0:u'مفرد/تكسير', 1:u'مفرد/تكسير'
        #, 2:u'اسم فاعل',
        # 3:u'', 4:u'', 5:u'المنقوص', 6:u'التأنيث', 7:u'جمع تكسير', 
        #8:u'التثنية', 
        #9:u'"ج. مذ. س."', 10:u'"ج. مؤ. س."', 11:u'الجمع', 12:u'',
        # 13:u'نسب', 14:u'ـو', 1
        #5:u'هم', 16:u'كال', 17:u'ها', 18:u'ك', 19:u'"إض. لف."', 20:u'', 
        #21:u':لا جذر:لا مفرد:لا تشكيل:لا شرح', }, 
        #u'شَاذّ':{0:u'شَاذّ', 1:u'شاذ', 2:u'اسم فاعل', 3:u'', 4:u'', 
        #5:u'', 
        #~6:u'Ta', 7:u'جمع تكسير', 8:u'DnT', 9:u'Pm', 10:u'Pf', 11:u'":شواذ"', 1
        #2:u'', 13:u'', 14:u'', 15:u'', 16:u'', 17:u'', 18:u'', 19:u'', 20:u'', 
        #21:u':لا جذر:لا مفرد:لا شرح', }, 

        # if self.attribIndex.has_key(attribute):
            # attnum = self.attribIndex[attribute]
        # else:
            # return False
        # if the id exists and the attribute existe return the value, 
        #else return False
        sql = u"select * FROM %s WHERE id='%s'" % (self.table_name, idf)
        try:
            self.cursor.execute(sql)
            #~entry_dict = {}
            if self.cursor:
                for row in self.cursor:
                    return  row[attribute]                        
        except  sqlite.OperationalError:
            return False
        return False

    def lookup(self, normalized):
        """
        look up for all word forms in the dictionary
        @param normalized: the normalized word.
        @type normalized: unicode.
        @return: list of dictionary entries .
        @rtype: list.

        Example:
            >>> import arramooz.arabicdictionary 
            >>> import arramooz.arabicdictionary
            >>> mydict = arramooz.arabicdictionary.ArabicDictionary('verbs')
            >>> wordlist = [u"استقلّ", u'استقل', u"كذب"]
            >>> tmp_list = []
            >>> for word in wordlist:
            ...     foundlist = mydict.lookup(word)
            ...     for word_tuple in foundlist:
            ...         print(dict(word_tuple))
            ...
            {'id': 4743, 'vocalized': 'اِسْتَقَلَّ', 'unvocalized': 'استقل', 'root': 'قلل', 'normalized': 'استقل', 'stamped': 'ستقل', 'future_type': 'فتحة', 'triliteral': 0, 'transitive': 1, 'double_trans': 0, 'think_trans': 1, 'unthink_trans': 0, 'reflexive_trans': 0, 'past': 0, 'future': 0, 'imperative': 0, 'passive': 0, 'future_moode': 0, 'confirmed': 0}
            {'id': 118, 'vocalized': 'كَذَّبَ', 'unvocalized': 'كذب', 'root': 'كذب', 'normalized': 'كذب', 'stamped': 'كذب', 'future_type': 'فتحة', 'triliteral': 0, 'transitive': 1, 'double_trans': 0, 'think_trans': 1, 'unthink_trans': 0, 'reflexive_trans': 0, 'past': 0, 'future': 0, 'imperative': 0, 'passive': 0, 'future_moode': 0, 'confirmed': 0}
            {'id': 10205, 'vocalized': 'كَذَبَ', 'unvocalized': 'كذب', 'root': 'كذب', 'normalized': 'كذب', 'stamped': 'كذب', 'future_type': 'كسرة', 'triliteral': 1, 'transitive': 1, 'double_trans': 0, 'think_trans': 1, 'unthink_trans': 0, 'reflexive_trans': 0, 'past': 0, 'future': 0, 'imperative': 0, 'passive': 0, 'future_moode': 0, 'confirmed': 0}
            >>>
        """
        idlist = []
        normword = araby.normalize_hamza(normalized)
        #print "###", normword.encode('utf8')

        sql = u"select * FROM %s WHERE normalized='%s'" % (self.table_name,
         normword)
        try:
            self.cursor.execute(sql)
            if self.cursor:
                # return self.curser.fetchall()
                for row in self.cursor:
                    idlist.append(row)
            return idlist
        except  sqlite.OperationalError:
            return []
    def exists_as_stamp(self, word):
        """
        look up for word if exists by using the stamp index, 
        the input word is stamped by removing infixes letters like alef, teh
        the stamped word is looked up in the stamp index
        @param word: word to look for.
        @type word: unicode.
        @return: True if exists.
        @rtype: Boolean.
        """
        stamp = self.word_stamp(word)
        sql = u"select id FROM %s WHERE stamped='%s'" % (self.table_name,
           stamp)
        try:
            self.cursor.execute(sql)
            if self.cursor:
                return True
        except  sqlite.OperationalError:
            return False
        return False
    def lookup_by_stamp(self, word):
        """
        look up for word if exists by using the stamp index, 
        the input word is stamped by removing infixes letters like alef, teh
        the stamped word is looked up in the stamp index
        @param word: to look for.
        @type word: unicode.
        @return: list of dictionary entries IDs.
        @rtype: list.
        """
        idlist = []
        stamp = self.word_stamp(word)
        sql = u"select * FROM %s WHERE stamped='%s'" % (self.table_name, 
        stamp)
        try:
            self.cursor.execute(sql)
            if self.cursor:
                # return self.curser.fetchall()
                for row in self.cursor:
                    idlist.append(row)
                    # idlist.append(nountuple.NounTuple(row))
            return idlist
        except  sqlite.OperationalError:
            return []



    def word_stamp(self, word):
        """
        generate a stamp for a word, 
        remove all letters which can change form in the word :
            - ALEF, 
            - HAMZA, 
            - YEH, 
            - WAW, 
            - ALEF_MAKSURA
            - SHADDA
        @return: stamped word
        """
        # strip the last letter if is doubled
        if word[-1:] ==  word[-2:-1]:
            word = word[:-1]
        return self.stamp_pat.sub('', word)

#Class test
def mainly():
    """
    main test
    """
    #ToDo: use the full dictionary of arramooz
    mydict = ArabicDictionary('verbs')
    wordlist = [u"استقلّ", u'استقل', u"كذب"]
    tmp_list = []
    for word in wordlist:
        foundlist = mydict.lookup(word)
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            vocalized = word_tuple['vocalized']
            tmp_list.append(dict(word_tuple))
    print(repr(tmp_list).replace('},','},\n').decode("unicode-escape"))            
if __name__  ==  '__main__':
    mainly()
