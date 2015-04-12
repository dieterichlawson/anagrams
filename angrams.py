#!/usr/bin/env python
import argparse
from collections import defaultdict

# accept a dictionary file from the command line
parser = argparse.ArgumentParser(description='Print anagrams in a dictionary.')
parser.add_argument('dictfile', type=file, help='dictionary file with one word per line')
args = parser.parse_args()

# map to hold the anagram lists
anagrams = defaultdict(list)
for word in args.dictfile:
  word = word.strip()
  # only want words with at least 4 characters
  if len(word) < 4: continue
  # collapse case and sort characters alphabetically
  key = ''.join(sorted(word.lower()))
  anagrams[key].append(word)

for k, words in anagrams.iteritems():
  # print the sets for which there are at least 
  # as many anagrams as characters
  if len(k) <= len(words): print ", ".join(words)
