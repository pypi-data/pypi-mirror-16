rbpy
===============================

version number: 0.1.1  
author: Matt Maybeno

Overview
--------

Python wrapper around the RelayBox API.

Installation / Usage
--------------------

To install use pip:

    $ pip install rbpy


Or clone the repo:

    $ git clone git@bitbucket.org:relaybox/rbpy.git
    $ python setup.py install
    

Example
-------

```python
from __future__ import print_function
import json
import rbpy

box = rbpy.Box('private_code_here', 'publid_id_here')
box.send('hello world private message')
box.send('hello world public message', public=True)
box.get()  # gets box messages
print(json.dumps(box.get(), indent=1))  # get box messages pretty
```
