#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_verbtuple.py
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

import unittest
import sys
sys.path.append('../')
import arramooz.arabicdictionary as arz
from arramooz.verbtuple  import VerbTuple

class verbTupleTestCase(unittest.TestCase):
    """Tests for `Arramooz`."""
    def setUp(self):
        self.mydict = arz.ArabicDictionary('verbs')
    def test_lookup(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs') 
        wordlist = [u"استقلّ", u'استقل', u"كذب"]
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),2, "Word not found in dictionary")

    def test_features(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs')
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),2, "Word not found in dictionary")
        # test features of one word
        lemma_dict = dict(lemma_list[1])
        vtuple = VerbTuple(lemma_dict)
        lemma_dict = dict(lemma_dict)
        # assert features
        self.assertEqual(vtuple.get_features_dict(), dict(lemma_dict))
        self.assertEqual(vtuple.get_feature("stamped"), lemma_dict["stamped"])
        # for key in lemma_dict:
        #     if isinstance(lemma_dict[key],(str)):
        #         print("self.assertEqual(vtuple.get_%s(),'%s')"%(key, lemma_dict[key]))
        #     else:
        #         print("self.assertEqual(vtuple.get_%s(),%d)"%(key, lemma_dict[key]))
        # #
        self.assertEqual(vtuple.get_vocalized(),'كَذَبَ')
        self.assertEqual(vtuple.get_unvocalized(),'كذب')
        self.assertEqual(vtuple.get_normalized(),'كذب')
        self.assertEqual(vtuple.get_stamped(),'كذب')

        self.assertEqual(vtuple.get_root(),'كذب')
        self.assertEqual(vtuple.get_wazn(),'')


        self.assertEqual(vtuple.get_lemma(),'كَذَبَ')


        self.assertEqual(vtuple.get_future_type(),'كسرة')
        self.assertEqual(vtuple.is_triliteral(), True)
        self.assertEqual(vtuple.is_transitive(), True)

        self.assertEqual(vtuple.is_double_transitive(), False)
        self.assertEqual(vtuple.is_think_transitive(), True)
        self.assertEqual(vtuple.is_unthink_transitive(), False)
        self.assertEqual(vtuple.is_reflexive_transitive(), False)

        self.assertEqual(vtuple.accept_past(), True)
        self.assertEqual(vtuple.accept_future(), True)
        self.assertEqual(vtuple.accept_imperative(), True)
        self.assertEqual(vtuple.accept_passive(), True)
        self.assertEqual(vtuple.accept_future_moode(), True)
        self.assertEqual(vtuple.accept_confirmed(), True)

        self.assertEqual(vtuple.accept_tense("past"), True)




        #print(vtuple)
        # TEST   []
        self.assertCountEqual(vtuple["stamped"], "كذب")
        self.assertCountEqual(vtuple.get("stamped", ""), "كذب")

        #
        self.assertTrue(isinstance(dict(vtuple), dict))


    def test_calculated_features(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs')
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),2, "Word not found in dictionary")
        # test features of one word
        lemma_dict = dict(lemma_list[1])
        vtuple = VerbTuple(lemma_dict)
        # lemma_dict = dict(lemma_dict)
        # assert features

        # print(vtuple.get_tags())
        tags = ['كَذَبَ', 'فعل ثلاثي', 'متعدي', 'سالم', 'صحيح']
        self.assertCountEqual(vtuple.get_tags(), tags )

        #print(vtuple)
        # TEST   []
        self.assertCountEqual(vtuple["stamped"], "كذب")
        self.assertCountEqual(vtuple.get("stamped", ""), "كذب")
if __name__  ==  '__main__':
    unittest.main()
