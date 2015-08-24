#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from euler import *
start_time = time.clock()
''' '''

x = 125478
s = "".join(sorted(list(str(x))))
print s

print time.clock() - start_time
