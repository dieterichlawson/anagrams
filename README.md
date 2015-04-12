# anagrams
`anagrams.py` is a simple tool to print anagrams from a list of words. It accepts a dictionary file that contains one word per line and prints the sets of anagrams for which there are at least as many anagrams as characters. It does not print words shorter than 4 characters.

### Example Usage
```
dlaw > planet $ ./angrams.py testdict.txt
reins, resin, rinse, risen, serin, siren
inert, inter, niter, retin, trine
merit, miter, mitre, remit, timer
emit, item, mite, time
inset, neist, snite, stein, stine
```
Note that neither "hello" nor "bye" anagrams are printed here despite being listed in the dictionary. "hello" was not printed because there are fewer anagrams in the dictionary than characters in the word. "bye" was not printed because it is shorter than the minimum length of 4.

### Implementation Details
This script works by adding each word to a map such that anagrams map to the same key. Since anagrams contain the same letters, we can just lowercase each word and sort the characters alphabetically to create such a key.
