#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nountuple.py
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
import pyarabic.araby as araby


class NounTuple:
    """
    A object to handle the noun tuple gotten from arramooz dictionary 
    """
    def __init__(self, noun_dict = {}):
        """
        Init noun tuples
        """
        self.noun_dict = dict(noun_dict)
    #---------------------------
    # nouns features
    #---------------------------
        #NOUN_DICTIONATY_INDEX = {
# ~ u'vocalized':0, 
# ~ u'unvocalized':1, 
# ~ u'wordtype':2, 
# ~ u'root':3, 
# ~ u'original':4, 
# ~ u'mankous':5, 
# ~ u'feminable':6,
# ~ u'number':7, 
# ~ u'dualable':8, 
# ~ u'masculin_plural':9,
# ~ u'feminin_plural':10, 
# ~ u'broken_plural':11, 
# ~ u'mamnou3_sarf':12, 
# ~ u'relative':13, 
# ~ u'w_suffix':14, 
# ~ u'hm_suffix':15, 
# ~ u'kal_prefix':16, 
# ~ u'ha_suffix':17, 
# ~ u'k_suffix':18, 
# ~ u'annex':19, 
# ~ u'definition':20,
# ~ u'note':21, 
# ~ }
     
     
    def get_features_dict(self,):
        """
         return the all features for  a noun
        """
        return self.noun_dict


    def get_feature(self,feature):
        """
         return the asked feature form  a noun
        """
        return self.noun_dict.get(feature,'')
        
    def get_vocalized(self,):
        """
         return the vocalized form of a noun
        """
        return self.noun_dict.get('vocalized','')

    def get_unvocalized(self,):
        """
         return the unvocalized form of a noun
        """
        return self.noun_dict.get('unvocalized','')

    def get_normalized(self,):
        """
         return the normalized form of a noun
        """
        return self.noun_dict.get('normalized','')

    def get_stamped(self,):
        """
         return the stamped form of a noun
        """
        return self.noun_dict.get('stamped','')


    def get_wordtype(self,):
        """
         return the wordtype of a noun
        """
        # return type or word_type 
        return self.noun_dict.get('wordtype','')

    def get_category(self,):
        """
         return the category of a noun
        """
        return self.noun_dict.get('category','')
              
    def get_root(self,):
        """
         return the root of a noun
        """
        return self.noun_dict.get('root','')

    def get_wazn(self,):
        """
         return the wazn of a noun
        """
        return self.noun_dict.get('wazn','')
        
            
    def get_gender(self,):
        """
         return the gender of a noun (masculine, feminine, "")
        """
        return self.noun_dict.get('gender','')

    def get_feminin(self,):
        """
         return the feminin form if exists
        """
        return self.noun_dict.get('feminin','')

    def get_masculin(self,):
        """
         return the  masculin form if exists
        """
        return self.noun_dict.get('masculin','')

    def is_feminine(self,):
        """
         return True if the gender is  feminine
        """
        return self.noun_dict.get('gender','') == "مؤنث"

    def is_masculine(self,):
        """
         return True if the gender is  masculine
        """
        return self.noun_dict.get('gender','') == "مذكر"

    def get_number(self,):
        """
         return the number of a noun (signular, plural, dual)
        """
        return self.noun_dict.get('number','')

        
    # intrinsic attributes
    # ~ u'mankous':5, 
    # * u'number':7, 
    # ~ u'masculin_plural':9,
    # ~ u'feminin_plural':10, 
    # ~ u'broken_plural':11, 
    # ~ u'relative':13, 
    # ~ u'definition':20,
       
    def is_plural(self,):
        """
         return True if the lemma word is plural (masculine, feminine, broken[irregular])
        """
        return bool(self.get_number()  in ("جمع", "جمع تكسير"))

    def is_singular(self,):
        """
         return True if the lemma word is singular
        """
        return bool(self.get_number() == "مفرد")

    def get_single(self,):
        """
                  return the single of the word if exists
        """
        return self.noun_dict.get('single','')

    def get_broken_plural(self,):
        """
                  return True if the lemma word is plural (broken[irregular])
        """
        return self.noun_dict.get('broken_plural','')

    def is_defined(self,):
        """
         return True if the word  is defined , 
        """
        return bool(self.noun_dict.get('defined',0))
    #-----------------------------
    # Lemmas accept affixes
    #-----------------------------
    # To accept
    # ~ u'feminable':6,
    # ~ u'dualable':8,
    # ~ u'mamnou3_sarf':12,
    # ~ u'w_suffix':14,
    # ~ u'hm_suffix':15,
    # ~ u'kal_prefix':16,
    # ~ u'ha_suffix':17,
    # ~ u'k_suffix':18,
    # ~ u'annex':19,
    def is_mankous(self,):
        """
         return True if the word  is mankous ,
        """
        return bool(self.noun_dict.get('mankous',0))

    def is_relative(self,):
        """
         return True if the word  is relative ,
        """
        return bool(self.noun_dict.get('relative',0))

    def is_mamnou3_sarf(self,):
        """
         return True if the word  is mamnou3_sarf ,
        """
        return bool(self.noun_dict.get('mamnou3_sarf',0))

    def accept_feminin(self,):
        """
         return True if the word  accept feminin form, 
        """
        return bool(self.noun_dict.get('feminable',0))
        
    def accept_dual(self,):
        """
         return True if the word  accept dual form, 
        """
        return bool(self.noun_dict.get('dualable',0))

    def accept_masculine_plural(self,):
        """
                  return True if the lemma word accept plural (masculine)
        """
        return bool(self.noun_dict.get('masculin_plural',0))

    def accept_feminine_plural(self,):
        """
                  return True if the lemma word accept plural (feminine)
        """
        return bool(self.noun_dict.get('feminin_plural',''))
    def accept_w_suffix(self,):
        """
         return True if the word  accept w_suffix form, 
        """
        return bool(self.noun_dict.get('w_suffix',0))
        
    def accept_hm_suffix(self,):
        """
         return True if the word  accept hm_suffix form, 
        """
        return bool(self.noun_dict.get('hm_suffix',0))
        
    def accept_ha_suffix(self,):
        """
         return True if the word  accept ha_suffix form, 
        """
        return bool(self.noun_dict.get('ha_suffix',0))
        
    def accept_k_prefix(self,):
        """
         return True if the word  accept k_suffix form, 
        """
        return bool(self.noun_dict.get('k_prefix',0))
        
    def accept_suffix(self, suffix):
        """
         return True if the word  accept given suffix, 
        """
        suffix_nm = araby.strip_tashkeel(suffix)
        if suffix_nm == araby.KAF and not self.accept_k_suffix():
            return False
        if suffix_nm == "ها" and not self.accept_ha_suffix():
            return False
        if suffix_nm == "هم" and not self.accept_hm_suffix():
            return False

        if suffix_nm == "و" and not self.accept_w_suffix():
            return False
        return True

        
    def accept_kal_prefix(self,):
        """
         return True if the word  accept kal_suffix form, 
        """
        return bool(self.noun_dict.get('kal_prefix',0))
                
    def accept_prefix(self, prefix):
        """
         return True if the word  accept given prefix, 
        """
        prefix_nm = araby.strip_tashkeel(prefix)
        if prefix_nm == u"كال" and not self.accept_kal_prefix():
            return False
        if prefix_nm == "ك" and not self.accept_k_prefix():
            return False
        return True


    def accept_tanwin(self,):
        """
         return True if the word  accept tanwin, 
        """
        return not self.is_mamnou3_sarf()

    def accept_plural_tanwin_nasb(self,):
        """
         return True if the word  accept plural_tanwin_nasb
        """
        return bool(self.noun_dict.get('plural_tanwin_nasb',0))

    def accept_annex(self,):
        """
         return True if the word  accept annex,
        """
        return bool(self.noun_dict.get('annex',0))

    #TODO:
    def get_tags(self,):
        """
         return True if the word  get tags, 
        """
        tags_list = ["اسم",]
        tags_list.append(self.get_wordtype())
        tags_list.append(self.get_category())
        if self.is_feminine():
            tags_list.append("مؤنث")
        elif self.is_feminine():
            tags_list.append("مذكر")
        if self.is_plural():
            tags_list.append(u"جمع")
        elif self.is_singular():
            tags_list.append(u"مفرد")
        if self.is_mamnou3_sarf():
            tags_list.append(u"ممنوع من الصرف")
        if self.is_mankous():
            tags_list.append(u"منقوص")
        if self.is_relative():
            tags_list.append(u"منسوب")
        # remove duplicated
        tags_list = list(set(tags_list))
        return tags_list


    def get_lemma(self,):
        """
         return   get lemma, 
        """
        return self.noun_dict.get('original','')


    def get_definition(self,):
        """
         return   get word definition,
        """
        return self.noun_dict.get('definition','')


    def get_note(self,):
        """
         return   get word note,
        """
        return self.noun_dict.get('note','')

    def __str__(self):
        """
        return tuple as string
        """
        return self.noun_dict.__str__()


    def __getitem__(self, key):
        """
        return attribute
        """
        return self.noun_dict.get(key,None)

    def __iter__(self):
        """
        :return:
        """
        yield from self.noun_dict.items()
        
    def get(self, key, default):
        """
        return attribute
        """
        return self.noun_dict.get(key,default)
    
