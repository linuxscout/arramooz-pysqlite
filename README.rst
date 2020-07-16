Arramooz
========

Arabic Dictionary for Morphological analysis (Python + SQLite API)


Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com Collect data manually Mohamed Kebdani, Morroco < med.kebdani
gmail.com>

Features \| value
---------\|---------------------------------------------------------------------------------
Authors \|
`Authors.md <https://github.com/linuxscout/arramooz-pysqlite/master/AUTHORS.md>`__
Release \| 0.1 License
\|\ `GPL <https://github.com/linuxscout/arramooz-pysqlite/master/LICENSE>`__
Tracker
\|\ `linuxscout/arramooz-pysqlite/Issues <https://github.com/linuxscout/arramooz-pysqlite/issues>`__
Website \|\ http://arramooz-pysqlite.sourceforge.net Source
\|\ `Github <http://github.com/linuxscout/arramooz-pysqlite>`__ Download
\|\ `sourceforge <http://arramooz-pysqlite.sourceforge.net>`__ Feedbacks
\|\ `Comments <https://github.com/linuxscout/arramooz-pysqlite/>`__
Accounts \|[@Twitter](https://twitter.com/linuxscout)
[@Sourceforge](http://sourceforge.net/projectsarramooz-pysqlite/) #
Description

Arramooz Alwaseet is an open source Arabic dictionary for morphological
analyze, It can help Natural Language processing developers. This work
is generated from the Ayaspell( Arabic spellchecker) brut data, which
are collected manually.

This dictionary consists of three parts :

-  stop words
-  verbs
-  Nouns

Files formats and BUILD Dictionary in multiple format
-----------------------------------------------------

Look at `arramooz <https://github.com/linuxscout/arramooz/>`__

Database description
~~~~~~~~~~~~~~~~~~~~

+----------------+-------------------+--------------------------------------+
| Field          | Description       | وصف                                  |
+================+===================+======================================+
| vocalized      | vocalized word    | الكلمة مشكولة                        |
+----------------+-------------------+--------------------------------------+
| unvocalized    | unvocalized word  | الكلمة غير مشكولة                    |
+----------------+-------------------+--------------------------------------+
| root           | root of the verb  | جذر الفعل                            |
+----------------+-------------------+--------------------------------------+
| future\_type   | The future mark,  | حركة عين الفعل الثلاثي في المضارع    |
|                | used only ofr     |                                      |
|                | trilateral verbs  |                                      |
+----------------+-------------------+--------------------------------------+
| triliteral     | the verb is       | الفعل ثلاثي/غير ثلاثي                |
|                | triliteral (3     |                                      |
|                | letters) or not   |                                      |
+----------------+-------------------+--------------------------------------+
| transitive     | transitive or not | فعل متعدي/ لازم                      |
+----------------+-------------------+--------------------------------------+
| double\_trans  | has double        | متعدي لمفعولين                       |
|                | transitivity for  |                                      |
|                | two objetcs       |                                      |
+----------------+-------------------+--------------------------------------+
| think\_trans   | the verb is       | متعدي للغاقل                         |
|                | transitive to     |                                      |
|                | human             |                                      |
+----------------+-------------------+--------------------------------------+
| unthink\_trans | the verb is       | متعدي لغير العاقل                    |
|                | transitive to     |                                      |
|                | unhuman being     |                                      |
+----------------+-------------------+--------------------------------------+
| reflexive\_tra | pronominal verb   | فعل من أفعال القلوب                  |
| ns             |                   |                                      |
+----------------+-------------------+--------------------------------------+
| past           | can be conjugated | يتصرف في الماضي                      |
|                | in past tense     |                                      |
+----------------+-------------------+--------------------------------------+
| future         | can be conjugated | يتصرف في المضارع                     |
|                | in present and    |                                      |
|                | future tense      |                                      |
+----------------+-------------------+--------------------------------------+
| imperative     | can be conjugated | يتصرف في الأمر                       |
|                | in imperative     |                                      |
+----------------+-------------------+--------------------------------------+
| passive        | can be conjugated | يتصرف في المبني للمجهول              |
|                | in passive voice  |                                      |
+----------------+-------------------+--------------------------------------+
| future\_moode  | can be conjugated | يتصرف في المضارع المجزوم أو المنصوب  |
|                | in future moode   |                                      |
|                | (jusive,          |                                      |
|                | subjuctive, )     |                                      |
+----------------+-------------------+--------------------------------------+
| confirmed      | can be conjugated | يتصرف في المؤكد                      |
|                | in confirmed      |                                      |
|                | tenses            |                                      |
+----------------+-------------------+--------------------------------------+

SQL format of verb
~~~~~~~~~~~~~~~~~~

.. code:: sql

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

Nouns
-----

Database description
~~~~~~~~~~~~~~~~~~~~

+----------------+-------------------+--------------------------------------+
| Field          | Description       | وصف                                  |
+================+===================+======================================+
| vocalized      | vocalized word    | الكلمة مشكولة                        |
+----------------+-------------------+--------------------------------------+
| unvocalized    | unvocalized word  | غير مشكولة                           |
+----------------+-------------------+--------------------------------------+
| wordtype       | word type( Noun   | نوع الكلمة (اسم فاعل، اسم مفعول،     |
|                | of Subject, noun  | صيغة مبالغة..)                       |
|                | of object, …)     |                                      |
+----------------+-------------------+--------------------------------------+
| root           | word root         | جذر الكلمة                           |
+----------------+-------------------+--------------------------------------+
| category       | word category     | صنف الكلمة أو قسمها الفرعي           |
+----------------+-------------------+--------------------------------------+
| original       | original verb or  | مصدر الكلمة فعل او اسم               |
|                | noun (masdar)     |                                      |
+----------------+-------------------+--------------------------------------+
| mankous        | if the word is    | اسم منقوص                            |
|                | mankous, ends     |                                      |
|                | with Yeh          |                                      |
+----------------+-------------------+--------------------------------------+
| feminable      | the word accept   | يقبل تاء التأنيث                     |
|                | Teh\_marbuta      |                                      |
+----------------+-------------------+--------------------------------------+
| defined        | the word is       | معرفة                                |
|                | defined or not    |                                      |
+----------------+-------------------+--------------------------------------+
| gender         | the word gender   | نوع أو جنس الكلمة                    |
+----------------+-------------------+--------------------------------------+
| feminin        | the feminin form  | مؤنث الكلمة                          |
|                | of the word       |                                      |
+----------------+-------------------+--------------------------------------+
| masculin       | the masculin form | مذكر الكلمة                          |
|                | of the word       |                                      |
+----------------+-------------------+--------------------------------------+
| number         | the word is       | عدد مفرد/مثنى/جمع                    |
|                | sigle, dual or    |                                      |
|                | plural            |                                      |
+----------------+-------------------+--------------------------------------+
| single         | the single form   | مفرد الكلمة                          |
|                | of the word       |                                      |
+----------------+-------------------+--------------------------------------+
| dualable       | accept dual       | يقبل التثنية                         |
|                | suffix            |                                      |
+----------------+-------------------+--------------------------------------+
| masculin\_plur | accept masculine  | يقبل جمع المذكر السالم               |
| al             | plural            |                                      |
+----------------+-------------------+--------------------------------------+
| feminin\_plura | accept feminin    | يقبل جمع المؤنث السالم               |
| l              | plural            |                                      |
+----------------+-------------------+--------------------------------------+
| broken\_plural | the irregular     | جموع تكسيره إن وجدت                  |
|                | plural if exists  |                                      |
+----------------+-------------------+--------------------------------------+
| mamnou3\_sarf  | doesnt accept     | ممنوع من الصرف                       |
|                | tanwin            |                                      |
+----------------+-------------------+--------------------------------------+
| relative       | relative          | منسوب يالياء                         |
+----------------+-------------------+--------------------------------------+
| w\_suffix      | accept waw suffix | يقبل الاحقة ـو الخاصة بجمع المذكر    |
|                |                   | السالم عند إضافته إلى ما بعده        |
+----------------+-------------------+--------------------------------------+
| hm\_suffix     | accept Heh+Meem   | يقبل اللاحقة ـهم                     |
|                | suffix            |                                      |
+----------------+-------------------+--------------------------------------+
| kal\_prefix    | accept            | يقبل السابقة كالـ                    |
|                | Kaf+Alef+Lam      |                                      |
|                | prefixe           |                                      |
+----------------+-------------------+--------------------------------------+
| ha\_suffix     | accept Heh suffix | يقبل اللاحقة ـه                      |
+----------------+-------------------+--------------------------------------+
| k\_prefix      | accept            | يقبل سابقة الجر دون ال التعريف       |
|                | preposition       |                                      |
|                | prefixes without  |                                      |
|                | "AL" definition   |                                      |
|                | article           |                                      |
+----------------+-------------------+--------------------------------------+
| annex          | accept the oral   | يقبل الإضافة إلى ما بعده مثل المقيمي |
|                | annexation        | الصلاة                               |
+----------------+-------------------+--------------------------------------+
| definition     | word description  | شرح الكلمة                           |
+----------------+-------------------+--------------------------------------+
| note           | notes about the   | ملاحظات على المدخل في القاموس        |
|                | dictionary entry. |                                      |
+----------------+-------------------+--------------------------------------+

SQL format of noun
~~~~~~~~~~~~~~~~~~

.. code:: sql

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

Usage
~~~~~

.. code:: python

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

\*[requirement]

::

    1- libqutrub

    2- pyarabic 


