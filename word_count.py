"""
INPUT:

document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"


output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]

for 

use seperator to get words = ["Practice", "makes", "perfect",    ...]

iterate through words :
 add to dict
 
Time - O(n)
Space - O(n)

For sorting:
 as for the sorting part, rather than sorting the entries in the map directly, which takes O(M⋅log(M)) - where M is number of unique words in document - a better solution will be to place words into an array of string arrays indexed by the occurrence number and then iterate through the array in the reverse order. This is similar to a Bucket Sort. The proposed solution trades off a bit of space for performance, which may be a reasonable trade under certain circumstances.

"""

import string
import re
from collections import OrderedDict, Counter

def word_count_engine(document):
  
  #words = re.split(r"[\s]\s*", document)
  words = re.sub(r'[^\w\s]', '', document) 
  words = re.split(r'\W+', words)

  words_dict = OrderedDict()
    
  for word in words:
    if(len(word) > 0):
      word = word.lower()# O(n*m), where m is length of curr string
      #word.replace("'", "")
      if word in words_dict:   
        words_dict[word] += 1
      else:
        words_dict[word] = 1
  
  #print(words_dict)
  sorted_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
  
  for i,word in enumerate(sorted_words):
    x,y = word

    sorted_words[i] = (x,str(y))
  
  return sorted_words

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

print(word_count_engine(document))
