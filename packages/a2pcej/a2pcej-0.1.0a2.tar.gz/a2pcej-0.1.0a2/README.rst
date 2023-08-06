a2pcej
======

**a2pcej**, convert Alphabet to Phonetic Code in English and Japanease.

This module convert each alphabet letters to phonetic code, and also
convert each alphabet letterts to katakana.

**IMPORTANT:** In current version, supported with Python 3.x, because of
Japanese Encoding issue.

Functions
~~~~~~~~~

conv\_al(letters, delimiter='-', upper\_sign='(CAPS)', num\_cnv\_flag=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

letters is string.

.. code:: python

    def conv_al(letters, delimiter='-', upper_sign='(CAPS)', num_cnv_flag=False):
        return _converter('alphabet_en', letters, delimiter, upper_sign, num_cnv_flag)

conv\_ak(letters, delimiter='・', upper\_sign='（大文字）', num\_cnv\_flag=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

letters is string.

.. code:: python

    def conv_ak(letters, delimiter='・', upper_sign='（大文字）', num_cnv_flag=False):
        return _converter('alphabet_kana', letters, delimiter, upper_sign, num_cnv_flag)

Simple example of usage as below...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, import module.

.. code:: python

    Import module.
    >>> from a2pcej import *

Convert 'exsamples' to Ponetic code in English.

.. code:: python

    >>> conv_al('examples')
    'ECHO, X―RAY, ALFA, MIKE, PAPA, LIMA, ECHO, SIERRA,'

Convert 'exsamples' to Ponetic code in Japanese Katakana.

.. code:: python

    >>> conv_ak('examples')
    'イー・エクス・エイ・エム・ピー・エル・イー・エス'

| Non alphabet letters are not convert (default).
| Upper case lattters has (CAPS) or (大文字) sign (default).

.. code:: python

    >>> conv_al('Examples002')
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-0-0-2'
    >>> conv_ak('Examples002')
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・0・0・2'

You can change delimiter and Upper case letters sign.

.. code:: python

    >>> conv_al('Examples003', delimiter='//', upper_sign='(CAPITAL)')
    'Echo(CAPITAL)//Xray//Alfa//Mike//Papa//Lima//Echo//Sierra//0//0//3/'
    >>> conv_ak('Examples003', delimiter='//', upper_sign='(CAPITAL)')
    'イー(CAPITAL)//エクス//エイ//エム//ピー//エル//イー//エス//0//0//3/'

If you would like to convert numbers to phonetic code, set
``num_cnv_flag=True``.

.. code:: python

    >>> conv_al('Examples002', num_cnv_flag=True)
    'Echo(CAPS)-Xray-Alfa-Mike-Papa-Lima-Echo-Sierra-zero-zero-two'
    >>> conv_ak('Examples002', num_cnv_flag=True)
    'イー（大文字）・エクス・エイ・エム・ピー・エル・イー・エス・ゼロ・ゼロ・ニイ'
