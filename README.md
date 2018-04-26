#Arramooz
Arabic Dictionary for Morphological analysis (Python + SQLite API)

[![downloads]( https://img.shields.io/sourceforge/dt/arramooz.svg)](http://sourceforge.org/projects/arramooz)
[![downloads]( https://img.shields.io/sourceforge/dm/arramooz.svg)](http://sourceforge.org/projects/arramooz)
  
  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com
  Collect data manually Mohamed Kebdani, Morroco < med.kebdani gmail.com>
  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/arramooz-pysqlite/master/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/arramooz-pysqlite/master/LICENSE)
Tracker  |[linuxscout/arramooz-pysqlite/Issues](https://github.com/linuxscout/arramooz-pysqlite/issues)
Website  |[http://arramooz-pysqlite.sourceforge.net](http://arramooz-pysqlite.sourceforge.net)
Source  |[Github](http://github.com/linuxscout/arramooz-pysqlite)
Download  |[sourceforge](http://arramooz-pysqlite.sourceforge.net)
Feedbacks  |[Comments](https://github.com/linuxscout/arramooz-pysqlite/)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projectsarramooz-pysqlite/)
#Description

Arramooz Alwaseet is an open source Arabic dictionary for morphological analyze,
It can help Natural Language processing developers.
This work is generated from the Ayaspell( Arabic spellchecker) brut data, which are collected manually.

This dictionary consists of three parts :

- stop words
- verbs
- Nouns

##Files formats and BUILD Dictionary in multiple format

Look at  [arramooz](https://github.com/linuxscout/arramooz/)

###Database description

Field | Description |  وصف
-------------|----------------|-----------------------------------
vocalized |vocalized word|الكلمة مشكولة
unvocalized |unvocalized word |الكلمة غير مشكولة
root |root of the verb|جذر الفعل
future_type |The future mark, used only ofr trilateral verbs|حركة عين الفعل الثلاثي في المضارع
triliteral |the verb is triliteral (3 letters) or not |الفعل ثلاثي/غير ثلاثي
transitive |transitive or not|فعل متعدي/ لازم
double_trans |has double transitivity for two objetcs|متعدي لمفعولين
think_trans|the verb is transitive to human|متعدي للغاقل
unthink_trans  |the verb is transitive to unhuman being|متعدي لغير العاقل
reflexive_trans |pronominal verb|فعل من أفعال القلوب
past  |can be conjugated in past tense |يتصرف في الماضي
future  |can be conjugated in present and future  tense|يتصرف في المضارع
imperative  |can be conjugated in imperative  |يتصرف في الأمر
passive |can be conjugated in passive voice|يتصرف في المبني للمجهول
future_moode |can be conjugated in  future moode (jusive, subjuctive, ) |يتصرف في المضارع المجزوم أو المنصوب
confirmed  |can be conjugated in confirmed  tenses|يتصرف في المؤكد

###SQL format of verb

```SQL
create table verbs
            (
            id int unique,
            vocalized varchar(30) not null,
            unvocalized varchar(30) not null,
            root varchar(30),
            normalized varchar(30) not null,
            stamp varchar(30) not null,
            future_type varchar(5),
            triliteral  tinyint(1) default 0, 
            transitive  tinyint(1) default 0, 
            double_trans  tinyint(1) default 0, 
            think_trans  tinyint(1) default 0, 
            unthink_trans  tinyint(1) default 0, 
            reflexive_trans  tinyint(1) default 0, 
            past  tinyint(1) default 0, 
            future  tinyint(1) default 0,  
            imperative  tinyint(1) default 0, 
            passive  tinyint(1) default 0,  
            future_moode  tinyint(1) default 0, 
            confirmed  tinyint(1) default 0, 
            PRIMARY KEY (id)
            );
```
            
##Nouns

###Database description

Field | Description |  وصف
-------------|----------------|-----------------------------------
vocalized|vocalized word|الكلمة مشكولة
unvocalized |unvocalized word|غير مشكولة
wordtype |word type( Noun of Subject, noun of object, …)|نوع الكلمة (اسم فاعل، اسم مفعول، صيغة مبالغة..)
root |word root|جذر الكلمة
category|word category|صنف الكلمة أو قسمها الفرعي
original|original verb or noun (masdar)|مصدر الكلمة فعل او اسم
mankous|if the word is mankous, ends with Yeh|اسم منقوص
feminable |the word accept Teh_marbuta|يقبل تاء التأنيث
defined| the word is defined or not |معرفة
gender|the word gender|نوع أو جنس الكلمة
feminin| the feminin form of the word|مؤنث الكلمة
masculin| the masculin form of the word| مذكر الكلمة
number |the word is sigle, dual or plural|عدد مفرد/مثنى/جمع
single| the single form of the word|مفرد الكلمة
dualable |accept dual suffix|يقبل التثنية
masculin_plural |accept masculine plural|يقبل جمع المذكر السالم
feminin_plural |accept feminin plural|يقبل جمع المؤنث السالم
broken_plural |the irregular plural if exists|جموع تكسيره إن وجدت
mamnou3_sarf |doesnt accept tanwin|ممنوع من الصرف
relative|relative |منسوب يالياء
w_suffix |accept waw suffix|يقبل الاحقة ـو الخاصة بجمع المذكر السالم عند إضافته إلى ما بعده
hm_suffix |accept Heh+Meem suffix|يقبل اللاحقة ـهم
kal_prefix |accept Kaf+Alef+Lam  prefixe|يقبل السابقة كالـ
ha_suffix|accept Heh suffix|يقبل اللاحقة ـه
k_prefix|accept preposition prefixes without "AL" definition article |يقبل سابقة الجر  دون ال التعريف
annex |accept the oral annexation|يقبل الإضافة إلى ما بعده مثل المقيمي الصلاة
definition |word description|شرح الكلمة
note |notes about the dictionary entry.|ملاحظات على المدخل في القاموس

###SQL format of noun

```sql
CREATE TABLE  IF NOT EXISTS `nouns` (
          `id` int(11) unique,
          `vocalized` varchar(30) DEFAULT NULL,
          `unvocalized` varchar(30) DEFAULT NULL,
          `normalized` varchar(30) DEFAULT NULL,
          `stamp` varchar(30) DEFAULT NULL,
          `wordtype` varchar(30) DEFAULT NULL,
          `root` varchar(10) DEFAULT NULL,
          `wazn` varchar(30) DEFAULT NULL,
          `category` varchar(30) DEFAULT NULL,
          `original` varchar(30) DEFAULT NULL,
          `gender` varchar(30) DEFAULT NULL,
          `feminin` varchar(30) DEFAULT NULL,
          `masculin` varchar(30) DEFAULT NULL,
          `number` varchar(30) DEFAULT NULL,
          `single` varchar(30) DEFAULT NULL,
          `broken_plural` varchar(30) DEFAULT NULL,            
          `defined` tinyint(1) DEFAULT 0,
          `mankous` tinyint(1) DEFAULT 0,
          `feminable` tinyint(1) DEFAULT 0,
          `dualable` tinyint(1) DEFAULT 0,
          `masculin_plural` tinyint(1) DEFAULT 0,
          `feminin_plural` tinyint(1) DEFAULT 0,
          `mamnou3_sarf` tinyint(1) DEFAULT 0,
          `relative` tinyint(1) DEFAULT 0,
          `w_suffix` tinyint(1) DEFAULT 0,
          `hm_suffix` tinyint(1) DEFAULT 0,
          `kal_prefix` tinyint(1) DEFAULT 0,
          `ha_suffix` tinyint(1) DEFAULT 0,
          `k_prefix` tinyint(1) DEFAULT 0,
          `annex` tinyint(1) DEFAULT 0,
          `definition` text,
          `note` text
        ) ;
```
###Usage
```python
>>> import arramooz.arabicdictionary 
>>> mydict = arramooz.arabicdictionary.ArabicDictionary('verbs')
>>> wordlist = [u"استقلّ", u'استقل', u"كذب"]
>>> tmp_list = []
>>> for word in wordlist:
>>> foundlist = mydict.lookup(word)
>>> for word_tuple in foundlist:
>>>     word_tuple = dict(word_tuple) 
>>>     vocalized = word_tuple['vocalized']
>>>     tmp_list.append(dict(word_tuple))
>>> print(tmp_list)
[{'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'اِسْتَقَلَّ', 'stamped': u'ستقل', 'future_moode': 0, 'triliteral': 0, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'استقل', 'future_type': u'َ', 'double_trans': 0, 'normalized': u'استقل', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'قلل', 'id': 7495},
{'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'كَذَبَ', 'stamped': u'كذب', 'future_moode': 0, 'triliteral': 1, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'كذب', 'future_type': u'كسرة', 'double_trans': 0, 'normalized': u'كذب', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'كذب', 'id': 1072},
{'think_trans': 1, 'passive': 0, 'confirmed': 0, 'vocalized': u'كَذَّبَ', 'stamped': u'كذب', 'future_moode': 0, 'triliteral': 0, 'future': 0, 'unthink_trans': 0, 'past': 0, 'unvocalized': u'كذب', 'future_type': u'َ', 'double_trans': 0, 'normalized': u'كذب', 'reflexive_trans': 0, 'imperative': 0, 'transitive': 1, 'root': u'كذب', 'id': 2869}]

```
*[requirement]

    1- libqutrub
    
    2- pyarabic 

