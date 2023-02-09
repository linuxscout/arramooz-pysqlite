#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_nountuple.py
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
from arramooz.nountuple  import NounTuple

class NounTupleTestCase(unittest.TestCase):
    """Tests for `Arramooz`."""
    def setUp(self):
        self.mydict = arz.ArabicDictionary('nouns')
    def test_lookup(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs') 
        wordlist = [u"استقلّ", u'استقل', u"كذب"]
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),1, "Word not found in dictionary")

    def test_features(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs')
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),1, "Word not found in dictionary")
        # test features of one word
        lemma_dict = dict(lemma_list[0])
        ntuple = NounTuple(lemma_dict)
        lemma_dict = dict(lemma_dict)
        # assert features
        self.assertEqual(ntuple.get_features_dict(), dict(lemma_dict))
        self.assertEqual(ntuple.get_feature("stamped"), lemma_dict["stamped"])
        # for key in lemma_dict:
        #     if isinstance(lemma_dict[key],(str)):
        #         print("self.assertEqual(ntuple.get_%s(),'%s')"%(key, lemma_dict[key]))
        #     else:
        #         print("self.assertEqual(ntuple.get_%s(),%d)"%(key, lemma_dict[key]))
        # #
        self.assertEqual(ntuple.get_vocalized(),'كَذِبٌ')
        self.assertEqual(ntuple.get_unvocalized(),'كذب')
        self.assertEqual(ntuple.get_normalized(),'كذب')
        self.assertEqual(ntuple.get_stamped(),'كذب')
        self.assertEqual(ntuple.get_wordtype(),'مصدر')

        self.assertEqual(ntuple.get_root(),'كذب')
        self.assertEqual(ntuple.get_wazn(),'')
        self.assertEqual(ntuple.get_category(),'مصدر')
        self.assertEqual(ntuple.get_definition(),'"كَذِبٌ-كَذِبٌ [ك ذ ب] (مص. كَذَبَ). ""أَقْوَالُهُ كَذِبٌ فِي كَذِبٍ"" : مُخَالِفَةٌ لِلْحَقِيقَةِ وَالأَمْرِ الوَاقِعِ. ""حَبْلُ الكَذِبِ قَصِيرٌ""."')
        self.assertEqual(ntuple.get_note(),'')

        self.assertEqual(ntuple.get_lemma(),'كَذَبَ')
        self.assertEqual(ntuple.get_gender(),'مذكر')
        self.assertEqual(ntuple.get_feminin(),'')
        self.assertEqual(ntuple.get_masculin(),'')
        self.assertEqual(ntuple.get_number(),'مفرد')
        self.assertEqual(ntuple.get_single(),'')
        self.assertEqual(ntuple.get_broken_plural(),'')

        self.assertEqual(ntuple.is_defined(), False)
        self.assertEqual(ntuple.is_mankous(), False)
        self.assertEqual(ntuple.is_mamnou3_sarf(), False)
        self.assertEqual(ntuple.is_relative(), True)

        self.assertEqual(ntuple.accept_feminin(), False)
        self.assertEqual(ntuple.accept_dual(), False)
        self.assertEqual(ntuple.accept_masculine_plural(), False)
        self.assertEqual(ntuple.accept_feminine_plural(), False)
        self.assertEqual(ntuple.accept_w_suffix(), False)
        self.assertEqual(ntuple.accept_hm_suffix(), True)
        self.assertEqual(ntuple.accept_kal_prefix(), True)
        self.assertEqual(ntuple.accept_ha_suffix(), True)
        self.assertEqual(ntuple.accept_k_prefix(), True)
        self.assertEqual(ntuple.accept_annex(), False)

        #print(ntuple)
        # TEST   []
        self.assertCountEqual(ntuple["stamped"], "كذب")
        self.assertCountEqual(ntuple.get("stamped", ""), "كذب")

    def test_calculated_features(self):
        """Test lookup"""
        mydict = arz.ArabicDictionary('verbs')
        word = "كذب"
        lemma_list = self.mydict.lookup(word)
        self.assertEqual(len(lemma_list),1, "Word not found in dictionary")
        # test features of one word
        lemma_dict = dict(lemma_list[0])
        ntuple = NounTuple(lemma_dict)
        lemma_dict = dict(lemma_dict)
        # assert features
        self.assertEqual(ntuple.get_gender(),'مذكر')
        self.assertEqual(ntuple.is_feminine(), False)
        self.assertEqual(ntuple.is_masculine(), True)

        self.assertEqual(ntuple.get_number(),'مفرد')
        self.assertEqual(ntuple.is_singular(), True)
        self.assertEqual(ntuple.is_plural(), False)

        self.assertEqual(ntuple.is_mamnou3_sarf(), False)
        self.assertEqual(ntuple.accept_tanwin(), True)
        tags = ['منسوب', 'مفرد', 'مصدر', 'اسم']
        self.assertCountEqual(ntuple.get_tags(), tags )

        #print(ntuple)
        # TEST   []
        self.assertCountEqual(ntuple["stamped"], "كذب")
        self.assertCountEqual(ntuple.get("stamped", ""), "كذب")
if __name__  ==  '__main__':
    unittest.main()
