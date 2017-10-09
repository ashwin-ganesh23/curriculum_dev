"""
Functional Programming in Python

Topics include:
	-Warm-up: File Objects
	-OS Module
	-Intro to Regular Expressions

Part 5 : Regular Expression Use Cases

"""

# phone numbers, emails, files

import re

ph_re = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}')
p_re = re.compile(r'[0-9]{3}')
#mo = re.search(ph_re, "asd510-449-3404 423-322-4343")
mo = re.match(ph_re, "510-449-3404 423-322-4343")
print(mo.group())
