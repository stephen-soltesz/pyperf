#!/usr/bin/python 

import random
import timer
import string


def dict_key_int(l):
  d = {}
  for i in xrange(l):
    if i not in d:
      d[i] = i
    else:
      y = d[i]


def create(key_type, count, max_key, max_str):
  d = {}
  keys = []
  for i in xrange(count):
    if key_type == int:
      r = int(max_key * random.random())
    elif key_type == str:
      r = string_key(max_str)
    elif key_type == tuple:
      r1 = int(max_key * random.random())
      r2 = int(max_key * random.random())
      r3 = int(max_key * random.random())
      r4 = int(max_key * random.random())
      r = (r1, r2, r3, r4)
    d[r] = i
    keys.append(r)
  return d, keys


def string_key(n):
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in xrange(n))


key_count = 100000
max_key = 100000
max_str = 40
rounds = 10000000

inputs = [int, str, tuple]

for key_type in inputs:
  d, keys = create(key_type, key_count, max_key, 0)
  with timer.Timer() as t:
    for i in xrange(rounds):
      k = keys[i % key_count]
  base = t.usecs / rounds

  d, keys = create(key_type, key_count, max_key, max_str)
  with timer.Timer() as t:
    for i in xrange(rounds):
      k = keys[i % key_count]
      _ = d[k]
  print str(key_type), base, (t.usecs / rounds) - base
