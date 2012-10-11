#!/usr/bin/env python

# generate a bigram markov chain from killian's tweets
import re
import random

model = {}

for line in open('tweets.txt', 'r'):
  words = re.split('\s+', line)
  last_word = 'START'
  for word in words:
    if last_word in model and word in model[last_word]:
      model[last_word][word] += 1
    elif last_word in model and word not in model[last_word]:
      model[last_word][word] = 1
    else: # last_word not in model
      model[last_word] = {word: 1}
    last_word = word

  if last_word in model and 'END' in model[last_word]:
    model[last_word]['END'] += 1
  elif last_word in model and 'END' not in model[last_word]:
    model[last_word]['END'] = 1
  else: # last_word not in model
    model[last_word] = {'END': 1}


# generate
for i in range(10):
  tweet = ''
  word = 'START'
  while word is not 'END':
    if word is not 'START':
      tweet += word + ' '
    choices = model[word]
    r = random.randint(1, sum(choices.values()))
    for k in choices:
      r -= choices[k]
      if (r <= 0):
        word = k
        break
  print tweet