def main():
    word = u"لعلهم"
    ntuple = {'id': 86107,
              'vocalized': 'كَذِبٌ',
              'unvocalized': 'كذب',
              'normalized': 'كذب',
              'stamped': 'كذب',
              'wordtype': 'مصدر',
              'root': 'كذب',
              'wazn': '',
              'category': 'مصدر',
              'original': 'كَذَبَ',
              'gender': 'مذكر',
              'feminin': '',
              'masculin': '',
              'number': 'مفرد',
              'single': '',
              'broken_plural': '',
              'defined': 0,
              'mankous': 0,
              'feminable': 0,
              'dualable': 0,
              'masculin_plural': 0,
              'feminin_plural': 0,
              'mamnou3_sarf': 0,
              'relative': 1,
              'w_suffix': 0,
              'hm_suffix': 1,
              'kal_prefix': 1,
              'ha_suffix': 1,
              'k_prefix': 1,
              'annex': 0,
              'definition': '"كَذِبٌ-كَذِبٌ [ك ذ ب] (مص. كَذَبَ). ""أَقْوَالُهُ كَذِبٌ فِي كَذِبٍ"" : مُخَالِفَةٌ لِلْحَقِيقَةِ وَالأَمْرِ الوَاقِعِ. ""حَبْلُ الكَذِبِ قَصِيرٌ""."',
              'note': ''}
    nn = NounTuple(ntuple)
    print(nn)
    return 0
    
if __name__ == '__main__':
    main()
