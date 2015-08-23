#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from euler import *

start_time = time.clock()

p = 3797
for i in range(1, len(str(p))):
    print str(p)[-1 * i:], str(p)[:i]

print time.clock() - start_time
