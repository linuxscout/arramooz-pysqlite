# Arramooz
Arabic Dictionary for Morphological analysis (Python + SQLite API)

[![downloads]( https://img.shields.io/sourceforge/dt/arramooz.svg)](http://sourceforge.org/projects/arramooz)
[![downloads]( https://img.shields.io/sourceforge/dm/arramooz.svg)](http://sourceforge.org/projects/arramooz)
  
  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com
  Collect data manually Mohamed Kebdani, Morroco < med.kebdani gmail.com>
  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/arramooz-pysqlite/master/AUTHORS.md)
Release  | 0.4
License  |[GPL](https://github.com/linuxscout/arramooz-pysqlite/master/LICENSE)
Tracker  |[linuxscout/arramooz-pysqlite/Issues](https://github.com/linuxscout/arramooz-pysqlite/issues)
Website  |[http://arramooz-pysqlite.sourceforge.net](http://arramooz-pysqlite.sourceforge.net)
Source  |[Github](http://github.com/linuxscout/arramooz-pysqlite)
Download  |[sourceforge](http://arramooz-pysqlite.sourceforge.net)
Feedbacks  |[Comments](https://github.com/linuxscout/arramooz-pysqlite/)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projectsarramooz-pysqlite/)

## Description

Arramooz Alwaseet is an open source Arabic dictionary for morphological analyze,
It can help Natural Language processing developers.
This work is generated from the Ayaspell( Arabic spellchecker) brut data, which are collected manually.

This dictionary consists of three parts :

- stop words
- verbs
- Nouns

## Files formats and BUILD Dictionary in multiple format

For details about  Data Structure, Look at  [arramooz](https://github.com/linuxscout/arramooz/blob/master/docs/datastructures.md)

### Database description

### Usage
```python
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

```
#### [requirement]

    1- libqutrub
 
    2- pyarabic 

