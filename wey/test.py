#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from euler import *

start_time = time.clock()

p = 13
print int(float(p) / 10) + (p % 10) * 10 ** (len(str(p)) - 1)

print time.clock() - start_time
