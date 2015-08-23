#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from euler import *

start_time = time.clock()

print sum(set([(x  * y) for x in range(2,60) for y in range(123,10000//x) if (len(set(str(x) + str(y) + str(x * y)) - set('0')) == 9) ]))


print time.clock() - start_time
