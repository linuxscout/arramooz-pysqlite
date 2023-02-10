#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  verbtuple.py
#  
#  Copyright 2023 zerrouki <zerrouki@majd4>
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
from typing import Any

import pyarabic.araby as araby


class VerbTuple:
    """
    A object to handle the verb tuple gotten from arramooz dictionary 
    """

    def __init__(self, verb_dict={}):
        """
        Init verb tuples
        """
        self.verb_dict = dict(verb_dict)
        self.tab_type = {0: '', 1: '', 2: '',
                         3: 'فعل ثلاثي',
                         4: 'فعل رباعي',
                         5: 'فعل خماسي',
                         6: 'فعل سداسي',
                         7: 'فعل سباعي',
                         8: 'فعل ثماني',
                         9: 'فعل تساعي'}
    # ---------------------------
    # verbs features
    # ---------------------------
    # 'vocalized',
    # 'unvocalized',
    # 'root',
    # 'normalized',
    # 'stamped',
    # 'future_type',
    # 'triliteral',
    # 'transitive',

    def get_features_dict(self, ):
        """
         return the all features for  a verb
        """
        return self.verb_dict

    def get_feature(self, feature):
        """
         return the asked feature form  a verb
        """
        return self.verb_dict.get(feature, '')

    def get_vocalized(self, ):
        """
         return the vocalized form of a verb
        """
        return self.verb_dict.get('vocalized', '')

    def get_unvocalized(self, ):
        """
         return the unvocalized form of a verb
        """
        return self.verb_dict.get('unvocalized', '')

    def get_normalized(self, ):
        """
         return the normalized form of a verb
        """
        return self.verb_dict.get('normalized', '')

    def get_stamped(self, ):
        """
         return the stamped form of a verb
        """
        return self.verb_dict.get('stamped', '')

    def get_root(self, ):
        """
         return the root of a verb
        """
        return self.verb_dict.get('root', '')

    # Todo
    def get_wazn(self, ):
        """
         return the wazn of a verb
        """
        return ""

    # 'future_type',
    # 'triliteral',
    # 'transitive',
    def get_future_type(self, ):
        """
         return the future mark of a verb
        """
        return self.verb_dict.get('future_type', '')

    def is_transitive(self, ):
        """
         return True if verb is transitive
        """
        return bool(self.verb_dict.get('transitive', 0))

    def is_triliteral(self, ):
        """
         return True if verb is triliteral
        """
        return bool(self.verb_dict.get('triliteral', 0))

    # ---------------------------
    # verbs features
    # ---------------------------
    # 'double_trans',
    # 'think_trans',
    # 'unthink_trans',
    # 'reflexive_trans',
    def is_double_transitive(self, ):
        """
         return True if verb is double transitive
        """
        return bool(self.verb_dict.get('double_trans', 0))

    def is_think_transitive(self, ):
        """
         return True if verb is transitive to brain having being
        """
        return bool(self.verb_dict.get('think_trans', 0))

    def is_unthink_transitive(self, ):
        """
         return True if verb is transitive to brain non having being
        """
        return bool(self.verb_dict.get('unthink_trans', 0))

    def is_reflexive_transitive(self, ):
        """
         return True if verb is reflexive transitive
        """
        return bool(self.verb_dict.get('reflexive_trans', 0))

    # ---------------------------
    # verbs features
    # ---------------------------
    # 'past',
    # 'future',
    # 'imperative',
    # 'passive',
    # 'future_moode',
    # 'confirmed',
    def accept_past(self, ):
        """
         return True if verb accept past tense conjugation
        """
        return bool(self.verb_dict.get('past', 0))

    def accept_future(self, ):
        """
         return True if verb accept future tense conjugation
        """
        return bool(self.verb_dict.get('future', 0))

    def accept_imperative(self, ):
        """
         return True if verb accept future tense conjugation
        """
        return bool(self.verb_dict.get('imperative', 0))

    def accept_passive(self, ):
        """
         return True if verb accept passive voice conjugation
        """
        return bool(self.verb_dict.get('passive', 0))

    def accept_confirmed(self, ):
        """
         return True if verb accept confirmed mood conjugation
        """
        return bool(self.verb_dict.get('confirmed', 0))

    def accept_future_moode(self, ):
        """
         return True if verb accept future_moode conjugation
        """
        return bool(self.verb_dict.get('future_moode', 0))

    # TODO: enhance
    def accept_tense(self, tense):
        """
         return True if verb accept conjugation in given tense
        """
        if tense in ("past", "الماضي") and self.accept_past():
            return True
        if tense in ("future", "present", "المضارع") and self.accept_future():
            return True
        if tense in ("imperative", "الأمر") and self.accept_imperative():
            return True
        if tense in ("passive", "مجهول") and self.accept_passive():
            return True
        if tense in ("confirmed", "مؤكد") and self.accept_confirmed():
            return True
        if tense in ("future_mood", "منصوب", "مرفوع", "مجزوم") and self.accept_future_moode():
            return True

        return False
    # TODO: enhance
    def accept_all_tenses(self):
        """
         return True if verb accept conjugation in given tense
        """
        return self.accept_past() \
        and self.accept_future()  \
        and self.accept_imperative()  \
        and self.accept_passive() \
        and self.accept_confirmed() \
        and  self.accept_future_moode()


    def accept_suffix(self, suffix):
        """
         return True if the word  accept given suffix,
        """

        return True

    def accept_prefix(self, prefix):
        """
         return True if the word  accept given prefix, 
        """
        return True

    # TODO: add verb extraction features
    def get_tags(self,):
        """
        return tags
        :return:
        """
        infos = self.get_tags_dict().values()
        #remove empty
        infos = [inf for inf in infos if inf]
        return infos

    def get_tags_dict(self, ):
        """
        This function extract verb feaures:
        * length: 3,4,5,6
        * weakness: weak, well
        * safety: hamza, shadda
        * kind of weakness: waw, yeh
        * category of weakness
        """
        tags_list = ["فعل", ]
        # remove duplicated
        tags_list = list(set(tags_list))

        # strip haraka and keep shadda
        verb_nm = self.get_unvocalized()
        verb_voc = self.get_vocalized()
        transitive = self.is_transitive()
        future_type = self.get_future_type()
        features = {"الفعل":verb_voc, "مضارعه": ""}

        # length
        vlength = len(verb_nm)
        features["طول"]= self.tab_type.get(vlength, "")
        verb_normalized = self.get_normalized()

        #التعدي
        if transitive :
            features["تعدي"] = "متعدي"
        else:
            features["تعدي"] = "لازم"
            # سالم أو مهموز أو مضعف
        if araby.SHADDA in verb_nm and araby.HAMZA in verb_normalized:
            features["سالم"] = "مضعف مهموز"
        elif araby.SHADDA in  verb_nm:
            features["سالم"] = "مضعف"
        elif araby.HAMZA in verb_normalized:
            features["سالم"] = "مهموز"
        else:
            features["سالم"] = ""

            # معتل
        features["علة"] = ""
        if vlength == 3:
            if verb_nm[0] == araby.WAW:
                # ~ if verb_nm[1] == araby.ALEF:
                # ~ feature["علة"] = "لفيف مقرون"
                if verb_nm[2] in(araby.ALEF, araby.ALEF_MAKSURA, araby.YEH):
                    features["علة"] = "لفيف مفروق"
                else:
                    features["علة"] = "مثال واوي"
            elif verb_nm[1] == araby.WAW:
                if verb_nm[2] in(araby.ALEF_MAKSURA, araby.YEH):
                    features["علة"] = "لفيف مقرون"
            elif verb_nm[1] == araby.ALEF:
                # ~ if verb_nm[2] in(araby.ALEF, araby.ALEF_MAKSURA, araby.YEH):
                # ~ feature["علة"] = "لفيف مفروق"
                if future_type == "ضمة":
                    features["علة"] = "أجوف واوي"
                elif future_type == "فتحة":
                    features["علة"] = "أجوف واوي"
                elif future_type == "كسرة":
                    features["علة"] = "أجوف يائي"
                else:
                    features["علة"] = "أجوف"
            elif verb_nm[2] == araby.ALEF or verb_nm[2] == araby.WAW:
                features["علة"] = "ناقص واوي"
            elif verb_nm[2] == araby.ALEF_MAKSURA or verb_nm[2] == araby.YEH:
                features["علة"] = "ناقص يائي"
            else:
                features["علة"] = "صحيح"
        else:
            if verb_nm[-2:-1] == araby.ALEF:
                features["علة"] = "أجوف"
            elif verb_nm[-1:] == araby.ALEF_MAKSURA:
                features["علة"] = "ناقص"
            else:
                features["علة"] = "صحيح"
        if not features["سالم"] and features["علة"] == "صحيح":
            features["سالم"]  = "سالم"
        return features

    def get_lemma(self, ):
        """
         return   get lemma, 
        """
        return self.verb_dict.get('vocalized', '')

    def get_definition(self, ):
        """
         return   get word definition,
        """
        return ""

    def get_note(self, ):
        """
         return   get word note,
        """
        return ""

    def __str__(self):
        """
        return tuple as string
        """
        return self.verb_dict.__str__()

    def __getitem__(self, key):
        """
        return attribute
        """
        return self.verb_dict.get(key, None)

    def __iter__(self):
        """
        :return:
        """
        yield from self.verb_dict.items()

    def get(self, key, default):
        """
        return attribute
        """
        return self.verb_dict.get(key, default)


def main():
    word = u'استقل'
    vtuple = {'think_trans': 1,
              'passive': 0,
              'confirmed': 0,
              'vocalized': u'اِسْتَقَلَّ',
              'stamped': u'ستقل',
              'future_moode': 0,
              'triliteral': 0,
              'future': 0,
              'unthink_trans': 0,
              'past': 0,
              'unvocalized': u'استقل',
              'future_type': u'َ',
              'double_trans': 0,
              'normalized': u'استقل',
              'reflexive_trans': 0,
              'imperative': 0,
              'transitive': 1,
              'root': u'قلل',
              'id': 7495},
    vt = VerbTuple(vtuple)
    print(vt)
    return 0


if __name__ == '__main__':
    main()
